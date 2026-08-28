"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # When the value gets inserted near the beginning it usually
    # takes longer because there are more elements that need to
    # be shifted over.

    lst.insert(index, value)

    return lst


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # This checks if the index exist before removing the item,
    # which prevents an IndexError when the list is empty or
    # index is not in the valid range.
    if index < 0 or index >= len(lst):
        return None

    # When removing an item it causes the other elements to shift left.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Checking an item from the beginning one item at a time
    # is a known as a linear search.
    for i in range(len(lst)):
        if lst[i]["title"] == value:
            return i

    return -1


def movie(title, domestic, worldwide, status):
    return {
        "title": title,
        "domestic": domestic,
        "worldwide": worldwide,
        "status": status,
    }


def show_list(label, lst):
    print(label)

    if not lst:
        print("  (empty)")
        return

    for i, movie_info in enumerate(lst):
        print(
            f"  [{i}] {movie_info['title']} | "
            f"{movie_info['status']} | "
            f"domestic {movie_info['domestic']} | "
            f"worldwide {movie_info['worldwide']}"
        )


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Create the original movie watchlist.
    watchlist = [
        movie(
            "Project Hail Mary",
            "$344.1M",
            "$684.0M",
            "released March 2026"
        ),
        movie(
            "Young Washington",
            "$47.0M",
            "$47.1M",
            "released July 2026"
        ),
        movie(
            "The Odyssey",
            "$547.2M",
            "$1.5B",
            "in theaters"
        ),
    ]

    show_list("Original list:", watchlist)

    # Creates a movie list and how much the movie have made
    insert_at(
        watchlist,
        0,
        movie(
            "Spider-Man: Brand New Day",
            "$866.5M",
            "$2.2B",
            "in theaters"
        )
    )

    show_list(
        "After inserting at the beginning:",
        watchlist
    )

    # This finds the index and inserts the movie there.
    middle = len(watchlist) // 2

    insert_at(
        watchlist,
        middle,
        movie(
            "Dune: Part Three",
            "not released",
            "not released",
            "due Dec 18, 2026"
        )
    )

    show_list(
        f"After inserting in the middle (index {middle}):",
        watchlist
    )

    # This inserts a movie at the end of a list.
    insert_at(
        watchlist,
        len(watchlist),
        movie(
            "Avengers: Doomsday",
            "not released",
            "not released",
            "due Dec 18, 2026"
        )
    )

    show_list(
        "After inserting at the end:",
        watchlist
    )
    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Removes the first movie from the list.
    removed = delete_at(watchlist, 0)

    print(
        "Removed from beginning:",
        removed["title"]
    )

    show_list(
        "List after beginning deletion:",
        watchlist
    )

    # This will remove our movie from the middle of the list.
    middle = len(watchlist) // 2
    removed = delete_at(watchlist, middle)

    print(
        f"Removed from middle (index {middle}):",
        removed["title"]
    )

    show_list(
        "List after middle deletion:",
        watchlist
    )

    #  This will remove the last movie from the list.
    removed = delete_at(
        watchlist,
        len(watchlist) - 1
    )

    print(
        "Removed from end:",
        removed["title"]
    )

    show_list(
        "List after end deletion:",
        watchlist
    )


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Searches for a movie in the list.
    result = search_value(
        watchlist,
        "The Odyssey"
    )

    if result != -1:
        print(
            "'The Odyssey' was found at index:",
            result
        )
    else:
        print("'The Odyssey' was not found.")

    # Searches for other movies that exist.
    result = search_value(
        watchlist,
        "Project Hail Mary"
    )

    if result != -1:
        print(
            "'Project Hail Mary' was found at index:",
            result
        )
    else:
        print("'Project Hail Mary' was not found.")

    # Searches for movies that don't exist.
    result = search_value(
        watchlist,
        "Inception"
    )

    if result != -1:
        print(
            "'Inception' was found at index:",
            result
        )
    else:
        print("'Inception' was not found.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Trys to delete invalid indexes
    result = delete_at(watchlist, 99)

    print(
        "Delete using invalid index 99:",
        result
    )

    # Trys to delete anything from the empty list
    empty_list = []

    result = delete_at(empty_list, 0)

    print(
        "Delete from an empty list:",
        result
    )

    # Inserts a movie in the empty list.
    insert_at(
        empty_list,
        0,
        movie(
            "Avatar: Fire and Ash",
            "catalog / earlier 2026 run",
            "prior release",
            "already released"
        )
    )

    show_list(
        "Insert into previously empty list:",
        empty_list
    )

    # Searches an empty list
    result = search_value(
        [],
        "The Super Mario Galaxy Movie"
    )

    print(
        "Search empty list:",
        result
    )


if __name__ == "__main__":
    main()