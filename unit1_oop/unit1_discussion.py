"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing    TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    sports = "track"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Sports: {self.sports}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    # New class variable
    activity = "Surfing"

    def __init__(self, name, age, years_experience, board_type="Shortboard"):
        # Call parent constructor
        super().__init__(name, age)
        # New instance variables
        self.years_experience = years_experience
        self.board_type = board_type
        self.favorite_spots = []

    def add_spot(self, spot_name):
        """New method"""
        self.favorite_spots.append(spot_name)

    def display_info(self):
        """Override parent method"""
        base = super().display_info()
        return (f"{base}, Activity: {self.activity}, "
                f"Experience: {self.years_experience} years, "
                f"Board: {self.board_type}, Spots: {self.favorite_spots}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two child objects
    surfer1 = ChildClass("Ben", 28, 8)
    surfer2 = ChildClass("Chad", 25, 5)

    # Class variable is accessed through the class
    print("Class variable via class:", ChildClass.activity)

    # Class variable is accessed through an object
    print("Class variable via object:", surfer1.activity)

    # Add a new attribute to only one object
    surfer1.home_break = "Ocean City"

    # Display each object's namespace
    print("\nsurfer1.__dict__:", surfer1.__dict__)
    print("surfer2.__dict__:", surfer2.__dict__)

    # Show class namespace
    print("\nChildClass namespace (non-dunder attributes):")
    for key in ChildClass.__dict__:
        if not key.startswith("__"):
            print(" -", key)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Created object that contains nested mutable data
    original = ChildClass("Lewis", 22, 3, "Fish")
    original.add_spot("Assateague")
    original.add_spot("Ocean City")

    # Created shallow and deep copies
    shallow = copy(original)
    deep = deepcopy(original)

    # Modified original object's nested data
    original.favorite_spots.append("Siargao")
    original.name = "Lewis Updated"

    # Display output
    print("Original :", original.display_info())
    print("Shallow  :", shallow.display_info())
    print("Deep     :", deep.display_info())

    print("\nExplanation:")
    print("- Shallow copy shares the same favorite_spots list because both original and shallow copy are saved in the same memory")
    print("- Deep copy creates own independent copy of favorite_spots list and the original does not affect the Deep copy")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Parent object
    print("\nParent object:")
    person = ParentClass("Ben", 28)
    print(person.display_info())

    # Child object
    print("\nChild object:")
    surfer = ChildClass("Lewis", 22, 6)
    surfer.add_spot("Ocean City")
    print(surfer.display_info())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()