"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    """When creating a stack use LIFO (Last in, first out) container."""
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = [] # The End of a list is the Top of a stack.

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # An append() will always begin at the top because pop() removes from the top.
        # The newest item becomes the first one out (LIFO).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # List.pop()on an empty list creates and IndexError,
        # which crashes the program. This means its important
        # to guard first (stack underflow).
        # Design choice: return none.
        if self.is_empty():
            return None
        return self.items.pop()  # This removes from the TOP

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek shows the most recent activity without removing
        # it and is a read-only.
        # In addition, it gives us a look at the top item and
        # the stack is unchanged.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0

    def size(self):
        """Number of items currently stored."""
        return len(self.items)

    def __str__(self):
        """Show bottom -> top so LIFO order is visible in the output."""
        return "bottom " + str(self.items) + " top"


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        # Deque gives an add/remove feature from both ends.
        self.items = deque()  #

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # When there is a new item it goes to the back so the oldest item stays in
        # front (First one in, first one out) --> FIFO.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None  # Do a return none, instead crashing on an empty queue.
        return self.items.popleft()  # This removes from the front.

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front() shows who is served without having to change the item
        # and saves the next activity that would be processed, without
        # having to remove it.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        """Have front Show back, so FIFO order is visible in display."""
        return "front " + str(list(self.items)) + " back"


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")
    print("Stack used to track recent Garmin activities (LIFO – most recent first)")

    activity_stack = Stack()
    print("Created empty activity stack.")
    print(f"Is empty? {activity_stack.is_empty()}")

    # Push a minimum of 4 Garmin-style activities values
    print("\n--- Logged activities on the Garmin watch ---")
    activities = [
        "Ruck Run - 6.5 miles",
        "Pool Swim - 1600 yards",
        "Evening Recovery Run - 3.1 miles",
        "Sleep Tracking - 7.5 hours"
    ]

    for activity in activities:
        activity_stack.push(activity)
        print(f"  Pushed: {activity}")

    print("\n--- Demonstrating LIFO behavior ---")
    print("Popping activities (most recent activity is removed first):")
    while not activity_stack.is_empty():
        latest = activity_stack.pop()
        print(f"  Popped: {latest}")

    print("\n--- Edge Case: pop() on empty stack ---")
    result = activity_stack.pop()
    print(f"  pop() returned: {result}")

    print("\n--- Edge Case: peek() on empty stack ---")
    result = activity_stack.peek()
    print(f"  peek() returned: {result}")

    print("\n--- Edge Case: single-item stack ---")
    single_stack = Stack()
    single_stack.push("Quick Strength Session")
    print(f"  After push: is_empty = {single_stack.is_empty()}")
    removed = single_stack.pop()
    print(f"  Popped: {removed}")
    print(f"  After pop: is_empty = {single_stack.is_empty()} (verified empty)")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    print("Garmin Connect uses a Queue for planned training workouts (FIFO – first scheduled first)")

    workout_queue = Queue()
    print("Created empty workout queue.")
    print(f"Is empty? {workout_queue.is_empty()}")

    # The enqueue contains minimum of 4 values
    print("\n---  Workout Scheduling via Garmin App ---")
    planned = [
        "Tuesday Tempo Run",
        "Wednesday Swim Intervals",
        "Thursday Easy Run + Strength",
        "Friday Long Run"
    ]

    for workout in planned:
        workout_queue.enqueue(workout)
        print(f"  Enqueued: {workout}")

    print("\n--- Demonstrating FIFO behavior ---")
    print("Workouts are processed the order they are scheduled:")
    while not workout_queue.is_empty():
        next_workout = workout_queue.dequeue()
        print(f"  Dequeued (starting): {next_workout}")

    print("\n--- Edge Case: dequeue() on empty queue ---")
    result = workout_queue.dequeue()
    print(f"  dequeue() returned: {result}")

    print("\n--- Edge Case: front() on empty queue ---")
    result = workout_queue.front()
    print(f"  front() returned: {result}")

    print("\n--- Edge Case: single-item queue ---")
    single_queue = Queue()
    single_queue.enqueue("Saturday Rest Day Walk")
    print(f"  After enqueue: is_empty = {single_queue.is_empty()}")
    removed = single_queue.dequeue()
    print(f"  Dequeued: {removed}")
    print(f"  After dequeue: is_empty = {single_queue.is_empty()} (verified empty)")

    # ===============================
    # Garmin Watch App Scenario
    # ===============================
    """
  Garmin Watch App Scenario: This is an app for Garmin Connect smartwatch.


  Stack -> It will "undo last logged activity," and undo the most recent entry first, doing
            it backwards will corrupt the weekly totals. Therefore, LIFO is required.

  Queue -> "Upload sync queue." The activties will link to the Garmin Connect from the order
            the activity was recorded; ensuring the timeline stays in chronological order.
  """
    print("\n=== CUSTOM REAL-WORLD SCENARIO ===")
    print("Garmin Watch Logged Activity (Stack) + Weekly Training Plan (Queue)")
    print("Stack = undo last logged activity (most recent first)")
    print("Queue = list of planned workouts for the week (first scheduled first)")


if __name__ == "__main__":
    main()
