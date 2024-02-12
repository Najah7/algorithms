def commons(tuple1, tuple2):
    return tuple((set(tuple1) & set(tuple2)))


data = (1, 2, 3, 4, 5)
data2 = (5, 1)

print(commons(data, data2) == (1, 5))
