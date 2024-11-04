def bubble_sort(ar):
    n = len(ar)
    for i in range(n):
        for j in range(i+1, n):
            if ar[i] > ar[j]:
                ar[i], ar[j] = ar[j], ar[i]
