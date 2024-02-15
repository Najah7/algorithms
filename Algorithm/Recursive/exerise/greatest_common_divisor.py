# GCD: Greatest Common Divisor
def GCD(x, y):
    if int(x) != x or int(y) != y or x < 0 or y < 0:
        raise ValueError("a and b must be non-negative integers")

    if x < y:
        x, y = y, x  # to accept opposite order of arguments

    # for negative numbers
    if 0 < x:
        x = abs(x)
    if 0 < y:
        y = abs(y)

    if y == 0:
        return x
    return GCD(y, x % y)


print(GCD(48, 18) == 6)
