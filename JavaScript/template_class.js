// Define a class named `Person`
class Person {
  // The constructor method is called when a new object is created
  constructor(name, age) {
    // Initialize the properties of the class
    this.name = name;
    this.age = age;
  }

  // A method (function) that is part of the class
  introduceYourself() {
    console.log(`Hi, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

// Create an object (instance) of the Person class
const person1 = new Person("Alice", 30);

// Access the properties and methods of the person1 object
console.log(person1.name); // Output: Alice
console.log(person1.age);  // Output: 30

// Call the introduceYourself method
person1.introduceYourself(); // Output: Hi, my name is Alice and I am 30 years old.
