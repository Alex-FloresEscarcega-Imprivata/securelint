#!/usr/local/bin/python3
import sys
import json
from RangeSet import RangeSet
from RangeSetEncoder import RangeSetEncoder

input_json = sys.stdin.read()

data = json.loads(input_json)


file_and_ranges = {}
for file, value in data.items():
    if file == "queries":
        continue
    file_and_ranges[file] = RangeSet()
    for range in value:
        file_and_ranges[file].add(range[0], range[1])
# print(file_and_ranges)
output = {}

def overlaps(query_file_range, file_and_ranges):
    for r in query_file_range.ranges:
        for rr in file_and_ranges[query["path"]].ranges:
            if rr.overlaps(r):
                return True
    return False

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


json_output = json.dumps(output, indent=4)
print(json_output)