# from RangeSetEncoder import RangeSetEncoder


import json


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlaps(self, other):
        return int(self.end) >= int(other.start) and int(self.start) <= int(other.end)

    def touches(self, o):
        return int(self.start) <= (int(o.end) + 1) and int(self.end) >= (int(o.start) - 1)

    def merge(self, other):
        self.start = min(self.start, other.start)
        self.end = max(self.end, other.end)
        return Range(self.start, self.end)

    def __repr__(self):
        return f"Range({self.start}, {self.end})"

    # def to_json(self):
    #     return json.dumps(self,  cls=RangeSetEncoder)