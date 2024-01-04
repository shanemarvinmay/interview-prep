from check_permutation_solution import check_permutation

def test_check_permutation_true():
    assert check_permutation('abc', 'cab') == True

def test_check_permutation_false():
    # Different letters
    assert check_permutation('abcd', 'cabe') == False
    assert check_permutation('abc', 'cabe') == False
    # Different frequency of letters
    assert check_permutation('abcc', 'caba') == False