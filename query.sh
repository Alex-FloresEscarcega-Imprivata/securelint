#!/bin/bash

start_time=$(date +%s)
debug_mode=false
git_mode=false
DIR=$1
shift


if [ "$DIR" == "." ]; then
  DIR=$(pwd)
fi

FILES=()
LINES_EDITED=""

temp_rules_file=$(mktemp)
real_rules_file="/Users/afloresescarcega/REPOS/securelint/rules/java-rules.txt"

while IFS= read -r line; do
  echo "$line" >> "$temp_rules_file"
done < "$real_rules_file"

while getopts "dgq:" opt; do
  case ${opt} in
    d )
      debug_mode=true
      ;;
    g )
      git_mode=true
      while IFS= read -r line; do
        FILES+=("$DIR/$line")
      done < <(git diff --name-only master)
      LINES_EDITED=$(git diff master | perl -lane 'if (/^\+\+\+ b\/([^\n]*)/) {$filename = $1;} if (/^@@ -[0-9]+,[0-9] \+([0-9]+),([0-9]+) @@/) { $start=$1; $end=$2; $sum = $start + $end - 1; print "${filename} ${start} ${sum}"; }')
      ;;
    q )
      echo "$OPTARG" >> "$temp_rules_file"
      ;;
    /? )
      echo "Invalid option: $OPTARG" 1>&2
      exit 1
      ;;
  esac
done
shift "$((OPTIND -1))"

if [ ${#FILES[@]} -eq 0 ]; then
  FILES=("$@")
fi

PARENT_JSON="{}"

QUERY_RESULT=$(docker run -v "${temp_rules_file}":"/rules/${temp_rules_file}" -v "${DIR}":"${DIR}" securelint:latest query --test "/rules/${temp_rules_file}" ${FILES[@]} | /Users/afloresescarcega/REPOS/securelint/consume_query.py)
PARENT_JSON=$(jq --argjson QUERY "$QUERY_RESULT" '. + $QUERY' <<< "$PARENT_JSON")
if [ $? -ne 0 ]; then
  echo "jq failed. Here was the query result"
  echo "$QUERY_RESULT"
  exit 1
fi


rm "$temp_rules_file"
if $git_mode; then
  while read -r lines_edited_line; do
    filename="$DIR/$(echo "$lines_edited_line" | cut -d' ' -f1)"
    start_line="$(echo "$lines_edited_line" | cut -d' ' -f2)"
    end_line="$(echo "$lines_edited_line" | cut -d' ' -f3)"

    if jq -e .\""$filename"\" <<< "$PARENT_JSON" > /dev/null; then
      PARENT_JSON=$(jq --arg finame "$filename" --argjson startt "$start_line" --argjson endd "$end_line" '.[$finame] += [[ $startt, $endd ]]' <<< "$PARENT_JSON")
    else
      PARENT_JSON=$(jq --arg finame "$filename" --argjson startt "$start_line" --argjson endd "$end_line" '.[$finame] = [[ $startt, $endd ]]' <<< "$PARENT_JSON")
    fi

  done <<< "$LINES_EDITED"
fi
echo "$PARENT_JSON" | /Users/afloresescarcega/REPOS/securelint/final_consumer.py


# don't add new lines below to best measure the total time elapsed of program
end_time=$(date +%s)
elapsed_time=$((end_time - start_time))

if $debug_mode; then
  echo "Time elapsed:: $elapsed_time seconds "
fi