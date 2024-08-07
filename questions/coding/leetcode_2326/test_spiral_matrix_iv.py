from questions.coding.leetcode_2326.spiral_matrix_iv import ListNode, Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.fixture()
def linked_list():
    values = [0,2,6,8,1,7,9,4,2,5,5,0]
    head = ListNode(3)
    itr = head
    for i in range(len(values)):
        itr.next = ListNode(values[i])
        itr = itr.next
    return head

@pytest.mark.parametrize('m, n, head, expected', [
    (3, 5, 'linked_list', [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]),
])
def test_spiralMatrix(m, n, head, expected, sol, request):
    head = request.getfixturevalue(head)
    
    got = sol.spiralMatrix(m, n, head)

    assert got == expected