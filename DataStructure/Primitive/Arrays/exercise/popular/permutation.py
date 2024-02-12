def permutation(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    arr1.sort()
    arr2.sort()
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


print("Test for permutation: input=[1, 2, 3,], [2, 1, 3], output=True")
print(permutation([1, 2, 3], [2, 1, 3]) == True)
print("Test for permutation: input=[a, b, c], [b, a, c], output=True")
print(permutation(["a", "b", "c"], ["b", "a", "c"]) == True)
