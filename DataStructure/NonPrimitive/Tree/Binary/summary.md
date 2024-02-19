# Binary Tree

## Description
Binary Tree is a data structure in which each node has at most two children, which are referred to as the left child and the right child.
Binary Tree is a family of data structure
- Binary Search Tree
- AVL Tree
- Red-black Tree
- Trie

## Why binary tree
- Binary tree is pre-requirement for mode advanced tree like AVL, Red-black, Trie ...etc
- can be solved many problems using binary tree
    - Huffman coding program
    - heap priority problem
    - expression parsing problem

## Types of Binary Tree
- Full Binary Tree: A Binary Tree is full if every node has 0 or 2 children
- Perfect Binary Tree: A Binary tree is perfect if all internal nodes have two children and all leaves are at the same level
- Complete Binary Tree: A Binary Tree is complete Binary Tree if all levels are completely filled except possibly the last level and the last level has all keys as left as possible
- Balanced Binary Tree: A Binary Tree is balanced if the height of the tree is O(Log n) where n is the number of nodes(most of the time, this has same height of all the leaf nodes)
- Degenerate (or pathological) Tree: A Tree where every internal node has one child. Such trees are performance-wise same as linked list.

## How to implement Binary Tree
- Using linked list: data and links to its children
- Using array (Python list): 
    - root node at index 0
    - left child of node at index i is at (2*h when first index is 1, 2*h + 1 when first index is 0)
    - right child of node at index i is at (2*h + 1 when first index is 1, 2*h + 2 when first index is 0)

Summary
- Python list is easy to implement but not space efficient
- Linked list is space efficient but not easy to implement


| Operation | Python list(time) | Python list(space) | Linked List(time) | Linked List(space) |
|-------------|-------------------|---------------------|-------------------|---------------------|
| creation | O(1) | O(n) | O(1) | O(1) |
| insertion | O(1) | O(1) | O(n) | O(n) |
| deletion | O(n) | O(1) | O(n) | O(n) |
| search | O(n) | O(1) | O(n) | O(n) |
| traversal | O(n) | O(1) | O(n) | O(n) |
| clear | O(1) | O(1) | O(1) | O(1) |

## Traverse Binary Tree
- Depth First Traversal
    - Inorder: left, root, right
    - Preorder: root, left, right
    - Postorder: left, right, root
- Breadth First Traversal
    - Level Order Traversal
