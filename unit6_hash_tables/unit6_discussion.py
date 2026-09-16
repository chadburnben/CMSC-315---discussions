"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.
You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    #I created an empty dictionary to use as my Tagalog dictionary.
    # I created an empty dictionary that will be used for my Tagalog dictionary.
    # The English word will be the key and the Tagalog translation will be the value.
    # In Python, dictionaries behave similarly to a hash table because the key gets
    # hashed to determine where the key's value gets stored.
    # The Python code can find values quickly without having to look at every value.

    tagalog_dict = {"hello": "kamusta", "water": "tubig", "food": "pagkain", "house": "bahay", "aso": "dog"}

    # For my dictionary, I added five English words as an example

    print("\n=== INSERT OPERATIONS ===")
    print("Tagalog dictionary after inserting five words:")
    print(tagalog_dict)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("Looking up existing words:")

    #
    # The dictionary lookup will use a key to find the associated value.
    # Python will hash the key and use that information to find the value.
    # This is a more efficient way to narrow down the search.
    print("hello ->", tagalog_dict["hello"])
    print("water ->", tagalog_dict["water"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("Dictionary before updating 'food':")
    print(tagalog_dict)

    # It's important to assign a new value to an existing value because the
    # existing key updates the key's value.
    # For instance, the key 'food' stays in the dictionary; however, the translation
    # is changed.
    tagalog_dict["food"] = "pagkain / pagkain na kinakain"

    print("Dictionary after updating 'food':")
    print(tagalog_dict)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("Dictionary before deleting 'house':")
    print(tagalog_dict)

    # The del statement will remove the key and the associated value.
    # Now, after deleting the word key "house," it is no longer in the dictionary.
    del tagalog_dict["house"]

    print("Dictionary after deleting 'house':")
    print(tagalog_dict)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # For edge case 1, it looks up a key that doesn't exist.
    # It helps to use get() to check for a missing key without causing key error,
    # and if the key is missing, it will return None.
    missing_word = tagalog_dict.get("school")

    if missing_word is None:
        print("Lookup for 'school': Word was not found in the dictionary.")
    else:
        print("school ->", missing_word)

    # For edge case 2, when trying to delete a key that doesn't exist, using
    # 'in' operator first prevents a KeyError from happening.
    if "school" in tagalog_dict:
        del tagalog_dict["school"]
        print("Deleted 'school' from the dictionary.")
    else:
        print("Delete for 'school': Word was not found, so nothing was deleted.")

    # For edge case 2, when updating a key that doesn't exist, assigning a value
    # to a new key does not cause an error.
    # Python will add the new key-value pair to the dictionary.
    tagalog_dict["school"] = "paaralan"
    print("Update for missing key 'school':")
    print("school ->", tagalog_dict["school"])

    print("\n=== FINAL TAGALOG DICTIONARY ===")
    print(tagalog_dict)


if __name__ == "__main__":
    main()
