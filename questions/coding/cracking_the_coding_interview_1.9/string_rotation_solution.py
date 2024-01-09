def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_idx, s2_idx = 0, 0
    # Finding postfix start
    while s1_idx < len(s1) and s1[s1_idx] != s2[s2_idx]:
        s1_idx += 1
    postfix_start = s1_idx

    # Checking postfix
    while s1_idx < len(s1) and s2_idx < len(s2) - postfix_start:
        if s1[s1_idx] != s2[s2_idx]:
            return False
        s1_idx += 1
        s2_idx += 1

    # Checking prefix
    s1_idx = 0
    s2_idx = len(s2) - postfix_start
    while s2_idx < len(s2):
        if s1[s1_idx] != s2[s2_idx]:
            return False
        s1_idx += 1
        s2_idx += 1
    
    return True
    