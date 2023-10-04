//OBJECTS-----------------------------------------------------------------------------
/*an object is a collection of properties, where each property is a key-value pair. 
The keys are strings that represent the names of the properties, and the values can be 
of any data type, including other objects*/
const person = {
  //props
  name: 'Brendan Eich',
  age: 60,
  address: {
    street: '123 JavaScript Street',
    city: 'Web',
    state: 'Programming',
    zip: '12345'
  }
};

/*
console.log(person.name); // Output: 'Brendan Eich'
console.log(person['age']); // Output: 60
console.log(person.address.city); // Output: 'Web'
*/

//CLASSES-----------------------------------------------------------------------------
/*blueprint for creating objects. It defines the properties and methods that objects 
of that class will have*/
class Person {
  //constructor initializes two properties
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  //define methods
  greet() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}
  //initializing new object of type 'Person' 
  const homie = new Person('Brendan Eich', 60);
  homie.greet(); // Output: 'Hello, my name is Brendan Eich and I am 60 years old.'

//INHERITANCE-------------------------------------------------------------------------
/*the process of creating a new class based on an existing class. The new class, known
 as the subclass, inherits the properties and methods of the existing class, known as 
 the superclass*/
class Student extends Person {
  constructor(name, age, grade) {
    super(name, age);
    this.grade = grade;
  }

  study() {
    console.log(`${this.name} is a ${this.grade} in JavaScript.`);
  }
}

  //initializing new object of type 'Student' 
  const student = new Student('Sumit', 38, 'beginner');
  student.greet(); // Output: 'Hello, my name is Sumit and I am 38 years old.'
  student.study(); // Output: 'Sumit is a beginner in JavaScript.'

//ENCAPSULATION-----------------------------------------------------------------------
/*the practice of hiding the internal details of an object and providing a public 
interface for interacting with it. This helps to prevent outside code from directly 
modifying the internal state of an object, which can lead to bugs and other issues. 
In JavaScript, we can use closures to achieve encapsulation*/
function createCounter() {
  let count = 0;

  return {
    increment() {
      count++;
    },

    decrement() {
      count--;
    },

    getCount() {
      return count;
    }
  };
}

const counter = createCounter();
console.log(counter.getCount()); // Output: 0
counter.increment();
console.log(counter.getCount()); // Output: 1
counter.decrement();
console.log(counter.getCount()); // Output: 0

//POLYMORPHISM------------------------------------------------------------------------
/*the ability of objects of different classes to be treated as if they were objects of 
the same class. In JavaScript, we can achieve polymorphism using interfaces*/

class Shape {
  draw() {
    console.log('Drawing shape...');
  }
}

class Circle extends Shape {
  draw() {
    console.log('Drawing circle...');
  }
}

class Square extends Shape {
  draw() {
    console.log('Drawing square...');
  }
}

function drawShapes(shapes) {
  shapes.forEach(shape => {
    shape.draw();
  });
}

const shapes = [
  new Circle(),
  new Square(),
  new Circle(),
  new Square()
];

drawShapes(shapes);

// FINAL EXAMPLE USING ALL CONCEPTS ABOVE---------------------------------------------
/*define a base class called Animal*/
class Animal {
  constructor(name) {
    this.name = name;
  }

  eat() {
    console.log(`${this.name} is eating.`);
  }

  sleep() {
    console.log(`${this.name} is sleeping.`);
  }
}

// define a subclass called Cat that inherits from Animal
class Cat extends Animal {
  constructor(name) {
    super(name);
  }

  meow() {
    console.log(`${this.name} says meow.`);
  }

  // override the sleep method of Animal
  sleep() {
    console.log(`${this.name} is taking a cat nap.`);
  }
}

// define another subclass called Dog that also inherits from Animal
class Dog extends Animal {
  constructor(name) {
    super(name);
  }

  bark() {
    console.log(`${this.name} says woof.`);
  }

  // override the eat method of Animal
  eat() {
    console.log(`${this.name} is eating from a bowl.`);
  }
}

// create an array of animals
let animals = [
  new Cat("Mumu"),
  new Dog("Laltu"),
  new Cat("Miaow"),
  new Dog("Boltu")
];

// loop through the array and call methods on each animal
for (let animal of animals) {
  animal.eat();
  animal.sleep();

  // check if the animal is a cat and call the meow method if it is
  if (animal instanceof Cat) {
    animal.meow();
  }

  // check if the animal is a dog and call the bark method if it is
  if (animal instanceof Dog) {
    animal.bark();
  }
}

//source: https://sayhitosumit.medium.com/object-oriented-programming-oop-in-javascript-a264c4342d1c