def binary_search(ar, target):
    left = 0
    right = len(ar) - 1
    while left < right:
        mid = (left + right) // 2
        if ar[mid] == target:
            return mid
        elif ar[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    return -1
