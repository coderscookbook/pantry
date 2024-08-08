'''
@staticmethod
- this decorator only works in classes

'''

# Pretend we are a calculator factory that produces calculators

class Calculator:
  def __init__(self, name: str, version: int) -> None:
    self.name = name
    self.version = version

  def get_calculator_info(self) -> str:
    return f'{self.name} V.{self.version}'
  
  # "*" allows us to input as many arguments as we want (aka: *args) 
  # This method may give syntax highlighting: method may be static
  # - method will work perfectly fine outside of the class
  # - add @staticmethod to tell code editor to only use inside class
  # - means you don't have to instantiate a Calculator to use the method
  @staticmethod
  # def add_all(self, *numbers: int) -> int:  # normal declaration
  def add_all(*numbers: int) -> int:    # declaration using @staticmethod
    return sum(numbers)
    
# Create Calculator instance
calc: Calculator = Calculator(name="CC's Calculator", version=1)
print(calc.get_calculator_info())   # Output: CC's Calculator V.1
print(calc.add_all(1,2,3,4))        # Output: 10     
print(Calculator.add_all(1,2,3,4))  # Output: 10 
print(Calculator.get_calculator_info()) # Output: Exception (no self = instance)