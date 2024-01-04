from urlify_solution import urlify

def test_urlify():
    assert urlify(' a   b  c   ') == 'a%20b%20c'
    assert urlify('') == ''