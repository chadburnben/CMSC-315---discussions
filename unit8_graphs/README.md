# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

Reflection: 

Through this assignment, I learned how to work with an undirected graph that utilizes an adjacency list and FIFO queues to conduct level-order traversal. I practiced marking places as visited when they are enqueued to prevent processing a location more than once. The biggest challenge was ensuring that the printed levels corresponded consistently to the visitation order. Since the neighbor list can be scanned left to right, places like Goblin Valley appeared before Orem, despite there being four connections from Pasadena. I resolved this issue by tracing the queue on paper from Pasadena and matching each dequeue to a hop count. 

Both BFS and depth-first search (DFS) examine the same connected components but in different orders. BFS uses a queue and expands one hop at a time, allowing it to find the fewest stops on an unweighted map. In contrast, DFS uses a stack or recursion and follows one road to a dead end before backtracking. I would use BFS to plan road trips by minimizing stops or finding the shortest route on a map. Conversely, I would utilize DFS for cycle detection, maze backtracking, or finding a thorough route through a park. 

