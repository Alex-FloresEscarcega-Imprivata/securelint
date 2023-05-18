#!/bin/bash
DIR=$1
shift


if [ "$DIR" == "." ]; then
  DIR=$(pwd)
fi

FILES=""

while getopts "g" opt; do
  case ${opt} in
    g )
      FILES=$(git diff --name-only master | awk -v dir="$DIR" '{printf "\"%s/%s\" ", dir, $0}')
      ;;
    /? )
      echo "Invalid option: $OPTARG" 1>&2
      exit 1
      ;;
  esac
done
echo $FILES
shift $((OPTIND -1))

if [ -z "$FILES" ]; then
  FILES="$@"
fi
echo $FILES
echo $DIR
docker run -it -v ${DIR}:${DIR} securelint:latest query --test 'rules/java-rules.txt' ${FILES}