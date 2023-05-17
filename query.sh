#!/bin/bash
DIR=$1
shift
FILES="$@"

docker run -it -v ${DIR}:${DIR} securelint:latest query --test 'rules/java-rules.txt' ${FILES}