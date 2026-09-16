# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search. For my assignment, I compared two searching algorithms: linear search and binary search. I used a list of U.S. states I have visited, arranged alphabetically, to test both algorithms.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

Linear Search

The linear search algorithm starts at the first item in the list and checks each item one by one until the target item is found. Once it finds the target, the function returns its index. If the entire list is checked without finding the target, the function returns -1. The worst-case time complexity for linear search is O(n), as the number of comparisons directly increases with the number of items in the list.

Binary Search

I implemented binary search using low, high, and mid values. This algorithm checks the middle item of a sorted list and eliminates half of the remaining search area after each comparison. The time complexity for binary search is O(log n) because the search area is divided approximately in half during each iteration. Note that this method requires the list to be sorted beforehand.

Dataset Testing

I used both a small dataset and a larger dataset for testing. The small dataset contained 10 state names, and both algorithms produced the correct results when searching for an existing state or for a state that was not present. For the larger dataset, which contained 200,000 sorted state names, I observed more noticeable differences between the two algorithms. Linear search required checking more items, including those that were missing or located near the end of the list. In contrast, binary search continuously reduced the search area by half, making it significantly more efficient for larger datasets.


Edge Case Testing  

I tested several edge cases, including an empty list, a single-element list, a value located at the beginning of the list, a value at the end of the list, and a missing value. Each search function returned the expected results.

 
Real-World Scenario

In my real-world scenario, I searched through a list of states that I have visited in the U.S. For this assignment, linear search was useful for an unsorted list because it does not require the items to be organized. On the other hand, binary search was more effective with the alphabetically organized list, as it quickly eliminates half of the remaining items during the search.
## Discussion Board Reflection

For this assignment, I learned that linear search and binary search handle the same problems just in a different way. Additionally, I learned that linear search checks items sequentially and works for an unsorted list. However, binary search depends on the data already being sorted. Also, I learned why binary search has O(log n) performance. The reason is that it removes about half of the remaining search space at every step.
