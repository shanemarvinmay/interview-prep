def selection_sort(ar):
    n = len(ar)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if ar[j] < ar[min_idx]:
                min_idx = j
        ar[min_idx], ar[i] = ar[i], ar[min_idx]
