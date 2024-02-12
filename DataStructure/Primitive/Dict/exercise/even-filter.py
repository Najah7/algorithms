def even_filter(my_dict, condition):
    return {k: v for k, v in my_dict.items() if v % 2 == 0}


data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

print(even_filter(data, 2) == {"b": 2, "d": 4})
