from partition_labels_solution import Solution

import pytest

@pytest.mark.parametrize('s, expected', [
	('ababcbacadefegdehijhklij', [9,7,8]),
	('eccbbbbdec', [10])
])
def test_partition_labels(s, expected):
	solution = Solution()

	got = solution.partitionLabels(s)

	assert got == expected
