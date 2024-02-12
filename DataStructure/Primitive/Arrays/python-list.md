# Python List
- A list is a data structure that holds an ordered collection of items.
- Each item is called an element, and elements can be of different data types.

## How to use list?
- Create a list: `list()`, `[]` (O(1))
- Access elements: `list[index]` (minus index is allowed) (O(1))
- Update a list: `list[index] = new_value` (O(1))
- Delete a list: `del list[index]` (in some cases, you can use slice, remove, pop, clear methods) (O(n))
- Slice a list: `list[start:end:step]` (O(k))
- Search for an element: `target in list` (O(n))
- Traverse a list: `for item in list:` (O(n))

## Operator for list
- `+`: concatenate two lists (O(k))
- `*`: repeat a list (O(nk))
- `in`: check if an element is in a list (O(n))
- `not in`: check if an element is not in a list (O(n))


## Methods of list
- `list.append(item)`: O(1)
- `list.insert(index, item)`: O(n)
- `list.pop()`: O(1)
- `list.pop(index)`: O(n)
- `list.remove(item)`: O(n)
- `list.index(item)`: O(n)
- `list.reverse()`: O(n)
- `list.extend(list)`: O(n)
- `list.sort() -> None`: O(nlogn) (Timsort)
- `list.count(item)`: O(n)
- `list.copy()`: O(n)
- `list.clear()`: O(1)

## functions related to list
- `len(list)`: O(1) (List has a variable to store its length)
- `max(list)`: O(n)
- `min(list)`: O(n)
- `sum(list)`: O(n)
- `sorted(list) -> list`: O(nlogn) (Timsort)
- `reversed(list)`: O(n)
- `enumerate(list)`: O(n)
- `zip(list1, list2)`: O(n)
- `all(list)`: O(n) (return True if all elements are True. you can use it to validate a list)
- `copy.deepcopy(list)`: O(n)  (you can use list[:] instead)
- `random.choice(list)`: O(1)
- `random.shuffle(list)`: O(n)


## List Comprehension
- List comprehension is an elegant way to define and create lists based on existing lists.

```python
# Syntax
new_list = [ expression for item in list] 
# item is used in an expression
```

## Conditional List Comprehension
- List comprehension can include an optional condition clause to filter elements.
- We should use function instead of list comprehension if the condition is complex.

```python
# Syntax
new_list = [ expression for item in list if conditional ]
# item is used in an expression and a condition
```
