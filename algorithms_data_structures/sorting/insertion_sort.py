def insertion_sort(ar):
    n = len(ar)
    for i in range(1, n):
        idx = i
        for j in range(i-1, -1, -1):
            if ar[j] > ar[idx]:
                ar[idx], ar[j] = ar[j], ar[idx]
                idx = j
            else:
                break
