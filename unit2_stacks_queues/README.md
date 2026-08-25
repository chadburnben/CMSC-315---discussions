# Unit 2 Discussion: Stacks and Queues

## Overview
The assignment covered the two fundamental linear data structures, Stack and Queue. The two structures were implemented in Python to demonstrate LIFO (Last-In, First-Out) and FIFO (First-In, First-Out) behavior. I answered the questions asked in each comment line and added my own comments to explain each operation and test multiple cases.

## Learning Objectives
- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Stack Implementation 

In my stack class Implementation, I used a Python list for the internal data structure and end of the list represented the top of the stack. I implemented the following operations:

  1. push() it adds a new value to the top of a stack.
  2. pop() removes and returns the most recent added value.
  3. peek() returns the top value without having to return it.
  4. is_empty() checks if the stack contains any of the values.
  5. size() returns the values that are stored.
     
In my stack implementation, I utilized a Python list to store values. Creating a push() operation adds the item to the top, peek() allows you to view the top item, and while pop() removes the most recently added item. Additionally, the is_empty() operation checks if the stack contains anything. The stack represents the activity history so in the example it would be most recent run, swim, bike, or sleep time, which is LIFO.
 
## Queue Implementation 

When implementing my queue, I utilized Python's deque. The enqueue() operation adds an item to the back and dequeue() removes the item from the front. Also, I added empty-queue handling; this ensures that dequeue() and front() return None and issue a Warning that prevents the program from crashing. Furthermore, I implemented front(), is_empty() and append(). The append() adds items to the back, and popleft() removes items from the front. In my example, I planned workouts, so the first scheduled workout was processed before the rest, making the queue represent the training plan. Workouts were completed in the order they were scheduled, preserving the undo feature and training timelines (FIFO). The queue uses FIFO behavior because it adds the first item that is removed. The queue implements the following operations:
  1. enqueue() adds a new value to the back of the queue.
  2. dequeue() removes and returns the value from the front.
  3. front() returns the first value without needing to remove it.
  4. is_empty() checks what values queue contains.
  5. size() returns the number of values that are stored.
  
## LIFO Behavior Demonstration

For my stack demonstration, I used Garmin Watch's and logged four activities:

  1. Ruck Run (6.5) miles
  2. Pool Swim (1600 yards)
  3. Evening Recovery Run (3.1 miles)
  4. Sleep Tracking - (7.5 hour)
     
The activities were then removed from the stack, with Sleep Tracking going first, demonstrating LIFO. This demonstrates LIFO because the newest activities are accessed before the oldest ones. In addition, I tested a push() operation, which adds the item to the top; peek() allows you to view the top item; and pop() removes the most recently added item. I also tested is_empty(), which checks whether the stack contains anything. The stack represents the activity history, so in the example it would be the most recent run, swim, bike, or sleep time, which is LIFO. Lastly, I created a stack with one activity and removed it to verify that the stack was empty.

## FIFO Behavior Demonstration

When I did my queue demonstration, I made a weekly training workout schedule and added the following four planned workouts:

  1. Tuesday Tempo Run
  2. Wednesday Swim Intervals
  3. Thursday Easy Run + Strength
  4. Friday Long Run
     
The workouts were removed from the queue in the same order they were added, demonstrating FIFO behavior. This means that the first workout scheduled is the first one to be processed. I used a similar approach to what I applied to LIFO by creating a queue with a one activity and then removing it to confirm that the queue was empty afterwards.

## Edge Case Handling

In my code, I tested multiple test cases, including popping and peeking from an empty stack, as well as dequeuing and viewing the front of an empty queue. The code was crashing in these scenarios, so I added a return statement that returns “None” and displays a warning message. This helped to set boundary conditions in a controlled way. For my edge cases, I tested the following to make the program more reliable: 
•	pop() on an empty stack and returns “None” with a warning message
•	peek() on an empty stack and returns “None” with a warning message
•	dequeue() on an empty queue returns “None” with a warning message 
•	View the front() on an empty queue returns “None” with a warning message
•	Remove the only item from a stack
•	Remove the only item from a queue

## Discussion Board Reflection

In my code, I tested multiple test cases, including popping and peeking from an empty stack, as well as dequeuing and viewing the front of an empty queue. The code was crashing in these scenarios, so I added a return statement to return None and display a warning message. 
 
One of the challenges I encountered was handling cases where the stack or queue is empty. To address this, I decided to return None and print a warning message in the output.

Overall, this assignment required me to think about FIFO and LIFO and how to apply a stack in a real-world example that I applied practically.  I also learned that the choice between a stack and a queue depends on how information needs to be processed. A stack works well when the newest item should be handled first, and a queue works well when items need to be processed in the order it was received.

