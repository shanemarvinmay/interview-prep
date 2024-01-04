from is_unique_solution import is_unique, is_unique_follow_up

def test_is_unique_true():
    assert is_unique('abc') == True
    assert is_unique_follow_up('abc') == True

def test_is_unique_false():
    assert is_unique('abca') == False
    assert is_unique_follow_up('abca') == False