'''
@abstractmethod
- used in abstract classes as a blueprint for classes
  - abstract classes: blueprints for other classes
- must be imported
'''

from abc import ABC, abstractmethod

# Blueprint animal class
class Animal(ABC):
  def __init__(self, name: str) -> None:
    self.name = name
    
  @abstractmethod
  def sound(self) -> None:
    ...
  
  @abstractmethod
  def move(self) -> None:
    ...
    # in other cases, you would probably raise "NOT IMPLEMENTED" error  
    
# Create cat from abstract animal class
class Cat(Animal):
  def __init__(self, name: str) -> None:
    super().__init__(name)
    
  def sound(self) -> None:
    print("Meow!")
    
  def move(self) -> None:
    print('Paw paw paw paw...')
  
# Instantiate new animal object
gato: Cat = Cat('Don Gato')
gato.move()
gato.sound()
print(gato.name)




