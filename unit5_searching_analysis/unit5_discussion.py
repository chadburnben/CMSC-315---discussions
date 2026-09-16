
"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.

REAL-WORLD SCENARIO:
For my real-world scenario, I created a list of U.S. states that I have visited. 
This list works like a contact list where it searches for one name and then decides 
whether it is already there. The linear search walks the list from the top, and 
the binary search works when the list is sorted from A-Z. The binary search will 
cut the remaining names in half for every comparison. 
"""

import time


# This is the sorted list of each U.S. State visited from A-Z
VISITED_STATES = [
    "Alabama",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Delaware",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Indiana",
    "Iowa",
    "Kentucky",
    "Louisiana",
    "Maryland",
    "Michigan",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "Ohio",
    "Oklahoma",
    "Pennsylvania",
    "South Carolina",
    "Tennessee",
    "Texas",
    "Utah",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wyoming",
]


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # The linear search starts at index 0 and will check each element at a time
    # until it finds the target.
    # This also explains the time complexity directly next to the code.
    # The linear search will check every item of the list in the worst case: the target
    # is last or missing -> n comparisons.
    # The Best case finds the target first and 1 comparison -> 0(n).
    # The average case will also grow with n, allowing the time complexity to be 0(n).
    # The list doesn't have to be sorted.
    # return -1 scans the whole list.
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1



def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # The binary search has a window low and high over a sorted list.
    # Every loop will pick the midpoint and throw away half the window:
    #   target < mid-value  -> search left half (high = mid - 1)
    #   target > mid-value  -> search right half (low  = mid + 1).
    # After k steps, the window is about n / 2^k items.
    # This will finish in O(log n) comparisons.
    # When the list is sorted properly, the process will work smoothly.
    low = 0
    high = len(lst) - 1

    # Elif: the mid is too large, so each name after the mid will also be too large.
    # Else: is the opposite if the mid is too small, then every name before the mid will
    # be too small, and discard the left half instead of the right.
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def run_search(label, func, lst, target):
    """Time one search and print a readable result line."""
    start = time.perf_counter()
    index = func(lst, target)
    elapsed_ms = (time.perf_counter() - start) * 1000

    if index == -1:
        status = "NOT FOUND"
    else:
        status = f"FOUND at index {index} ({lst[index]})"
    print(f"  {label:<22} {status:<42} {elapsed_ms:8.4f} ms")
    return index, elapsed_ms


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")
    print("Scenario: search a personal list of U.S. states I have visited.")
    print(f"Visited-state count: {len(VISITED_STATES)}")
    print(f"List is sorted A-Z: {VISITED_STATES == sorted(VISITED_STATES)}")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    # This will be for the first 10 visited states as already sorted. This model
    # is a short contact list.
    small_data = VISITED_STATES[:10]
    print(f"Small dataset (n={len(small_data)}): {small_data}")

    exists_small = "Colorado"
    missing_small = "Florida"

    print(f"\nSearch for existing state '{exists_small}':")

    # Linear search will check from the start.
    # The binary search will use the sorted order to eliminate
    # half of the list.
    run_search("Linear search", linear_search, small_data, exists_small)
    run_search("Binary search", binary_search, small_data, exists_small)

    print(f"\nSearch for missing state '{missing_small}':")

    # The linear search will check every item before determining Florida is missing
    # and inspects that all 10 names before giving up.
    # The binary search will reduce the search area until nothing remains and
    # halves the window empty.
    run_search("Linear search", linear_search, small_data, missing_small)
    run_search("Binary search", binary_search, small_data, missing_small)
    print("On a tiny list both algorithms agree and the time gap is tiny.")

    # The full list of states that I have gone to for my
    # real-world scenario (35 states).
    print("\n=== REAL-WORLD LIST (all visited states) ===")
    print(f"Full visited list (n={len(VISITED_STATES)}):")
    print(", ".join(VISITED_STATES))
    print("\nLookup Maryland (home state, exists) and Florida (missing):")
    run_search("Linear / Maryland", linear_search, VISITED_STATES, "Maryland")
    run_search("Binary / Maryland", binary_search, VISITED_STATES, "Maryland")
    run_search("Linear / Florida", linear_search, VISITED_STATES, "Florida")
    run_search("Binary / Florida", binary_search, VISITED_STATES, "Florida")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # This is a scale of the visited-state idea that is up to 200,000 unique sorted labels.
    # For example Maryland 000123. This is the
    large_n = 200_000
    large_data = [f"{VISITED_STATES[i % len(VISITED_STATES)]} {i:06d}"
                  for i in range(large_n)]
    large_data.sort()
    print(f"Large dataset created: n = {large_n:,} sorted state labels")

    # This value is guaranteed to exist and is selected near the middle, making
    # a linear search travel through a large portion of the list.
    exists_large = large_data[large_n // 2]
    missing_large = "ZZZ Not A State 999999"
    print(f"\nSearch for existing label '{exists_large}':")
    # The linear search will walk toward the middle/end and inspect a large portion
    # of this list.
    # The binary search will repeatedly cut the search in half about log2(200000)
    # ≈ 18 comparisons.
    lin_i, lin_ms = run_search("Linear search", linear_search, large_data, exists_large)
    bin_i, bin_ms = run_search("Binary search", binary_search, large_data, exists_large)
    print(f"  Same index returned? {lin_i == bin_i}")

    if bin_ms > 0:
        print(f"  Binary was about {lin_ms / bin_ms:.1f}x faster on this lookup.")

    print(f"\nSearch for missing label '{missing_large}':")

    print(f"\nSearch for missing label '{missing_large}':")
    # Linear search will scan the entire list before returning -1, so
    # in this case it will scan 200,000 items.
    # Binary search will finish in about 18 steps and cut the search in half
    run_search("Linear search", linear_search, large_data, missing_large)
    run_search("Binary search", binary_search, large_data, missing_large)
    print("As the dataset grows, linear search requires more comparisons.")
    print("Binary search removes about half of the remaining items each time.")
    print("This is why linear search is O(n) while binary search is O(log n).")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    print("\n1) Empty list [] looking for Maryland:")
    # Both the loops will return -1 and the loops never run because the
    # low starts at 0 and high starts at -1 and there are no items to search.
    run_search("Linear search", linear_search, [], "Maryland")
    run_search("Binary search", binary_search, [], "Maryland")

    print("\n2) Single-element list ['Texas']:")
    # This is a list that only contains one item and both returns
    # index 0 and misses both return -1.
    run_search("Linear hit", linear_search, ["Texas"], "Texas")
    run_search("Binary hit", binary_search, ["Texas"], "Texas")
    run_search("Linear miss", linear_search, ["Texas"], "Ohio")
    run_search("Binary miss", binary_search, ["Texas"], "Ohio")

    print("\n3) First and last names on the full visited list:")
    run_search("Linear first", linear_search, VISITED_STATES, VISITED_STATES[0])
    run_search("Binary first", binary_search, VISITED_STATES, VISITED_STATES[0])
    run_search("Linear last", linear_search, VISITED_STATES, VISITED_STATES[-1])
    run_search("Binary last", binary_search, VISITED_STATES, VISITED_STATES[-1])

    print("\n4) Missing value on the full visited list (Florida):")
    run_search("Linear missing", linear_search, VISITED_STATES, "Florida")
    run_search("Binary missing", binary_search, VISITED_STATES, "Florida")

    print("\n=== SUMMARY ===")
    print("Linear search: O(n). Works on unsorted data. Simple.")
    print("Binary search: O(log n). Needs sorted data. Much faster at scale.")
    print("Use linear for a short or messy list (unsorted downloads folder).")
    print("Use binary after the collection is ordered (sorted state names).")


if __name__ == "__main__":
    main()
