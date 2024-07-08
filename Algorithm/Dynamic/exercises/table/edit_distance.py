def edit_distance_table(s1, s2, table):
    # initialize the table
    for i in range(len(s1) + 1): 
        table.append([0] * (len(s2) + 1))

    # fill initial values (count of inserting characters)
    for i in range(len(s1) + 1):
        table[i][0] = i
    for j in range(len(s2) + 1):
        table[0][j] = j

    # calculate the minimum cost
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]: # when characters are same, no operation is needed. go to the next character
                table[i][j] = table[i - 1][j - 1]
            else:
                # you can understand this by seeing the edit graph
                # it's simple version of the edit graph (all cost is 1)
                insert = 1 + table[i][j - 1]
                delete = 1 + table[i - 1][j]
                replace = 1 + table[i - 1][j - 1]
                table[i][j] = min(insert, delete, replace)
    return table[len(s1)][len(s2)]

print(edit_distance_table("table", "tbrltt", []))  # 4