# Dictionary

## Description
- key-value pairs

## Features
- unordered
- changeable
- indexed

## Dictionary in Memory
- dictionary is stored in memory as a hash table
- hash table is an array of linked lists
- first element of the linked list is the hashed value of the key

### flow
1. hash(key) -> index
2. hash table[index] <- linked list
3. when collision occurs, linked list is used

## Creating a Dictionary in Python
```python
# use constructor
my_dict = dict() # O(1)
my_dict = dict(key=value, key2=value2...) # O(n)

# use curly braces
my_dict = {} # O(1)
my_dict = {key: value, key2: value2...} # O(n)
```

## methods
- creation
    - fromkeys(keys[], default_value=None)
- find
    - get(key, default_value=None)
    - pop(key): return the value and remove the key-value pair
    - popitem(): LIFO(after Python 3.7, dict has order)
- update
    - update(dict): merge two dictionaries
    - setdefault(key, default_value=None)
- delete
    - del
    - clear()
- iterable
    - keys() -> key[]
    - values() -> value[]
    - items() -> key, value
- copy
    - copy(): shallow copy(copy of the first level, and reference to the deeper levels)

## operations
- len(dict)
- in -> key in dict
- all(dict): return True if all keys are True
- any(dict): return True if any keys is True
- sorted(dict): return sorted keys

## Dictionary Comprehension
```python
new_dict = {key: value for item in iterable}
new_dict = {key: value for key, value in iterable}
new_dict = {key: value for value in iterable if condition}
```

## Deep Copy
- deepcopy() in copy module
- `new_dict = dict(old_dict)`

## Examples in this lecture
- baggage counter
    - array: number and baggage
    - dictionary: customer's name and baggage



## Others
- We can use tuple's array instead of dictionary when using numeric keys.




