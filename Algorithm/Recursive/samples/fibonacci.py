def fibonacci(n):
    if n < 0 and not int(n) != n:
        raise ValueError("n must be a non-negative integer")

    if n <= 1:  # fin(0) = 0, fin(1) = 1
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(4) == 3)
