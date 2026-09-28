# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort. The assignment compares Bubble Sort and Merge Sort by running multiple datasets and testing each edge case. This runs a Rotten Tomatoes score catalog and then sorts the titles by their respective scores from (1-100), which the score keeps the original relative order.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

For my assignment, I aimed to implement code that functions similarly to Rotten Tomatoes, specifically for a sort-by-score page. During this process, I learned how design influences algorithm complexity. For instance, I discovered that writing a Bubble Sort results in a time complexity of O(n²) due to its nested loops.  

One challenge I encountered was keeping the Merge Sort stable while ensuring that the original caller list was not mutated. To address this, I copied the input. I utilized the less-than-or-equal-to operator (<=) in the merge function so that two films with the same score of 87% would remain in their catalog order. I printed the original list after sorting to confirm it remained unchanged. Another challenge was figuring out how to properly divide and then merge the lists in the Merge Sort process. To better understand the problem, I worked with smaller datasets and checked each step of the merging process, ensuring that my code functioned correctly with an unsorted list. 

In a real-world scenario, I chose to implement a sort-by-score feature like Rotten Tomatoes because I enjoy movies. This functionality will order movie titles by Tomatometer score while preserving their original order when multiple films share the same percentage. The system will handle searches with both single results and those involving a 500-title browse page. The Merge Sort will effectively manage all cases, while the Bubble Sort will be suitable for tiny, nearly sorted lists. 
