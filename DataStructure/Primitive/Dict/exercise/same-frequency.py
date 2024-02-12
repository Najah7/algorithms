def same_frequency(l1, l2):
    d = {}
    for value in [*l1, *l2]:
        d[value] = d.get(value, 0) + 1
    return d


data = [1, 2, 3, 4, 5]
data2 = [5, 4, 3, 2, 1]

print(same_frequency(data, data2) == {1: 2, 2: 2, 3: 2, 4: 2, 5: 2})
