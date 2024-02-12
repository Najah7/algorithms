def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)


data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

print(max_value_key(data) == "d")
