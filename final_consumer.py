#!/usr/local/bin/python3
import sys
import json
from RangeSet import RangeSet

input_json = sys.stdin.read()

data = json.loads(input_json)

file_and_ranges = {}
for file, value in data.items():
    if file == "queries":
        continue
    file_and_ranges[file] = RangeSet()
    for file_range in value:
        file_and_ranges[file].add(file_range[0], file_range[1])
output = {}


def overlaps(query_file_ranges, file_ranges):
    for query_range in query_file_ranges.ranges:
        for git_range in file_ranges[query["path"]].ranges:
            if git_range.overlaps(query_range):
                return True
    return False


if len(data) > 1:  # git mode
    for query in data["queries"]:
        if query["path"] not in file_and_ranges.keys():
            continue
        if len(query["file_range_set"]) == 0:
            continue
        query_file_range = RangeSet()
        for r in query["file_range_set"]:
            query_file_range.add(r["start"], r["end"])

        if overlaps(query_file_range, file_and_ranges):
            output[query["path"]] = query
else:  # not filtering on git output
    for query in data["queries"]:
        output[query["path"]] = query

json_output = json.dumps(output, indent=4)
print(json_output)
sys.stdout.flush()
