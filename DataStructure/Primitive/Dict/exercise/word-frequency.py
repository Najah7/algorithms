def count_word_frequency(words):
    frequency_count = {}
    for word in words:
        frequency_count[word] = frequency_count.get(word, 0) + 1
    return frequency_count


data = [
    "apple",
    "banana",
    "peach",
    "apple",
    "banana",
]

print(count_word_frequency(data))
