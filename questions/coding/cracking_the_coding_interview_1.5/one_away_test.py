from one_away_solution import one_away

def test_one_away_no_diff():
    assert one_away('abc', 'abc') == True

def test_one_away_missing_chars():
    assert one_away('ab', 'abc') == True
    assert one_away('a', 'abc') == False

def test_one_away_mismatch_chars():
    assert one_away('abd', 'abc') == True
    assert one_away('abc', 'xyz') == False
