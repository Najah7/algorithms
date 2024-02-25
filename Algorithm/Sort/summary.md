# Sorting

## Description
By definition sorting refers to arranging data in a particular format: either ascending or descending order.

## Evaluation of Sorting
- **Space used**
    - **In-place**: An in-place sorting algorithm uses constant extra space for producing the output (modifies the given array only).
    - **Out-of-place**: An out-of-place sorting algorithm does not use the extra space for producing the output (creates a new array for the output).
- **Stability**:
    - **Stable**: A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted.
    - **Unstable**: A sorting algorithm is said to be unstable if two objects with equal keys may not appear in the same order in sorted output as they appear in the input array to be sorted. 

## Which one to select?
- Stability
- Space Efficiency
- Time Efficiency

## Terminology of Sorting
**Increasing Order**: A sequence of elements is said to be in increasing order if the element at the next position is greater than or equal to the element at the current position. ex: 1, 2, 3, 4, 5
**Decreasing Order**: A sequence of elements is said to be in decreasing order if the element at the next position is less than or equal to the element at the current position. ex: 5, 4, 3, 2, 1
**Non Increasing Order**: A sequence of elements is said to be in non-increasing order if the element at the next position is less than or equal to the element at the current position. ex: 5, 4, 3, 3, 2, 1
**Non Decreasing Order**: A sequence of elements is said to be in non-decreasing order if the element at the next position is greater than or equal to the element at the current position. ex: 1, 2, 3, 3, 4, 5

## Types of Sorting
- **Bubble Sort**: It is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
    - when to use
        - When the input is almost sorted
        - Space is a concern
        - Easy to implement
    - when to avoid
        - Average time complexity is poor
- **Selection Sort**: It is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part and putting it at the beginning.
    - when to use
        - when we have insufficient memory
        - easy to implement
    - when to avoid
        - When  time is a concern
- **Insertion Sort**: It is a simple sorting algorithm that works by building a sorted array one element at a time.
    - when to use
        - When we have insufficient memory
        - easy to implement
        - when we have continuous inflow of number and we want to keep them sorted
    - when to avoid
        - When time is a concern
- **Bucket Sort**: It is a sorting algorithm that works by distributing the elements into a number of buckets and then each bucket is sorted individually.
    - when to use
        - When the input is uniformly distributed over a range (you can use normalizing function to make it uniform)
    - when to avoid
        - When space is a concern
- **Merge Sort**: It is a divide and conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
    - when to use
        - When you need stable sort
        - When average time complexity is O(N log N) <- good time complexity
    - when to avoid
        - When space is a concern
- **Quick Sort**: It is a divide and conquer algorithm that picks an element as pivot and partitions the given array around the picked pivot.
    - when to use
        - When average time complexity is O(N log N) <- good time complexity
    - when to avoid
        - When you need stable sort
- **Heap Sort**: It is a comparison-based sorting algorithm that uses a binary heap data structure.
    - when to use
        - When space is a concern <- O(1) space complexity
    - when to avoid
        - When average time complexity is poor
