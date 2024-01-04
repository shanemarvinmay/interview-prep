from collections import Counter

def check_permutation(s1, s2):
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)
    
    for ltr in s1_counter:
        if ltr not in s2_counter or s1_counter[ltr] != s2_counter[ltr]:
            return False
    
    for ltr in s2_counter:
        if ltr not in s1_counter:
            return False
    
    return True

print(check_permutation('abc', 'cab'))