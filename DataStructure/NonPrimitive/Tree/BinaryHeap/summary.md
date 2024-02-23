# Binary Heap

## Description
A Binary Heap is a Binary Tree with the following properties:
- A Binary Heap is either Min Heap or Max Heap.
    - Min Heap: The key at the root must be minimum among all keys present in the Binary Heap. the value of each node is less than or equal to the value of its children.
    - Max Heap: The key at the root must be maximum among all keys present in the Binary Heap. the value of each node is greater than or equal to the value of its children.
- It's a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). and it makes them suitable to be stored in an array.

## Why Binary Heap
- Find the minimum or maximum element in O(1) time.
- inserting additional numbers does not take more than O(log n) time.

## How to implement Binary Heap
- Using Array: this is better for binary heap.
- Using Tree

## Practical Use
- Prim's Algorithm
- Heap Sort
- Priority Queue

## Common Operations of Binary Heap
- Creation
- Peek
- Extract Min/Max
- Size of Heap
- Insertion
- Deletion
