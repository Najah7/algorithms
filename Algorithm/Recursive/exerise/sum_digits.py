def sum_digits(n):
    # validations
    if not (0 <= n) and not int(n) != n:
        raise ValueError("n must be a non-negative integer")
    if n < 10:
        return n  # base case
    return n % 10 + sum_digits(n // 10)


print(sum_digits(123) == 6)
