def power(base, exponent):
    # validations
    if not (0 <= base) and not int(base) != base:
        raise ValueError("base must be a non-negative integer")

    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)

    return base * power(base, exponent - 1)


print(power(2, 3) == 8)
