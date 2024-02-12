# Tuple

# Features
- ordered
- unchangeable
- indexed

## Tuple in Memory
- tuple is stored in memory as an array

## Creating a Tuple in Python
```python
# use constructor
my_tuple = tuple() # O(1)
my_tuple = tuple(iterable) # O(n) (O(1) when using existed iterable)

# use parentheses
my_tuple = (item1, item2...) # O(n)
```

## methods
- count(item) -> int
- index(item) -> int

## operations
- len(tuple)
- in -> item in tuple
- not in -> item not in tuple
- + -> concatenate two tuples
- * -> repeat a tuple
