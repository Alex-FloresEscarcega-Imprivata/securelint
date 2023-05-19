from RangeSet import RangeSet


def test_range_set():
    r = RangeSet()
    r.add(2, 4)
    r.add(1, 3)
    assert repr(r) == "RangeSet([Range(1, 4)])"

    r = RangeSet()
    r.add(1, 3)
    r.add(2, 4)
    assert repr(r) == "RangeSet([Range(1, 4)])"

    r = RangeSet()
    r.add(1, 4)
    r.add(2, 3)
    assert repr(r) == "RangeSet([Range(1, 4)])"

    r = RangeSet()
    r.add(2, 3)
    r.add(1, 4)
    assert repr(r) == "RangeSet([Range(1, 4)])"

    r = RangeSet()
    r.add(1, 2)
    r.add(4, 5)
    assert repr(r) == "RangeSet([Range(1, 2), Range(4, 5)])"

    r = RangeSet()
    r.add(4, 5)
    r.add(1, 2)
    assert repr(r) == "RangeSet([Range(4, 5), Range(1, 2)])"

    r = RangeSet()
    r.add(1, 2)
    r.add(3, 4)
    assert repr(r) == "RangeSet([Range(1, 4)])"

    r = RangeSet()
    r.add(3, 4)
    r.add(1, 2)
    assert repr(r) == "RangeSet([Range(1, 4)])"
    
    
test_range_set() # TODO: move me to a separate file