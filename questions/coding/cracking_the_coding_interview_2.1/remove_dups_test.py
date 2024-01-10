from remove_dups_solution import list_to_linked_list, remove_dups

def assert_linked_list_are_equal(l1, l2):
    p1, p2 = l1, l2
    while p1 and p2:
        print(f'p1:{p1.value}\tp2:{p2.value}')
        assert p1.value == p2.value
        p1 = p1.next
        p2 = p2.next
    if p1:
        print(f'p1:{p1.value}')
    if p2:
        print(f'p2:{p2.value}')
    assert p1 is None and p2 is None


def test_remove_dups_head_and_mid_need_removal():
    head_and_mid_need_removal = list_to_linked_list([0, 1, 0, 1, 0])
    expected = list_to_linked_list([1, 0])

    assert_linked_list_are_equal(remove_dups(head_and_mid_need_removal), expected)


def test_remove_dups_mid_and_end_need_removal():
    mid_and_end_need_removal = list_to_linked_list([0, 0, 0, 0])
    assert_linked_list_are_equal(remove_dups(mid_and_end_need_removal), list_to_linked_list([0]))