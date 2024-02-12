def insert_first(t, e):
    return (e,) + t


t = (1, 2, 3)
new_elem = 0
print(insert_first(t, new_elem) == (0, 1, 2, 3))
