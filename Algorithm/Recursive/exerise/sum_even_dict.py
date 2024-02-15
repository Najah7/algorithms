def nested_even_sum(obj, even_sum=0):
    for key in obj:
        if isinstance(obj[key], dict):
            even_sum += nested_even_sum(obj[key])
        elif isinstance(obj[key], int) and obj[key] % 2 == 0:
            even_sum += obj[key]

    return even_sum


sample_dict = {
    "a": 2,
    "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
    "c": {"c": {"c": 2}, "cc": "ball", "ccc": 5},
    "d": 1,
    "e": {"e": {"e": 2}, "ee": "car"},
}

print(nested_even_sum(sample_dict) == 10)
