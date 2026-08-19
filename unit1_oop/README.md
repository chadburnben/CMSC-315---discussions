# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.
## Implementation

For the assignment demonstrating the required concepts for my Python OOP, I used a sports and surfing example. I created a ParentClass to represent a track athlete, using a class variable (sports = “track”), two instance variables (name and age), a constructor, and a display_info() method. The display_info() method returns the athlete’s information as a formatted string.

The next TODO: I created a ChildClass that calls and inherits the parent class constructor super().__init__(). This ChildClass includes a class variable called (activity = "Surfing"), two new instance variables (years_experience and board_type), and a list of favorite surfing spots provided by the user.

Additionally, I implemented a new method, add_spot(), and overrode the parent class's display_info() method to display both inherited details and information specific to the child object.

For my main(), I created one parent object and one child object, then called methods to demonstrate inheritance and ran both. The namespace demonstration has two surfer child objects created and accesses the class variable through both the class and object. This adds a unique attribute to just one object and uses __dict__  to display the instances namespaces and class. Lastly, I created an object with a nested list of favorite surfing spots. The nested list creates both a shallow copy and a deep copy that modifies the original list. The shallow copy is affected because it shares the nested list with the original copy, while the deep copy stays independent because it has its own nested list.

## Discussion Board Reflection
For this assignment, I demonstrated how inheritance allows a child class to be reused and extends a parent class, showed how class variables are different than instance variables, and compared the difference between shallow and deep copying with nested mutable data. I enjoyed getting more familiar using __dict__ to inspect namespaces. I picked sports and surfing because it shows how a parent class provides basic information while a child class shows more specific information.

The challenges I ran into were keeping the constructor parameters consistent, and some of my earlier code had mismatched arguments between the class definition and places where I had created objects, that had errors. In addition, I mixed up some of my method names and referenced attributes that didn’t exist. I corrected my implementation by evaluating the error codes produced in IntelliJ and the Python interpreter compared my class initialization line by line with each spot I created an object. I would test the code one section at a time and debug. There were times when I would go back and look at some examples of how Parent and Child classes were used in the course to get an idea of the code structure.

When comparing procedural programming to object-oriented programming (OOP), it's clear that OOP groups related data and behavior into a single unit. In contrast, procedural programming requires separate functions and data structures to manage the same information. I believe that using classes and objects in OOP makes it much easier to expand, explore, and reuse components. I've noticed that reusable classes help reduce repeated code, resulting in cleaner and easier-to-read code.

Inheritance and encapsulation greatly improve maintainability and promote code reuse. When a parent class is created, its properties and methods are automatically inherited by child classes. This means that new features can be added without needing to rewrite the existing code. Such an approach is beneficial for projects that require organized and easily expandable code
