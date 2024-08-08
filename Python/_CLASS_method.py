from typing import Self

# Part 1:
class Car:
  # class attribute
  # created directly inside class, not initializer
  total_cars: int = 0

  def __init__(self, brand: str, top_speed: int) -> None:
    self.brand = brand
    self.top_speed = top_speed
    # Refer directly to class
    Car.total_cars += 1
    
# Examples
bmw: Car = Car(brand="BMW", top_speed=250)
print(Car.total_cars)   # Output: 1
volvo: Car = Car(brand="Volvo", top_speed=190)
print(Car.total_cars)   # Output: 2

# Wrong:
bmw.total_cars = 100
print(bmw.total_cars)
Car.total_cars = 200
print(Car.total_cars) # affects all instances equally
print(volvo.total_cars) # Output: 200


# Part 2:
class Car:
  total_cars: int = 0

  def __init__(self, brand: str, top_speed: int) -> None:
    self.brand = brand
    self.top_speed = top_speed
    Car.total_cars += 1
  
  # alternative constructor
  # Belong to the class, not the instance created
  @classmethod
  def auto_top_speed(cls, brand: str) -> Self:
    database: dict[str, int] = {'bmw': 300, 'volvo': 400}
    top_speed: int | None = database.get(brand.lower())
    
    if top_speed:
      print(f"Setting top speed to: {top_speed}.")
    else:
      print(f'Could not find: "{brand}" in our databse. Using default of 200')
      top_speed = 200
      
    return cls(brand=brand, top_speed=top_speed)
  
  def __str__(self) -> str:
    return f'{self.brand} ({self.top_speed}km/h)'
  
  @classmethod
  def total_cars_created(cls) -> int:
    # refers to class attribute at the top, not inside initializer
    return cls.total_cars

# Examples
bmw: Car = Car.auto_top_speed('BMW')
print(bmw)
volvo: Car = Car.auto_top_speed('Volvo')
print(volvo)
mercedes: Car = Car.auto_top_speed('Subaru')
print(mercedes)

print(Car.total_cars_created())