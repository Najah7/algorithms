# Queue

## Features
- FIFO(First In First Out)

## Example of Queue
- sale system of restaurant
- Printer 
- Cell Center System

## When to use
- Utilize first data coming first, while others wait for their turn.


## Operation
- Create
- enqueue
- dequeue
- peek
- delete
- isEmpty
- isFull

## Points
- List no capacity limit
    - Enqueue: O(n) <- append sometimes reallocatee
    - Dequeue: O(n) <- shift all items after removed item
- Cricular Queue
    - Creation(Space Complexity): O(n)
- Linked List Queue
    - all of operation: O(1)

## Build-in Queue
- Collection Module
    - methods
        - dequeue
        - append
        - popleft
        - clear
- Queue Module
    - FIFO queue
    - LIFO queue
    - Priority queue
    - methods
        - qsize()
        - empty()
        - full()
        - put()
        - get()
        - task_done()
        - join
- Multiprocessing Module
