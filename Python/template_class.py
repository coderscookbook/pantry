# Define a class named `Person`
class Person:
    # The __init__ method is the constructor, which is called when a new object is created
    def __init__(self, name, age):
        # Initialize the member variables (attributes) of the class
        self.name = name
        self.age = age

    # A method (function) that is part of the class
    def introduce_yourself(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Create an object (instance) of the Person class
person1 = Person("Alice", 30)

# Access the attributes and methods of the person1 object
print(person1.name) # Output: Alice
print(person1.age)  # Output: 30

# Call the introduce_yourself method
person1.introduce_yourself() # Output: Hi, my name is Alice and I am 30 years old.
