/*  1. Not using STRICT MODE
    enforces stricter rules for certain behaviors
    help avoid common mistakes and ensure code is more secure and performant */
" use strict ";
x = 10;
//  this will cause an error because x is not declared beforehand


//  2. Not using LET and CONST instead of VAR
let x = 1;
let x = 2; 
//  error because x is already declared
const y = {};
y.name = "Tom"; // this is allowed
y = {}; // this will cause  an error because y is a constant


//  3. Not using ARROW FUNCTIONS 
//  traditional function expression
let add = function(a, b) {
    return a + b;
};
// arrow function
let add = (a, b) => a + b;


/*  4. Not using the SPREAD OPERATOR
    expands an array or object into its individual elements
    helps write more concise code by avoiding unecessary loops */
let numbers = [1, 2, 3];
let newNumbers = [0, ...numbers, 4];
console.log(newNumbers); // [0, 1, 2, 3, 4]


/* 5. Not using DESTRUCTURING ASSIGNMENT
    extract values from arrays and ojbects in a more concise and readable way
    more efficient and maintainable code */
let person = {
    name: "Tom",
    age: 25
};
let { name, age } = person;
console.log(name); // Tom
console.log(age); // 25


/* 6. Not using PROMISES
    handle asynchronous operations 
    helps avoid callback hell and chaining async operations */
// Callback
FileSystem.readFile("file.txt", function(err, data) {
    if (err) {
        console.log(err)
    } else {
        console.log(data);
    }
});
// Promise
FileSystem.promises.readFile("file.txt")
    .then(data => {console.log(data)})
    .catch(err => {console.log(err)})

/* 7. Not using === instead of ==
    === Strict Equality compares values without type coercion
    ==  Loose  Equality compares values after type coercion */
console.log(1 == "1"); // true
console.log(1 === "1"); // false


/* 8. Not using FOREACH
    forEach is a higher order function  = iterate array, perform specific operation 
        on each element
    avoid loops and reducing amount of boilerplate code */
// Wrong
let numbers = [1, 2, 3];
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);}
// Right
numbers.forEach(number => console.log(number));