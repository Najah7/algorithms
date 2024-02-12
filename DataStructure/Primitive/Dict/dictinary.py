d = {
    "lable1": 1,
    "lable2": 2,
    "lable3": 3,
    "lable4": 4,
}


def filter_even(d):
    return {k: v for k, v in d.items() if v % 2 == 0}
