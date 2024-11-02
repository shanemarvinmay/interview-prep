def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    prev1, prev2, new_fib = 1, 0, -1
    for _ in range(3, n + 1):
        new_fib = prev1 + prev2
        prev2 = prev1
        prev1 = new_fib
    
    return new_fib
