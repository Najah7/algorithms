# Array

## Features
- Array has a same type of elements
- all element are stored next to each other in memory
- each element is identified by an index (location)

## what is array for?
- store a collection of data (same type)
- access elements by index
- iterate over and perform same operation on each element (for loop)

## When to use/avoid array?
- when to use
    - To store multiple values of same type
    - Random access of elements
- when to avoid
    - To store multiple values of different types
    - Insertion/Deletion at beginning/middle of array
    - Dynamic size


## Type of Array
- One Dimensional Array
- Multi Dimensional Array
    - Two Dimensional Array
      - Matrix
      - val[row][col]
    - N Dimensional Array
    - all of N Dimensional Array are stored in one dimensional array in memory

## Array in Python
- Python does not have a built-in array data structure
- library for array
    - array.array
    - numpy.array
    - pandas.Series
- numpy.array is the most popular array library in Python

## data types for array.array

| Type code | C Type | Python Type | Minimum size in bytes |
| --- | --- | --- | --- |
| 'b' | signed char | int | 1 |
| 'B' | unsigned char | int | 1 |
| 'u' | Py_UNICODE | Unicode character | 2 |
| 'h' | signed short | int | 2 |
| 'H' | unsigned short | int | 2 |
| 'i' | signed int | int | 2 |
| 'I' | unsigned int | int | 2 |
| 'l' | signed long | int | 4 |
| 'L' | unsigned long | int | 4 |
| 'q' | signed long long | int | 8 |
| 'Q' | unsigned long long | int | 8 |
| 'f' | float | float | 4 |
| 'd' | double | float | 8 |
| 'c' | char | int | 1 |

## Operation & Complexity
- Create Empty Array
    - Time Complexity: O(1)
    - Space Complexity: O(1)
- Create
    - Time Complexity: O(n)
    - Space Complexity: O(n)
- Access(index): O(1) (index is known)
- Search/Traverse(value): O(n)
- Insert
    - Insert at the end: O(1) (end index is known)
        - Insert: O(1)
    - Insert at the beginning
        - Insert: O(1)
        - Shift: O(n)
    - Insert in the middle: O(n) (index is known)
        - Insert: O(1)
        - Shift: O(n/2) = O(n)
- Delete: O(n)
    - Delete at the end: O(1) (end index is known)
    - Delete at the beginning
        - Delete: O(1)
        - Shift: O(n)
    - Delete in the middle (index is known)
        - Delete: O(1)
        - Shift: O(n/2) = O(n)
    - Delete by value: O(n)

## methods of array.array

| Method | Description |
| --- | --- |
| append(value) | append value at the end |
| insert(index, value) | insert value at index |
| pop() | remove the last element |
| pop(index) | remove the element at index |
| remove(value) | remove the first element with value |
| index(value) | return the index of the first element with value |
| reverse() | reverse the array |
| extend(array) | append all elements of array |
| count(value) | return the number of occurrences of value |
| fromlist(list) | append all elements of list |
| tolist() | convert array to list |
| buffer_info() | return a tuple (address, length) of array |

## methods of numpy.array

| Method | Description |
| --- | --- |
| append(array, value, axis=None) | append value to array |
| insert(array, index, value, axis=None) | insert value at index |
| delete(array, index, axis=None) | delete value at index |
| unique(array) | return unique elements of array |
| where(condition, [x, y]) | return elements, either x or y, depending on condition |
| searchsorted(array, value) | return the index where the value would be inserted |
| sort(array) | sort the array |
| argsort(array) | return the indices that would sort the array |
| argmax(array) | return the index of the maximum value in the array |
| argmin(array) | return the index of the minimum value in the array |
| nonzero(array) | return the indices of the elements that are non-zero |
| fromstring(string, dtype=float, count=-1, sep='') | return a new 1-D array initialized from raw binary or text data in a string |
| tostring(array) | return a string representing the data in the array |
