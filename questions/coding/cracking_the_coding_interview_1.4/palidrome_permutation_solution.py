def palidrome_permutation(s):
    s = s.lower()
    unique_ltrs = set()
    for ltr in s:
        if ltr.isalpha() == False:
            continue
        if ltr in unique_ltrs:
            unique_ltrs.remove(ltr)
        else:
            unique_ltrs.add(ltr)
    print(unique_ltrs)
    return len(unique_ltrs) < 2