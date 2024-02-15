def stringify_nums(obj):
    for key in obj:
        # NOTE: isinstance(True, int) -> True, because bool is a subclass of int
        if type(obj[key]) == int:
            obj[key] = str(obj[key])
        if isinstance(obj[key], dict):
            obj[key] = stringify_nums(obj[key])
    return obj


sample_dict = {
    "num": 1,
    "test": [],
    "data": {"val": 4, "info": {"isRight": True, "random": 66}},
}

expected = {
    "num": "1",
    "test": [],
    "data": {"val": "4", "info": {"isRight": True, "random": "66"}},
}
print(stringify_nums(sample_dict) == expected)
