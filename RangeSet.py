from Range import Range
# from RangeSetEncoder import RangeSetEncoder


import json


class RangeSet:
    def __init__(self):
        self.ranges = []

    def add(self, start, end):
        new_range = Range(start, end)
        for i, existing_range in enumerate(self.ranges):
            if existing_range.overlaps(new_range) or existing_range.touches(new_range):
                self.ranges[i] = existing_range.merge(new_range)
                return
        self.ranges.append(new_range)

    def __repr__(self):
        return f"RangeSet({self.ranges})"

    # def to_json(self):
    #     return json.dumps(self, cls=RangeSetEncoder)