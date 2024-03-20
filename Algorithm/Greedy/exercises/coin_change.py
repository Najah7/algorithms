coins = (1, 5, 10, 25, 50, 100)


def coin_change(coins: tuple, amount: int) -> int:  # O(n)
    coins = sorted(coins, reverse=True)
    result = {}
    for coin in coins:  # O(n)
        result[coin] = amount // coin
        amount = amount % coin
    return result


print(coin_change(coins, 99))
