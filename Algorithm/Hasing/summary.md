# Hashing

## Description
Hashing is a method of sorting and indexing data.
The idea behind hashing is to allow large amounts of data to be indexed using keys commonly created by formula.

## Why Hashing
- It is tme efficient in case of searching.

## Pros and COns of Hashing
- Pros
    - On an average, hash table operations take O(1) time to search, insert, delete.
- Cons
    - In worst case, hash table operations take O(n) time to search, insert, delete.

## Terminology of Hashing
- **Hash Function**: A function that converts a given big input key to a small practical integer value. The mapped integer value is used as an index in hash table.
- **Key**: A unique identifier for a value in a collection. most of the time it is input data by a user.
- **Hash Value**: The result of applying a hash function to a key.
- **Hash Table**: Data structure that implements an associative array abstract data type, a structure that can map keys to values.
- **Collision**: When two different keys hash to the same index in the array, it is called a collision.
- **Load Factor**: The load factor is a measure that decides when to increase the size of the hash table. It is the ratio of the number of items in the hash table to the size of the hash table.
- **Rehashing**: The process of increasing the size of the hash table when the load factor increases beyond a particular threshold.

## Collision Resolution
- **Direct Chaining**: In chaining, each slot of the array contains a link to a list of elements that hash to the slot.
- **Open Addressing**: In open addressing, all elements are stored in the hash table itself. Each table entry contains either a record or NIL.
    - **Linear Probing**: In linear probing, the interval between the keys is fixed.
    - **Quadratic Probing**: In quadratic probing, the interval between the keys is increased by adding the successive outputs of a quadratic function to the starting value given by the original hash function. (quadratic function: f(i) = i^2)
    - **Double Hashing**: In double hashing, the interval between the keys is fixed for each record but is computed by another hash function.

## Properties of Good Hash Function
- It distributes hash value uniformly across the table.
- It has to use all the input data.f

## When hash table is full (Load Factor)
- If the hash table is full, then the hash table is rehashed to double its size.

## Pros and Cons of Collision Techniques
- **Direct Chaining**
    - Pros: never get full
    - Cons: huge linked list causes performance issue.
    - When: do deletion frequently.
- **Open Addressing**
    - Pros: easy to implement
    - Cons: when table is full, creation of new table affects performance.
    - When: know the size of data.

## Practical Use
- Password Verification
- File System: File path is mapped to physical location on disk.
