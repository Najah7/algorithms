def house_robber_memo(houses, current, memo):
    if current in memo:
        return memo[current]
    if current >= len(houses):
        return 0
    steal_current = houses[current] + house_robber_memo(houses, current + 2, memo)
    skip_current = house_robber_memo(houses, current + 1, memo)
    memo[current] = max(steal_current, skip_current)
    return memo[current]

print(house_robber_memo([6, 7, 1, 30, 8, 2, 4], 0, {}))  # 41