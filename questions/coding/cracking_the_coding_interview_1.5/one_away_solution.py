def one_away(s1, s2):
    s1_idx, s2_idx = 0, 0
    already_editted = False
    while s1_idx < len(s1) and s2_idx < len(s2):
        if s1[s1_idx] != s2[s2_idx]:
            if already_editted:
                return False
            already_editted = True
            if s1_idx + 1 < len(s1) and s1[s1_idx + 1] == s2[s2_idx]:
                s1_idx += 1
            elif s2_idx + 1 < len(s2) and s1[s1_idx] == s2[s2_idx + 1]:
                s2_idx += 2
        s1_idx += 1
        s2_idx += 1
    return abs(len(s1) - len(s2)) < 2
