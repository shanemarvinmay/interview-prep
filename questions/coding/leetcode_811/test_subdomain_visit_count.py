from questions.coding.leetcode_811.subdomain_visit_count import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()
'''
Constraints:
1 <= cpdomain.length <= 100
1 <= cpdomain[i].length <= 100
cpdomain[i] follows either the "repi d1i.d2i.d3i" format or the "repi d1i.d2i" format.
repi is an integer in the range [1, 104].
d1i, d2i, and d3i consist of lowercase English letters.
'''
@pytest.mark.parametrize('cpdomains, expected', [
    (["9001 discuss.leetcode.com"], ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]),
    (["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"], ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]),
])
def test_subdomainVisits(cpdomains, expected, sol):
    got = sol.subdomainVisits(cpdomains)
    
    assert len(got) == len(expected)

    for i in got:
        assert i in expected
