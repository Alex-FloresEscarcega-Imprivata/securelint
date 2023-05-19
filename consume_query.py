#!/usr/local/bin/python3
import json
import re
from RangeSet import RangeSet
from RangeSetEncoder import RangeSetEncoder

import sys


def parse_line(file_line):
    key, value = file_line.split(": ", 1)
    key = key.strip().replace(" ", "_")
    value = value.strip()
    return key, value


"""
output = 
[
  {
    "path": "/Users/afloresescarcega/REPOS/parent/service-impl/src/test/java/rss/web/seamless/VendorClientTest.java",
    "patterns": "patterns": [
      {
        "pattern": 0,
        "captures": [
          {
            "capture": "0 - annotation, start: (76, 5), end: (76, 14), text: `Autowired`"
          },
          {
            "capture": "1 - field, start: (76, 45), end: (76, 66), text: `connectRequestService`"
          }
        ],
        "pattern_range_set": [
          {
            "start": "76",
            "end": "76"
          }
        ]
      }],
    "file_range_set": [
      {
        "start": "76",
        "end": "76"
      }]
  }
]
"""

output = []
current_file = None
current_pattern = None

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    if line.startswith("/Users/"):
        current_file = {"path": line, "patterns": [], "file_range_set": RangeSet()}
        output.append(current_file)
    elif line.startswith("pattern:"):
        _, pattern_value = parse_line(line)
        current_pattern = {"pattern": int(pattern_value), "captures": [], "pattern_range_set": RangeSet()}
        current_file["patterns"].append(current_pattern)
    elif line.startswith("capture:"):
        capture_dict = {}
        current_pattern["captures"].append(capture_dict)
        _, capture_value = parse_line(line)
        capture_dict["capture"] = capture_value
        pattern = r"start: \((\d+), \d+\), end: \((\d+), \d+\)"
        match = re.search(pattern, capture_value)
        start_row, end_row = match.groups()
        start_row, end_row = int(start_row), int(end_row)
        current_pattern["pattern_range_set"].add(start_row, end_row)
        current_file["file_range_set"].add(start_row, end_row)
    else:
        k, v = parse_line(line)
        capture_dict[k] = v

output = {"queries": output}
json_output = json.dumps(output, indent=4, cls=RangeSetEncoder)
print(json_output)
