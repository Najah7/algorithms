def upper_words(arr):
    if len(arr) == 0: return []
    return [arr[0].upper()] + upper_words(arr[1:])

words = ['apple', 'banana', 'cherry']
print(upper_words(words) == ['APPLE', 'BANANA', 'CHERRY'])
