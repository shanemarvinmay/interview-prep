def is_unique(s):
    unique_chars = set(s)
    return len(s) == len(unique_chars)

def is_unique_follow_up(s):
    # Sort
    s = ''.join(sorted(s))
    # Make sure no neighbors are the same
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


print(is_unique_follow_up('3763'))
print(is_unique_follow_up('376'))