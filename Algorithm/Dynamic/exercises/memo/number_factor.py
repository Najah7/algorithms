def number_factor_memo(n, memo):
    if n in memo:
        return memo[n]
    if n in (0, 1, 2):
        return 1
    if n == 3:
        return 2
    sub1 = number_factor_memo(n - 1, memo)
    sub3 = number_factor_memo(n - 3, memo)
    sub4 = number_factor_memo(n - 4, memo)
    memo[n] = sub1 + sub3 + sub4
    return memo[n]

print(number_factor_memo(5, {}))  # 6