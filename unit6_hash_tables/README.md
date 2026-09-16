# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior. For the assignment, I created a English to Tagalog dictioanry. The dictionary stores English words as keys used as hash table keys. 

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection
Reflection

While completing this assignment, I learned how to create an efficient Python dictionary and how it relates to hash tables in storing key-value pairs. Additionally, I also learned that a Python dictionary is a hash table" concrete and a hash function turns each English word into a bucket index. This means that average lookup is O(1), and that Python still handles collisions when two words land in the same bucket, and assigning an existing key assigns to a missing key insert. Safe APIs ( .get(), pop(key, default matter because a raw [] or del on a missing word causes a KeyError and can cause the application to crash. One challenge I encountered was understanding what happens if a key doesn’t exist. To address this, I used the get() method for lookups and checked whether the key was present in the dictionary before attempting to delete it.

Additionally, I discovered that hash tables use a hash function to determine where data is stored and located. A collision occurs when two different keys produce the same hash location. Therefore, effective hash table implementation requires a method to handle these collisions to ensure data can be stored and retrieved accurately. Fortunately, Python manages this behavior internally, so I don’t need to implement collision resolution myself.
