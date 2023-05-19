from Range import Range
from RangeSet import RangeSet


import json
from typing import Any


class RangeSetEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, RangeSet):
            return o.ranges
        elif isinstance(o, Range):
            return {'start': o.start, 'end': o.end}
        return super().default(o)