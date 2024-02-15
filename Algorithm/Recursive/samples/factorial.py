def factorial(n):
    if n < 0 and not isinstance(n, int):
        raise ValueError("n must be a non-negative integer")
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5) == 120)
