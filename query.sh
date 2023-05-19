#!/bin/bash
DIR=$1
shift


if [ "$DIR" == "." ]; then
  DIR=$(pwd)
fi

FILES=()
LINES_EDITED=()

while getopts "g" opt; do
  case ${opt} in
    g )
      while IFS= read -r line; do
        FILES+=("$DIR/$line")
      done < <(git diff --name-only master)
      # FILES=$(git diff --name-only master | while read file; do if [ -e "$DIR/$file" ]; then printf "'%s' " "$DIR/$file"; fi; done)
      LINES_EDITED=$(git diff master | perl -lane 'if (/^\+\+\+ b\/([^\n]*)/) {$filename = $1;} if (/^@@ -[0-9]+,[0-9] \+([0-9]+),([0-9]+) @@/) { $start=$1; $end=$2; $sum = $start + $end - 1; print "${filename} ${start} ${sum}"; }')
      ;;
    /? )
      echo "Invalid option: $OPTARG" 1>&2
      exit 1
      ;;
  esac
done
# echo $FILES
shift $((OPTIND -1))

if [ ${#FILES[@]} -eq 0 ]; then
  FILES=("$@")
fi
# echo \n\n
# echo $FILES
# echo $DIR
# echo "docker run -it -v ${DIR}:${DIR} securelint:latest query --test 'rules/java-rules.txt' ${FILES}"
# docker run -it -v ${DIR}:${DIR} securelint:latest query --test 'rules/java-rules.txt' ${FILES[@]}
QUERY_RESULT=$(docker run -it -v ${DIR}:${DIR} securelint:latest query --test 'rules/java-rules.txt' ${FILES[@]} | /Users/afloresescarcega/REPOS/securelint/consume_query.py)
# QUERY_RESULT=$(docker run -it -v ${DIR}:${DIR} securelint:latest query --test 'rules/java-rules.txt' ${FILES[@]})
echo $QUERY_RESULT
JSON="{}"
while read -r lines_edited_line; do
  filename="$DIR/$(echo $lines_edited_line | cut -d' ' -f1)"
  start_line="$(echo $lines_edited_line | cut -d' ' -f2)"
  end_line="$(echo $lines_edited_line | cut -d' ' -f3)"
  # echo $filename $start_line $end_line
  
  if jq -e .\"$filename\" <<< "$JSON" > /dev/null; then
    JSON=$(jq --arg finame $filename --argjson startt $start_line --argjson endd $end_line '.[$finame] += [[ $startt, $endd ]]' <<< "$JSON")
  else
    JSON=$(jq --arg finame $filename --argjson startt $start_line --argjson endd $end_line '.[$finame] = [[ $startt, $endd ]]' <<< "$JSON")
  fi
  
done <<< "$LINES_EDITED"
# echo $JSON
#output=$(git diff master | perl -ne 'if (/^\+\+\+ b\/(.*)$/) {print "$1\n";} if (/^@@ -[0-9]+,[0-9] \+([0-9]+),([0-9]+) @@/) { print "$1 "; print $1 + $2 -1; print "\n"; }')
#output=$(git diff master | perl -lane 'if (/^\+\+\+ b\/([^\n]*)/) {$filename = $1;} if (/^@@ -[0-9]+,[0-9] \+([0-9]+),([0-9]+) @@/) { $start=$1; $end=$2; $sum = $start + $end - 1; print "${filename} ${start} ${sum}"; }')