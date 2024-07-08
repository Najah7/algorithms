def zero_one_knapsack_with_table(profits, weights, capacity):
    # for padding
    profits = [0] + profits
    weights = [0] + weights

    # initialize the table with zeros. x: profits, y: capacity
    table = [[0] * (capacity + 1) for _ in range(len(profits))]

    # calculate the maximum profit
    for i in range(1, len(profits)):
        # i: profit index, j: capacity
        for j in range(1, capacity + 1):
            if weights[i] > j:
                table[i][j] = table[i - 1][j]
            else:
                # j-weight[i] is the key point <- get max profit when it is the (capacity - current) weight
                take = profits[i] + table[i - 1][j - weights[i]]
                leave = table[i - 1][j]
                table[i][j] = max(take, leave)

    return table[len(profits) - 1][capacity]

profits = [31, 26, 17, 72]
weights = [3, 1, 2, 5]
capacity = 7
print(zero_one_knapsack_with_table(profits, weights, capacity))  # 98