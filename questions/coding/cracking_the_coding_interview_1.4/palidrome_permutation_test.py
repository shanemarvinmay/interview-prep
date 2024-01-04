from palidrome_permutation_solution import palidrome_permutation

def test_palidrome_permutation_true():
    assert palidrome_permutation(' Tact Coa  ') == True
    assert palidrome_permutation('Tact Ca') == True

def test_palidrome_permutation_false():
    assert palidrome_permutation(' Tat Co  ') == False