'''WHAT NOT TO DO'''
def func(key, value, d={})
    d[key] = value
    print(d)

func('a', 10)
#prints {'a': 10}
func('b', 20)
#prints {'a': 10, 'b': 20}
#expected -> {'b', w20}t does

'''TIPS for BETTER FUNCTIONS'''
# 1. When creating functions to add functionality later, use raise exceptions
def connect():
    # pass    # instead of using pass when creating functions, use ...
    raise NotImplementedError("Connect() is missing code.")

connect() # will tell you code has not been created yet


# 2. Specifying return types and type annotations
def get_users() -> dict[int, str]:
  users: dict[int, str] = {1: 'Bob', 2: 'Jef', 3: 'Tom'}
  return users

def display_users(users: dict[int, str]) -> None:
  for k, v in users.items():
    print(k, v, sep=': ')

def main() -> None:
  users: dict[int, str] = get_users()
  display_users(users)
  
# if __name__ == '__main__': # uncomment to run
#   main()


# 3. Writing documentation for code using docstrings, sphinx markup
def get_users() -> dict[int, str]:
    """
    Retrieves the ids and usernames from a database as a dict.
    
    :return: dict[int, str]
    """
    users: dict[int, str] = {1: 'Bob', 2: 'Jef', 3: 'Tom'}
    return users

def display_users(users: dict[int, str]) -> None:
    """
    Prints each user to the console in a nice format.
    
    :param users: The users to display
    :return:
    """
    for k, v in users.items():
        print(k, v, sep=': ')

def main() -> None:
    users: dict[int, str] = get_users()
    display_users(users)
    
# if __name__ == '__main__': # uncomment to run
#   main()
 
# 4. Force progammer to be more explicit arguments
from enum import Enum
class Quality(Enum):
    LOW: int    = 480
    MEDIUM: int = 1080
    HIGH: int   = 1440

class Privacy(Enum):
    PRIVATE: str    = 'Private'
    UNLISTED: str   = 'Unlisted'
    PUBLIC: str     = 'Public'
    
def upload(file: str, *, quality: Quality, privacy: Privacy) -> None:
    print(f'Uploading: "{file}" in {quality.value}p ({privacy.value})')

def main() -> None:
    # upload('cat.mp4', 
    #        Quality.LOW, 
    #        Privacy.PRIVATE) #as functions grow this can be confusing as to what is being passed in
    
    upload('cat.mp4', 
           quality=Quality.LOW, 
           privacy=Privacy.PRIVATE) # by adding * in parameters, forces programmer to input respective keywords/positional args to be explicit

# if __name__ == '__main__':
#     main()


# 5. Force progammer to be extra explicit
# def join_text(text1: str, text2: str, text3: str, *, sep: str) -> str: # but what if we only want to insert TWO strings or a FOURTH text?

def join_text(*strings, sep: str) -> str: # "*" turns strings into a tuple 
    return sep.join(strings)

def main() -> None:
    print(join_text('A', 'B', 'C', sep='-')) 
    print(join_text('A', sep='-')) 
    print(join_text('A', 'B', 'C', 'D', 'End', sep='-')) 

# if __name__ == '__main__':
#     main()









































