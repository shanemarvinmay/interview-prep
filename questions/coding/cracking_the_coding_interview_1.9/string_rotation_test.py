from string_rotation_solution import string_rotation

def test_string_rotation_true():
    s1 = 'whatwhat'
    s2 = 'hatwhatw'

    assert string_rotation(s1, s2) == True

def test_string_rotation_false():
    s1 = 'whatwhata'
    s2 = 'hatwhatwa'

    assert string_rotation(s1, s2) == False