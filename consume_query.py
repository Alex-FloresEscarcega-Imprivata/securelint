#!/usr/local/bin/python3
import json
import re
from RangeSet import RangeSet
from RangeSetEncoder import RangeSetEncoder

# from test_range import test_range



text = """/Users/afloresescarcega/REPOS/parent/service-impl/src/main/java/rss/service/SiteService.java
            pattern: 0
              capture: 0 - annotation, start: (76, 5), end: (76, 14), text: `Autowired`
              capture: 1 - field, start: (76, 45), end: (76, 66), text: `connectRequestService`
            pattern: 0
              capture: 0 - annotation, start: (77, 5), end: (77, 14), text: `Autowired`
              capture: 1 - field, start: (77, 40), end: (77, 56), text: `customerGroupDao`
            pattern: 0
              capture: 0 - annotation, start: (78, 5), end: (78, 14), text: `Autowired`
              capture: 1 - field, start: (78, 39), end: (78, 54), text: `customerService`
            pattern: 0
              capture: 0 - annotation, start: (79, 5), end: (79, 14), text: `Autowired`
              capture: 1 - field, start: (79, 46), end: (79, 68), text: `seamlessApplicationDao`
            pattern: 0
              capture: 0 - annotation, start: (80, 5), end: (80, 14), text: `Autowired`
              capture: 1 - field, start: (80, 46), end: (80, 68), text: `loggedOnUserRepository`
            pattern: 0
              capture: 0 - annotation, start: (81, 5), end: (81, 14), text: `Autowired`
              capture: 1 - field, start: (81, 45), end: (81, 66), text: `siteCredentialService`
            pattern: 0
              capture: 0 - annotation, start: (82, 5), end: (82, 14), text: `Autowired`
              capture: 1 - field, start: (82, 46), end: (82, 68), text: `siteCustomFieldService`
            pattern: 0
              capture: 0 - annotation, start: (83, 5), end: (83, 14), text: `Autowired`
              capture: 1 - field, start: (83, 37), end: (83, 50), text: `siteValidator`
            pattern: 0
              capture: 0 - annotation, start: (84, 5), end: (84, 14), text: `Autowired`
              capture: 1 - field, start: (84, 31), end: (84, 38), text: `siteDao`
            pattern: 0
              capture: 0 - annotation, start: (85, 5), end: (85, 14), text: `Autowired`
              capture: 1 - field, start: (85, 39), end: (85, 54), text: `sitePropertyDao`
            pattern: 0
              capture: 0 - annotation, start: (86, 5), end: (86, 14), text: `Autowired`
              capture: 1 - field, start: (86, 42), end: (86, 60), text: `histSiteUpgradeDao`
            pattern: 0
              capture: 0 - annotation, start: (87, 5), end: (87, 14), text: `Autowired`
              capture: 1 - field, start: (87, 34), end: (87, 44), text: `gatewayDao`
            pattern: 0
              capture: 0 - annotation, start: (88, 5), end: (88, 14), text: `Autowired`
              capture: 1 - field, start: (88, 38), end: (88, 52), text: `gatewayService`
            pattern: 0
              capture: 0 - annotation, start: (89, 5), end: (89, 14), text: `Autowired`
              capture: 1 - field, start: (89, 43), end: (89, 62), text: `userPropertyService`
            pattern: 0
              capture: 0 - annotation, start: (90, 5), end: (90, 14), text: `Autowired`
              capture: 1 - field, start: (90, 35), end: (90, 46), text: `userService`
            pattern: 0
              capture: 0 - annotation, start: (91, 5), end: (91, 14), text: `Autowired`
              capture: 1 - field, start: (91, 41), end: (91, 56), text: `propertyService`
            pattern: 0
              capture: 0 - annotation, start: (92, 5), end: (92, 14), text: `Autowired`
              capture: 1 - field, start: (92, 49), end: (92, 72), text: `accessExpirationService`
            pattern: 0
              capture: 0 - annotation, start: (93, 5), end: (93, 14), text: `Autowired`
              capture: 1 - field, start: (93, 53), end: (93, 80), text: `globalCredentialPoolService`
            pattern: 0
              capture: 0 - annotation, start: (94, 5), end: (94, 14), text: `Autowired`
              capture: 1 - field, start: (94, 48), end: (94, 70), text: `securelinkEventService`
            pattern: 0
              capture: 0 - annotation, start: (95, 5), end: (95, 14), text: `Autowired`
              capture: 1 - field, start: (95, 37), end: (95, 48), text: `requestUtil`
            pattern: 0
              capture: 0 - annotation, start: (96, 5), end: (96, 14), text: `Autowired`
              capture: 1 - field, start: (96, 40), end: (96, 54), text: `sessionFactory`
            pattern: 0
              capture: 0 - annotation, start: (97, 5), end: (97, 14), text: `Autowired`
              capture: 1 - field, start: (97, 39), end: (97, 54), text: `userSiteService`
            pattern: 0
              capture: 0 - annotation, start: (98, 5), end: (98, 14), text: `Autowired`
              capture: 1 - field, start: (98, 51), end: (98, 78), text: `credentialEncryptionService`
            pattern: 0
              capture: 0 - annotation, start: (99, 5), end: (99, 14), text: `Autowired`
              capture: 1 - field, start: (99, 38), end: (99, 52), text: `siteServiceDao`
            pattern: 0
              capture: 0 - annotation, start: (100, 5), end: (100, 14), text: `Autowired`
              capture: 1 - field, start: (100, 49), end: (100, 68), text: `notificationService`
            pattern: 0
              capture: 0 - annotation, start: (101, 5), end: (101, 14), text: `Autowired`
              capture: 1 - field, start: (101, 38), end: (101, 52), text: `messageService`
            pattern: 0
              capture: 0 - annotation, start: (102, 5), end: (102, 14), text: `Autowired`
              capture: 1 - field, start: (102, 43), end: (102, 62), text: `sitePropertyService`
            pattern: 0
              capture: 0 - annotation, start: (103, 5), end: (103, 14), text: `Autowired`
              capture: 1 - field, start: (103, 50), end: (103, 76), text: `gatekeeperHostGroupService`
            pattern: 0
              capture: 0 - annotation, start: (104, 5), end: (104, 14), text: `Autowired`
              capture: 1 - field, start: (104, 40), end: (104, 56), text: `siteGroupBindDao`
            pattern: 0
              capture: 0 - annotation, start: (105, 5), end: (105, 14), text: `Autowired`
              capture: 1 - field, start: (105, 54), end: (105, 84), text: `siteHostServicePropertyService`
            pattern: 0
              capture: 0 - annotation, start: (106, 5), end: (106, 14), text: `Autowired`
              capture: 1 - field, start: (106, 44), end: (106, 64), text: `sessionClientService`
            pattern: 0
              capture: 0 - annotation, start: (108, 5), end: (108, 14), text: `Autowired`
              capture: 1 - field, start: (108, 52), end: (108, 69), text: `sessionKeyFactory`
            pattern: 0
              capture: 0 - annotation, start: (109, 5), end: (109, 14), text: `Autowired`
              capture: 1 - field, start: (109, 41), end: (109, 58), text: `sessionKeyService`
            pattern: 0
              capture: 0 - annotation, start: (110, 5), end: (110, 14), text: `Autowired`
              capture: 1 - field, start: (110, 40), end: (110, 56), text: `userGroupService`
            pattern: 0
              capture: 0 - annotation, start: (111, 5), end: (111, 14), text: `Autowired`
              capture: 1 - field, start: (111, 37), end: (111, 50), text: `hibernateUtil`
            pattern: 0
              capture: 0 - annotation, start: (112, 5), end: (112, 14), text: `Autowired`
              capture: 1 - field, start: (112, 56), end: (112, 88), text: `versionTwoRegistrationKeyService`
            pattern: 0
              capture: 0 - annotation, start: (114, 5), end: (114, 14), text: `Autowired`
              capture: 1 - field, start: (114, 44), end: (114, 64), text: `changeEventPublisher`
            pattern: 0
              capture: 0 - annotation, start: (115, 5), end: (115, 14), text: `Autowired`
              capture: 1 - field, start: (115, 46), end: (115, 68), text: `notesEncryptionService`
            pattern: 0
              capture: 0 - annotation, start: (117, 5), end: (117, 14), text: `Autowired`
              capture: 1 - field, start: (117, 48), end: (117, 72), text: `userApprovalQueueService`
            pattern: 0
              capture: 0 - annotation, start: (118, 5), end: (118, 14), text: `Autowired`
              capture: 1 - field, start: (118, 48), end: (118, 72), text: `vendorRepApprovalService`
          /Users/afloresescarcega/REPOS/parent/service-impl/src/main/java/rss/web/seamless/SeamlessClient.java
          /Users/afloresescarcega/REPOS/parent/service-impl/src/main/java/rss/web/seamless/SeamlessSession.java
          /Users/afloresescarcega/REPOS/parent/service-impl/src/main/java/rss/web/seamless/SleClient.java
          /Users/afloresescarcega/REPOS/parent/service-impl/src/main/java/rss/web/seamless/SyncDatabase.java
          /Users/afloresescarcega/REPOS/parent/service-impl/src/main/java/rss/web/seamless/VendorClient.java
          /Users/afloresescarcega/REPOS/parent/service-impl/src/test/java/rss/web/seamless/SleClientTest.java
          /Users/afloresescarcega/REPOS/parent/service-impl/src/test/java/rss/web/seamless/SyncDatabaseTest.java
          /Users/afloresescarcega/REPOS/parent/service-impl/src/test/java/rss/web/seamless/VendorClientTest.java"""

import sys




def parse_line(line):
    key, value = line.split(": ", 1)
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

# text.split()
for line in sys.stdin:
# for line in text:
    # print(line)
    line =  line.strip()
    if not line:
        continue
    
    if line.startswith("/Users/"):
        current_file = {"path": line, "patterns": [], "file_range_set": RangeSet()}
        output.append(current_file)
        # print("New file\n\n\n\n")
    elif line.startswith("pattern:"):
        _,pattern_value = parse_line(line)
        current_pattern = {"pattern": int(pattern_value), "captures": [], "pattern_range_set": RangeSet()}
        current_file["patterns"].append(current_pattern)
        # print("New pattern\n\n")
    elif line.startswith("capture:"):
        capture_dict = {}
        current_pattern["captures"].append(capture_dict)
        _, capture_value = parse_line(line)
        capture_dict["capture"] = capture_value
        pattern = r"start: \((\d+), \d+\), end: \((\d+), \d+\)"
        # print(capture_value)
        match = re.search(pattern, capture_value)
        start_row, end_row = match.groups()
        start_row, end_row = int(start_row), int(end_row)
        # print("row: ", start_row, "end row: ", end_row)
        current_pattern["pattern_range_set"].add(start_row, end_row)
        # print('current_pattern["pattern_range_set"]:', current_pattern["pattern_range_set"])
        current_file["file_range_set"].add(start_row, end_row)
        # print('current_file["file_range_set"]:', current_file["file_range_set"])
        # print("")
    else:
        key, value = parse_line(line)
        capture_dict[key] = value

  

json_output = json.dumps(output, indent=4, cls=RangeSetEncoder)
print(json_output)