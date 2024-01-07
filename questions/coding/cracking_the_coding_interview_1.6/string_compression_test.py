from string_compression_solution import string_compression

def test_string_compression():
    assert string_compression('') == ''
    assert string_compression('abc') == 'abc'
    assert string_compression('aabcccccaaa') == 'a2b1c5a3'
