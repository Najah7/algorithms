def capitalize_first(arr):
    if len(arr) == 0:
        return []

    return [arr[0].capitalize()] + capitalize_first(arr[1:])


words = ["apple", "banana", "cherry"]
print(capitalize_first(words) == ["Apple", "Banana", "Cherry"])
