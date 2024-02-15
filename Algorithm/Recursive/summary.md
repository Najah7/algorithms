# Recursive

## Description
A way of solving problems by having a function call itself.

## Features
- performing the same operation multiple times with different input
- In every step we try to make the problem smaller
- Base condition is needed to stop the recursion, otherwise it will go into infinite loop

## Why Recursion
- Recursive thinking is really important in programming and it helps you break down big problems into smaller ones and easier to handle
- prominent usage for specific data structures like trees and graphs
- Recursive is used in many algorithms like quicksort, mergesort, binary search, etc...

## How Recursion Works
- using the stack to store the function calls
- when a function calls itself, the new call is added to the top of the stack

## Requirements of Recursion
- A method that calls itself
- A base condition to exit from infinite loop

## 3 step to write a recursive function
1. Recursive case - the flow
2. Base case - the stopping criterion
3. Unintentional case - the constraint

## Recursion vs Iteration
- in some cases, recursion is more elegant and easier to understand and implement
- in some cases, iteration is more efficient and faster(especially in space complexity)

## When to use/avoid Recursion
- Use
  - when the problem can be divided into smaller sub-problems
  - whe we are fine with the overhead that comes with recursion(both time and space)
  - when we need a quick working solution instead of an efficient one
  - when traversing a tree or graph
  - when you memoization or dynamic programming
- Avoid
    - when time and space complexity matters for us
    - when we need to optimize the solution
    - when we need speed and efficiency

## How to calculate the algorithm with Recursion
- single recursive call: a + M(n-a) -> O(n)
- multiple recursive call: a + M(n-a) + M(n-a) -> O(2^n) <- O(branch^depth)

👇 Example of Multiple recursive. ()
```
ex) def f(n): return f(n-1) + f(n-1)
ex) n = 4
each node call method 1 time, so count up all the nodes in the tree -> 15node (2^4 - 1) ≒ O(2^n)
        4
       / \
      3   3
     / \ / \
    2  2  2  2
  / \ /\  /\ /\
  1 1 1 1 1 1 1 1
```

## Example of Recursive
- Russian Dolls

## A joke of Infinite loop
- A programmer's wife tells him as he leaves the house: "While you're out, buy some milk". He never returns home and the universe runs out of milk.
