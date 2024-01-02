# Big O
- language and metric used to describe the efficiency of algorithms
- you can use it to compare two algorithms and see which one is more efficient


# Complexity
- complexity provides a way to describe the relationship between the input to a function and the time or space that it takes to run
- Time Complexity
    - A way of showing how the runtime of function  increases as the size of the input increases
    - number of operations
- Space Complexity
    - A way of showing how the memory usage of function increases as the size of the input increases
    - amount of memory
- Expressions
    - Big O Notation
    - ex) O(1), O(n), O(n^2), O(log n), O(n log n), O(2^n), O(n!)

# Cases of Complexity
- Best Case
        - Best Case is the case where the algorithm performs the best
        - expression: Ω (Omega)
    - Average Case
        - Average Case is the case where the algorithm performs the average
        - expression: θ (Theta)
    - Worst Case
        - Worst Case is the case where the algorithm performs the worst
        - most popular way to evaluate the performance of an algorithm
        - expression: O (Big O)

# Big O Notation
- Big O Notation is a way of expressing the relationship between the input to a function and the time or space that it takes to run
- It tells you the worst case scenario
- the table below shows the most common Big O Notation. (ordered by efficiency. from the most efficient to the least efficient)
- Drop the constants
    - when you have a constant in front of the Big O Notation, you can drop it
    - ex) O(2n) = O(n), O(1/2n) = O(n)
- Non Dominate Terms
    - when you have multiple terms in the Big O Notation, you can drop the non dominate terms
    - ex) O(n^2 + n) = O(n^2), O(n^2 + n + 1) = O(n^2)


| Big O Notation | Name | Description |
| --- | --- | --- |
| O(1) | Constant | The runtime is not dependent on the size of the input |
| O(n) | Linear | The runtime is directly proportional to the size of the input |
| O(n^2) | Quadratic | The runtime is proportional to the square of the size of the input |
| O(log n) | Logarithmic | The runtime is proportional to the logarithm of the size of the input |
| O(n log n) | Log Linear | The runtime is proportional to the product of the logarithm of the size of the input and the size of the input |
| O(2^n) | Exponential | The runtime is proportional to 2 raised to the power of the size of the input |
| O(n!) | Factorial | The runtime is proportional to the factorial of the size of the input |
sss

# Add v.s Multiply
- when you have multiple terms in the Big O Notation, you can add them if they are in different loops, but you can multiply them if they are in the same loop
- O(n + m) ≒ O(n) (Do not say O(n), should say O(n + m))
```python
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4]

for i in a:
    print(i)

for j in b:
    print(j)
```
- O(n * m) ≒ O(n^2) (Do not say O(n^2), should say O(n * m))
```python
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4]

for i in a:
    for j in b:
        print(i, j)
```


# Points when thinking about Algorithms
- Algorithms work base on context
    - Type of input
    - Type of Algorithm
    - Spec of the machine
    - Spec of the language ...etc
- Algorithms have different cases
    - Best Case
    - Average Case
    - Worst Case
- Algorithms have different metrics
    - Time Complexity
    - Space Complexity

# Points to recognize Big O
| steps | description | Big O |
| --- | --- | --- |
| 1 | Any assignment and if statements that are excuted once regardless of the size of problem | O(1) |
| 2 | A simple for loop from 0 to n (without no iteral loops) | O(n) |
| 3 | A for loop that iterates over half of the input | O(n) |
| 4 | A nested loop of the same type takes | O(n^2) |
| 5 | when dealing with multiple statements, just add them up | depends |
