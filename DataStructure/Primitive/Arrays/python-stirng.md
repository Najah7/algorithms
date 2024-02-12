# Python String
- A string is a sequence of characters.

## How to use string?
- Create a string: `str()`, `''`, `""`, `''' '''`, `""" """` (O(1))
- Access characters: `str[index]` (minus index is allowed) (O(1))
- Update a string: `str[index] = new_value` (not allowed) (O(1))
- Delete a string: `del str[index]` (not allowed) (O(n))
- Slice a string: `str[start:end:step]` (O(k))
- Search for a character: `target in str` (O(n))
- Iterate over a string: `for char in str:` (O(n))

## Operator for string
- `+`: concatenate two strings (O(k))
- `*`: repeat a string (O(nk))
- `in`: check if a character is in a string (O(n))
- `not in`: check if a character is not in a string (O(n))

## Methods of string (Common)
- `str.upper()`: O(n)
- `str.lower()`: O(n)
- `str.capitalize()`: O(n)
- `str.title()`: O(n)
- `str.count(substring, start, end)`: O(n)
- `str.find(substring, start, end)`: O(n)
- `str.index(substring, start, end)`: O(n)
- `str.join(iterable)`: O(n)
- `str.strip(characters)`: O(n)
- `str.strip()`: O(n)
