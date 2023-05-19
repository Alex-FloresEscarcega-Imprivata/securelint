from Range import Range


def test_range():
    a = Range(2, 4)
    b = Range(1, 3)
    assert a.overlaps(b) == True

    a = Range(1, 3)
    b = Range(2, 4)
    assert a.overlaps(b) == True

    a = Range(1, 4)
    b = Range(2, 3)
    assert a.overlaps(b) == True

    a = Range(2, 3)
    b = Range(1, 4)
    assert a.overlaps(b) == True

    a = Range(1, 2)
    b = Range(4, 5)
    assert a.overlaps(b) == False

    a = Range(1, 2)
    b = Range(3, 4)
    assert a.touches(b) == True

    a = Range(3, 4)
    b = Range(1, 2)
    assert a.touches(b) == True

    a = Range(1, 2)
    b = Range(4, 5)
    assert a.touches(b) == False

    a = Range(4, 5)
    b = Range(1, 2)
    assert a.touches(b) == False
    
    
test_range()  # TODO: move me to a separate file