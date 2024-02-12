def reverse_dict(my_dict):
    return {value: key for key, value in my_dict.items()}


data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

print(reverse_dict(data) == {1: "a", 2: "b", 3: "c", 4: "d"})
