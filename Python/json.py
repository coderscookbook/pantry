import json

##############################################################################
# This approach is safer than using 'eval()' because JSON serialization and 
#   deserialization do not execute arbitrary code
# - note: not all objects can be directly serialized to JSON (see: jsonpickle)
##############################################################################
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age  = age

  def to_dict(self):
    return {"name": self.name, "age": self.age}

  @classmethod
  def from_dict(cls, data):
    return cls(data["name"], data["age"])

# Create a Person object
person = Person("Alice", 30)

# Serialize the object to a JSON string
json_string = json.dumps(person.to_dict())

# Store or transmit the JSON string as needed
print("Serialized JSON string: ", json_string)

# Deserialize the JSON string back into an object
decoded_person = Person.from_dict(json.loads(json_string))

# Verify the deserialized object
print("Deserialized object: ", decoded_person.name, decoded_person.age)

