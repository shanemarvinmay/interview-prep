from collections import Counter

def check_permutation(s1, s2):
    s1_counter = Counter(s1)
    
    for ltr in s2:
        if ltr not in s1_counter or s1_counter[ltr] == 0:
            return False
        s1_counter[ltr] -= 1
    
    for ltr in s1_counter:
        if s1_counter[ltr]:
            return False
    
    return True

print(check_permutation('abc', 'cab'))