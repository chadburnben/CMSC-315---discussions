"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.

Real-world Scenario: I chose to implement a review site similar to
Rotten Tomatoes because it can be to sort titles through a Tomato-meter score.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.
    """

    # This creates a copy so the original list isn't changed.
    sorted_list = lst.copy()

    # This compares the neighboring values, and then it will swap them if necessary.
    for i in range(len(sorted_list) - 1):

        swapped = False

        for j in range(len(sorted_list) - 1 - i):

            if sorted_list[j] > sorted_list[j + 1]:

                # This does a swap between the two values
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )

                swapped = True

        # Stops if values don't need to be swapped.
        if not swapped:
            break

    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.
    """

    # This creates a list with zero or one value that is already sorted
    if len(lst) <= 1:
        return lst.copy()

    # This looks for the middle of the list.
    middle = len(lst) // 2

    # The takes the list and divides them into smaller list.
    left = lst[:middle]
    right = lst[middle:]

    # Uses recursive to sort both halves.
    left = merge_sort(left)
    right = merge_sort(right)

    # Does a merge for sorted halves together.
    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    result = []

    left_index = 0
    right_index = 0

    # Does a comparison of the different values from both list.
    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Adds the remaining over values from the left list.
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    # Adds values from the right list
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    # I had my first dataset represent Rotten Tomatoes movies scores.
    print("\n=== DATASET #1: ROTTEN TOMATOES SCORES ===")

    movie_scores = [72, 95, 41, 88, 67, 100, 53, 79, 91, 64]

    print("Original movie scores:")
    print(movie_scores)

    bubble_result = bubble_sort(movie_scores)
    merge_result = merge_sort(movie_scores)

    print("\nBubble Sort result:")
    print(bubble_result)

    print("\nMerge Sort result:")
    print(merge_result)

    # The two algorithms produce the same sorted results.
    print("\nResults match:")
    print(bubble_result == merge_result)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")

    second_dataset = [34, 87, 12, 65, 43, 91, 28, 76, 55]

    print("Original dataset:")
    print(second_dataset)

    bubble_result = bubble_sort(second_dataset)
    merge_result = merge_sort(second_dataset)

    print("\nBubble Sort result:")
    print(bubble_result)

    print("\nMerge Sort result:")
    print(merge_result)

    print("\nResults match:")
    print(bubble_result == merge_result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    empty_list = []

    print("\n1. Empty list:")
    print("Original:", empty_list)
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))

    # Edge case 2: uses Single-element list
    single_value = [50]

    print("\n2. Single-element list:")
    print("Original:", single_value)
    print("Bubble Sort:", bubble_sort(single_value))
    print("Merge Sort:", merge_sort(single_value))

    # Third Edge case: has a ready sorted list
    already_sorted = [10, 20, 30, 40, 50]

    print("\n3. Already sorted list:")
    print("Original:", already_sorted)
    print("Bubble Sort:", bubble_sort(already_sorted))
    print("Merge Sort:", merge_sort(already_sorted))

    duplicates = [80, 50, 80, 30, 50, 90]

    print("\n4. List with duplicate values:")
    print("Original:", duplicates)
    print("Bubble Sort:", bubble_sort(duplicates))
    print("Merge Sort:", merge_sort(duplicates))

    # ===============================
    # ADDED A PERFORMANCE ANALYSIS
    # ===============================

    print("\n=== PERFORMANCE ANALYSIS ===")

    # Created a large dataset to help comprehend the differences between other algorithms
    performance_data = list(range(1000, 0, -1))

    # This import the time here keeping the sorting functions simplistic.
    import time

    start_time = time.perf_counter()
    bubble_sort(performance_data)
    bubble_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    merge_sort(performance_data)
    merge_time = time.perf_counter() - start_time

    print("Dataset size:", len(performance_data))
    print("Bubble Sort time:", bubble_time)
    print("Merge Sort time:", merge_time)

    print("\nBubble Sort has O(n²) average and worst-case time complexity.")
    print("Merge Sort has O(n log n) time complexity.")

    print("\n=== SORTING ANALYSIS ===")
    print("Bubble Sort is easier to understand and works well for small")
    print("datasets, but it becomes slower as the dataset gets larger.")

    print("Merge Sort uses a divide-and-conquer approach and is more")
    print("efficient for larger datasets, but it requires more steps")
    print("and additional memory for the merge process.")


if __name__ == "__main__":
    main()
