/*
Spread Operator (...)
  - allows to expand an iterable object (eg array, string, object) into individual elements
  - commonly used in function calls, array literals & object literals
  - creates a SHALLOW COPY of an object or array
    -- Shallow Copy = while top-level elements are copied, nested objects or arrays within
        the spread may still be referenced instead of deeply copied
    -- To create a deep copy, use other techniques suc as recursion or external libraries
*/

//Example 1. Array Cocatenation
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]
const concat = [...array1, ...array2]
console.log(concat)

//Example 2. Array Copy
const original = [1, 2, 3];
const copy = [...original];
console.log(copy)

//Example 3. Ojbect Copy
const original2 = { name: "John", age: 25 };
const copy2 = { ...original2}
console.log(copy2)

//Example 4. Object Merging
const obj1 = { a: 1 };
const obj2 = { b: 2 };
const merged = {...obj1, ...obj2};
console.log(merged)

//Example 5. Function Arguments
function addNumbers(a, b, c){
  return a + b + c;
}
const numbers = [1, 2, 3, 4, 5, 6]
const sum = addNumbers(...numbers);
console.log(sum)

