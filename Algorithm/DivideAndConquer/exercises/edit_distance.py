"""
convert S1 to S2 with minimum cost

Operations:
    1. Insert
    2. Delete
    3. Replace

NOTE:

    Edit Distance/Levenshtein Distance

    Edit Graph help you understand this problem better
    - insert: x + 1
    - delete: y + 1
    - replace: z + 1 (z costs 0)

    notes:
    - the cost must be bigger than the difference between the two strings
    - the tips to make the cost smaller: should replace instead of deleting and inserting


"""

# NOTE: this problem is that all operations have the same cost (actually, delete and insert have 2x cost)

def convert_string(s1, s2, i, j):
    # we need to delete all the remaining characters in s1/s2
    if i == len(s1):
        return len(s2) - j
    if j == len(s2):
        return len(s1) - i
    # go to the next character
    if s1[i] == s2[j]:
        return convert_string(s1, s2, i + 1, j + 1)
    insert = 1 + convert_string(s1, s2, i, j + 1)
    delete = 1 + convert_string(s1, s2, i + 1, j)
    replace = 1 + convert_string(s1, s2, i + 1, j + 1)
    return min(insert, delete, replace)


print(convert_string("table", "tbrle", 0, 0))  # 2
