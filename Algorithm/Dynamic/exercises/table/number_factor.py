def number_factor_table(n):
    table = [1, 1, 1, 2]
    for i in range(4, n + 1):
        sub1 = table[i - 1]
        sub3 = table[i - 3]
        sub4 = table[i - 4]
        table.append(sub1 + sub3 + sub4)
    return table[n]

print(number_factor_table(5))  # 6