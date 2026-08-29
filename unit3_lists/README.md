# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists. For my code, I created a movie watchlist application to demonstrate how Python lists behave. When values are inserted, removed, and searched. The application used a list of movie dictionaries that contained the movie titles, domestic earnings, worldwide earnings, and release status. This meets the required list operations and multiple edge cases. 

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection
Through this assignment, I learned about how Python lists handle insertion, deletion, and searching. I had to consider how these operations apply to everyday applications in the real world. I became more familiar with using insert() and pop() and how the location of an operation affects performance. Additionally, I discovered that searching for an item one by one is categorized as a linear search, as the program checks the elements sequentially.

One challenge I encountered was ensuring that the deletion operations were safe when invalid indexes or empty lists were provided. I addressed this issue by adding index validation before calling pop(). Furthermore, I tested multiple edge cases to ensure the program returned the expected values without errors.

I noticed that list operations significantly impact performance in real-world applications, especially with large datasets. Inserting or deleting items near the start of an array-based list can cause many elements to shift. As a developer, it is essential to understand the performance differences between data structure
