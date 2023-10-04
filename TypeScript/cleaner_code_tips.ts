//https://medium.com/@mvsg/12-typescript-tricks-for-clean-code-b23651dd0430

/*1 - Use Type Annotation: ype annotations can help catch errors early in the development
process and improve code readability*/
// Explicitly specify the data type of a variable
let count: number = 0;

// Explicitly specify the data type of a function parameter and return value
function addNumbers(a: number, b: number): number {
  return a + b;
}

// Explicitly specify the data type of a class property
class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  getDetails(): string {
    return `${this.name} is ${this.age} years old.`;
  }
}

/*2 — Use Enums: Enums are a powerful feature of TypeScript that allows you to define 
a set of named constants. They can help make your code more readable and maintainable, 
as well as reduce the likelihood of errors caused by magic numbers.*/
//define an enum called Color that contains three named constants: Red, Green, and Blue. 
// Each constant has an associated value, which can be a string or a number. We then define
//   a function called printColor that takes a Color parameter and logs a message to the 
//   console using the parameter value.
// When we call the printColor function with the Color.Red constant as the parameter, 
//   it logs the message "The color is RED" to the console.

enum Color {
  Red = "RED",
  Green = "GREEN",
  Blue = "BLUE"
}

function printColor(color: Color): void {
  console.log(`The color is ${color}`);
}

printColor(Color.Red); // output: The color is RED

// 3 — Use Optional Chaining: Optional chaining is a TypeScript feature that allows you to safely access nested properties and methods without worrying about whether the intermediate values are null or undefined. This can help reduce the likelihood of runtime errors and make your code more robust.

// Here’s an example of how optional chaining can be used in TypeScript:

interface Person {
  name: string;
  address?: {
    street: string;
    city: string;
    state: string;
  };
}

const person1: Person = {
  name: "John",
  address: {
    street: "123 Main St",
    city: "Anytown",
    state: "CA",
  },
};

const person2: Person = {
  name: "Jane",
};

console.log(person1?.address?.city); // output: Anytown
console.log(person2?.address?.city); // output: undefined
// In this example, we have an interface called Person that defines an optional address property, which is an object with street, city, and state properties. We then create two objects of type Person, one with an address property and one without.

// We use optional chaining to safely access the city property of the address object, even if the address property or any of its sub-properties are undefined or null. If any of the properties in the chain are undefined or null, the expression will return undefined instead of throwing a TypeError.

// 4 — Use Nullish Coalescing: Nullish coalescing is another TypeScript feature that can help make your code more robust. It allows you to provide a default value for a variable or expression when it is null or undefined, without relying on falsy values.

// Here’s an example of how nullish coalescing can be used in TypeScript:

let value1: string | null = null;
let value2: string | undefined = undefined;
let value3: string | null | undefined = "hello";

console.log(value1 ?? "default value"); // output: "default value"
console.log(value2 ?? "default value"); // output: "default value"
console.log(value3 ?? "default value"); // output: "hello"
// In this example, we have three variables that may contain null or undefined values. We use the nullish coalescing operator (??) to check if the values are nullish (either null or undefined) and provide a default value in that case.

// In the first two cases, the variables value1 and value2 are null or undefined, respectively, so the default value is returned. In the third case, the variable value3 contains a non-null/non-undefined value, so that value is returned instead of the default value.

// 5 — Use Generics: Generics are a powerful feature of TypeScript that allows you to write reusable code that works with different types. They can help reduce code duplication and improve code maintainability.

// Here’s an example of how generics can be used in TypeScript:

function identity<T>(arg: T): T {
  return arg;
}

let output1 = identity<string>("hello"); // output: "hello"
let output2 = identity<number>(42); // output: 42
// In this example, we define a function called identity that takes a type parameter T and returns the same type of value that was passed in. The function can work with any type of data, and the actual data type is specified when the function is called.

// We then call the identity function with two different data types: a string and a number. The function returns the same type of value that was passed in, so output1 is of type string and output2 is of type number.

// 6 — Use Interfaces: Interfaces are another powerful feature of TypeScript that can help you write clean and readable code. They allow you to define a contract for a class, object, or function, which can help you avoid common errors and make your code more self-documenting.

// Here’s an example of how interfaces can be used in TypeScript:

interface Person {
  firstName: string;
  lastName: string;
  age?: number;
}

function sayHello(person: Person): void {
  console.log(`Hello, ${person.firstName} ${person.lastName}!`);
  if (person.age) {
    console.log(`You are ${person.age} years old.`);
  }
}

let person1 = { firstName: "John", lastName: "Doe", age: 30 };
let person2 = { firstName: "Jane", lastName: "Doe" };

sayHello(person1); // output: "Hello, John Doe! You are 30 years old."
sayHello(person2); // output: "Hello, Jane Doe!"
// In this example, we define an interface called Person that specifies the shape of a person object, including a firstName and lastName property and an optional age property. We then define a function called sayHello that takes a Person object as an argument and prints a greeting to the console.

// We create two objects that match the shape of the Person interface, and pass them into the sayHello function. The function is able to access the firstName and lastName properties of each object, and also check whether the age property exists before printing it to the console.

// 7 — Use Destructuring: Destructuring is a shorthand syntax that allows you to extract values from arrays and objects. It can help make your code more readable and concise, as well as reduce the likelihood of errors caused by misaligning variable names.

// Here are some examples of how destructuring can be used in TypeScript:

// Object destructuring:

let person = { firstName: "John", lastName: "Doe", age: 30 };

let { firstName, lastName } = person;

console.log(firstName); // output: "John"
console.log(lastName); // output: "Doe"
// In this example, we create an object called person with three properties. We then use object destructuring to extract the firstName and lastName properties and assign them to variables of the same name. This allows us to access these properties more easily and with less code.

// Array destructuring:

let numbers = [1, 2, 3, 4, 5];

let [first, second, , fourth] = numbers;

console.log(first); // output: 1
console.log(second); // output: 2
console.log(fourth); // output: 4
// In this example, we create an array of numbers and use array destructuring to extract the first, second, and fourth elements and assign them to variables. We skip the third element using an empty slot in the destructuring pattern. This allows us to access specific elements of an array more easily and with less code.

// Destructuring can also be used with function parameters, allowing you to extract specific values from an object passed as an argument:

function greet({ firstName, lastName }: { firstName: string, lastName: string }): void {
  console.log(`Hello, ${firstName} ${lastName}!`);
}

let person = { firstName: "John", lastName: "Doe", age: 30 };

greet(person); // output: "Hello, John Doe!"
// In this example, we define a function called greet that takes an object with firstName and lastName properties as an argument using destructuring syntax in the function parameter. We then pass in a person object and the greet function is able to extract the firstName and lastName properties and use them in the console log statement.

// 8 — Use Async/Await: Async/await is a powerful feature of TypeScript that allows you to write asynchronous code that looks and behaves like synchronous code. It can help improve code readability and reduce the likelihood of errors caused by callback hell.

// Here is an example of how async/await can be used in TypeScript:

async function getData() {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  return data;
}

getData().then((data) => {
  console.log(data);
}).catch((error) => {
  console.error(error);
});
// In this example, we define an async function called getData that makes a fetch request to an API and waits for the response using the await keyword. We then parse the response using the json() method and again wait for the result using await. Finally, we return the data object.

// We then call the getData() function and use the then() method to handle the returned data, or the catch() method to handle any errors that may occur.

// 9 — Use Functional Programming Techniques: Functional programming techniques, such as immutability, pure functions, and higher-order functions, can help you write clean and maintainable code. They can help reduce side effects and make your code more predictable and testable.

// Pure functions: A pure function is a function that has no side effects and always returns the same output given the same input. Pure functions make it easier to reason about code and can help prevent bugs. Here’s an example of a pure function:

function add(a: number, b: number): number {
  return a + b;
}
// Higher-order functions: A higher-order function is a function that takes one or more functions as arguments or returns a function as its result. Higher-order functions can be used to create reusable code and simplify complex logic. Here’s an example of a higher-order function:

function map<T, U>(arr: T[], fn: (arg: T) => U): U[] {
  const result = [];
  for (const item of arr) {
    result.push(fn(item));
  }
  return result;
}

const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = map(numbers, (n) => n * 2);
console.log(doubledNumbers); // Output: [2, 4, 6, 8, 10]
// In this example, the map function takes an array and a function as arguments, and applies the function to each element in the array, returning a new array with the results.

// Immutable data: Immutable data is data that cannot be changed after it is created. In functional programming, immutability is emphasized to prevent side effects and make code easier to reason about. Here’s an example of using immutable data:

const numbers = [1, 2, 3, 4, 5];
const newNumbers = [...numbers, 6];
console.log(numbers); // Output: [1, 2, 3, 4, 5]
console.log(newNumbers); // Output: [1, 2, 3, 4, 5, 6]
// In this example, we use the spread operator to create a new array with a new element appended to the end, without modifying the original array.

// 10 — Use Pick Helper: The Pick helper is a TypeScript utility type that allows us to create new types from existing types, making it easier to reuse and maintain code. It also helps to prevent errors by ensuring that the new type only includes the properties we intend to use.

// Here’s an example:

interface User {
  name: string;
  email: string;
  age: number;
  isAdmin: boolean;
}

type UserSummary = Pick<User, 'name' | 'email'>;

const user: User = {
  name: 'John Doe',
  email: 'johndoe@example.com',
  age: 30,
  isAdmin: false,
};

const summary: UserSummary = {
  name: user.name,
  email: user.email,
};

console.log(summary); // Output: { name: 'John Doe', email: 'johndoe@example.com' }
// In this example, we define an interface User with several properties. We then define a new type UserSummary using the Pick utility type, which selects only the name and email properties from the User interface.

// We then create an object user with all the properties of the User interface, and use the name and email properties to create a new object summary of type UserSummary.

// 11 — Use Omit Helper: The Omit helper is a TypeScript utility type that allows us to create new types from existing types, while ensuring that certain properties are excluded. This can be helpful when working with complex interfaces where certain properties may not be needed in certain situations. It can also help prevent errors by ensuring that certain properties are not accidentally included.

// Here’s an example:

interface User {
  name: string;
  email: string;
  age: number;
  isAdmin: boolean;
}

type UserWithoutEmail = Omit<User, 'email'>;

const user: User = {
  name: 'John Doe',
  email: 'johndoe@example.com',
  age: 30,
  isAdmin: false,
};

const userWithoutEmail: UserWithoutEmail = {
  name: user.name,
  age: user.age,
  isAdmin: user.isAdmin,
};

console.log(userWithoutEmail); // Output: { name: 'John Doe', age: 30, isAdmin: false }
// In this example, we define an interface User with several properties. We then define a new type UserWithoutEmail using the Omit utility type, which omits the email property from the User interface.

// We then create an object user with all the properties of the User interface, and use the name, age, and isAdmin properties to create a new object userWithoutEmail of type UserWithoutEmail.

// 12 — Use Discriminated Unions: Discriminated unions are a TypeScript feature that allows us to model types that can take on different shapes based on a specific property or combination of properties, and handle them in a type-safe manner using switch statements. It is a powerful feature of TypeScript that can make your code more expressive and maintainable.

// Here’s an example:

interface Square {
  kind: 'square';
  size: number;
}

interface Circle {
  kind: 'circle';
  radius: number;
}

interface Triangle {
  kind: 'triangle';
  base: number;
  height: number;
}

type Shape = Square | Circle | Triangle;

function area(shape: Shape) {
  switch (shape.kind) {
    case 'square':
      return shape.size * shape.size;
    case 'circle':
      return Math.PI * shape.radius * shape.radius;
    case 'triangle':
      return 0.5 * shape.base * shape.height;
  }
}

const square: Square = { kind: 'square', size: 10 };
const circle: Circle = { kind: 'circle', radius: 5 };
const triangle: Triangle = { kind: 'triangle', base: 10, height: 8 };

console.log(area(square)); // Output: 100
console.log(area(circle)); // Output: 78.53981633974483
console.log(area(triangle)); // Output: 40
// In this example, we define three interfaces Square, Circle, and Triangle, each representing a different shape. We then define a union type Shape that can be either a Square, a Circle, or a Triangle.

// We define a function area that takes a shape of type Shape as an argument and uses a switch statement to calculate the area of the shape based on its kind. The kind property is used as the discriminating property, as it uniquely identifies each type of shape.

// We then create three objects, one for each type of shape, and call the area function with each object as an argument to calculate the area.

// In conclusion, these TypeScript tricks for writing clean code can help you write more expressive, maintainable, and error-free code. By using type annotations, enums, optional chaining, nullish coalescing, generics, interfaces, destructuring, async/await, functional programming techniques, and various helper types like Pick, Omit, and discriminated unions, you can create more robust and scalable TypeScript applications.