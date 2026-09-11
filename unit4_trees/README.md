# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations. For my Binary Search Trees (BST), I created and tested a BST application that demonstrated recursive insertion, searching, and in-order traversal. 

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Implementation

Node class 

I made a node class that stored each department ID for every military branch. Additionally, every node had references that contained the left and right child nodes.

BST Node

I made a BST class with the root property, and the root had been set to 'None' because started empty. 

Insert operation

For my code I implemented the insert() method by using the recursive _insert_recursive() helper method. Furthermore, while doing insertion the values that were smaller than the current node had been placed on the left subtree and the larger values had been placed on the right. For my department IDs I used the following to build my tree out: 1003, 1002, 1005, 1001, 1004, 1006, 1000, 1007. The first value was 1003, which was the root of my tree. However, the smaller deparments had been placed on the left side. In addition, I had tested the insertion of several different duplicate department IDs. The duplicate happened to be placed on the right side of the matching node. This allowed the implementation ordering to be maintained. 

In-Order Traversal

For this, I implemented the inorder() method by having the recursive _inorder_recursive() helper method. The traversal would visit the left subtree first and then it would follow the current node, and the right subtree last. The BST would organize the smaller values on the left first then it would organize the bigger values on the right of the subtree. After, the in-order traversal would produce the department IDs in sorted order and would be returned in ascending order.

Testing

I would look at the tested BST by searching for the department IDs that did and didn't exist. 

Edge cases

I would test an empty BST to see if the value would return 'False' and the in-order traversal returned an empty list. In addition, I tested a one-node tree to validate that the root had been inserted and searched properly. 

## Real-World Application

This demonstrated how military department IDs could be applied in a BST as a Real-World application. This would do a department lookup and organize the records by using department ID numbers. This would search for a department and compare it with the current node, and if the ID was smaller, the search would continue to the left, and if it  was larger, it would go to the right. This was a more efficient way to search than just doing a whole scan of every record in the list.
## Discussion Board Reflection

For this assignment, I learned how Binary Search Trees (BST) organize data during the insertion process and how recursion is employed to navigate through the trees. I discovered that smaller values are placed on the left side, while larger values are positioned on the right. Additionally, I observed that in-order traversal produces a sorted output from the BST.

One of the initial challenges was ensuring that self.root = self._insert_recursive(...) sets the first department as the root of the tree. Another difficulty I encountered was understanding how the recursive insertion and search methods determined the direction to move. This involved evaluating each comparison: smaller values move to the left, and larger values move to the right. 

Lastly, I found that using a Binary Search Tree (BST) is more efficient than using a linear list for searching. This is because each step in the search process reduces the number of remaining IDs by eliminating portions of the tree. Additionally, a balanced BST is particularly efficient for searching, as it requires checking fewer nodes. However, certain factors can affect the tree's efficiency, such as inserting values in sequential order, which can lead to an unbalanced tree.
