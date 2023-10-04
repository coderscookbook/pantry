 
'''
In Python, if __name__ == "__main__": is a common conditional statement that is used to control the execution of a Python script.

When a Python module is imported into another module, 
the code in that module is executed. If the module is the main program being run, 
however, the code is executed directly.

The __name__ attribute is a special built-in attribute in Python that specifies the name of the module. 
When a Python script is run directly, the __name__ attribute is set to "__main__". 
When the module is imported into another module, however, the __name__ attribute is set to the name of the module.

So, the if __name__ == "__main__": statement checks whether the script is being run directly or being imported as a module. 
If the script is being run directly (i.e., __name__ is equal to "__main__"), then the code inside the if statement will be executed. 
If the script is being imported as a module, the code inside the if statement will not be executed.

Typically, the code inside the if __name__ == "__main__": statement contains the main logic of the script, 
such as defining functions and executing code. 
This allows the script to be used both as a standalone program and as a module that can be imported into other programs.
'''

'''
Suppose you have a Python script that defines a function add_numbers(a, b) that adds two numbers together and prints the result. 
You want to be able to use this script both as a standalone program and as a module that can be imported into other scripts. 
Here's an example of how you could use if __name__ == "__main__": correctly to achieve this:
'''

# Correct Usage:
if __name__ == "__main__":
    def add_numbers(a, b):
        result = a + b
        print(f"{a} + {b} = {result}")

    if __name__ == "__main__":
        add_numbers(2, 3)
'''
In this example, the add_numbers() function is defined at the top of the script. 
The if __name__ == "__main__": statement is then used to check if the script is being run as the main program. 
If it is, the add_numbers() function is called with the arguments 2 and 3, and the result is printed to the console. 
If the script is being imported as a module, however, the add_numbers() function will not be called.
'''

# Incorrect Usage:
if __name__ == '__main__':
    def add_numbers(a, b):
        result = a + b
        print(f"{a} + {b} = {result}")

    if __name__ != "__main__":
        add_numbers(2, 3)
    '''
In this example, the add_numbers() function is defined at the top of the script, just like in the previous example. 
However, the if __name__ != "__main__": statement is used to check if the script is being imported as a module, 
rather than being run as the main program. If it is, the add_numbers() function is called with the arguments 2 and 3, 
and the result is printed to the console. If the script is being run as the main program, 
however, the add_numbers() function will not be called.

This is incorrect usage because the if __name__ != "__main__": statement will always be true when the script is imported as a module. 
This means that the add_numbers() function will always be called when the script is imported, which is not what we want.
'''   