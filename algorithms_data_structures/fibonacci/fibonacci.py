def fibonacci(n):
    if n < 0:
        return -1
    if n <= 1:
        return n
    prev1, prev2 = 1, 0
    for _ in range(1, n):
        new_fib = prev1 + prev2
        prev2 = prev1
        prev1 = new_fib
    
    return new_fib

def fibonacci_recursive(n):
    if n < 0:
        return -1
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
