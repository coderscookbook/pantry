/*
GENERAL NOTES:
- MAP() when you want to TRANSFORM each element into something else and get a NEW Array
- FILTER() when you want a NEW array with only elements that meet a certain CONDITION 
- REDUCE() when you want to TRANSFORM an array into a SINGLE VALUE, eg find max value
*/

/*************************************************************************************
Map(): 
  - creates a new array by calling a provided function on each element in the og array
  - does not change the original array
  - returns a new array with the results of the function applied to each element
**************************************************************************************/
// SYNTAX:
// array.map(function(currentValue))
// array.map(function(currentValue, index, arr), thisValue)
// index: optionl | arr: optional | thisValue: optional

// EXAMPLES: 
// Doubling each number in an array
const numbersA = [1, 2, 3, 4, 5];
const doubleNumbers = numbersA.map(num => num*2);
console.log("NumbersA: ", numbersA, "\nDoubleNumbers: ", doubleNumbers);

let numbersPlusOne = numbersA.map((num) => num + 1);

let fruits = ["apple", "banana", "cherry"];
let capitalFruits = fruits.map((fruit) =>
  fruit.toUpperCase()
);


/*************************************************************************************
Filter(): 
  - creates a new array with all elements that pass the test implemented by a function 
  - does not change the original array
  - does not execute the function for empty elements
  - returns a new array with only the elements that meet the condition
**************************************************************************************/
// SYNTAX:
// array.filter(function(currentValue))
// array.filter(function(currentValue, index, arr), thisValue)
// Filtering even numbers from an array
// index: optionl | arr: optional | thisValue: optional

// EXAMPLES: 
const numbersB = [1, 2, 3, 4, 5];
const evenNumbers = numbersB.filter(num => num % 2 === 0);
console.log("NumbersB: ", numbersB, "\nEvenNumbers: ", evenNumbers);

let names = ["Alice", "Ben", "Bob", "David"];

let lengthNames = names.filter(name => 
  name.length === 5);

let ary = [{ name: "John", age: 25}, { name: "Alice", age: 30 }];
let filteredArr = ary.filter(obj => obj.hasOwnProperty("age"));
console.log(filteredArr);


/*************************************************************************************
Reduce(): 
  - applies a function against an accumulator & each element in the array to redude it
    to a single value
  - takes a callback function with an accumulator and current value as arguments and 
    returns a single value
**************************************************************************************/
// SYNTAX:
// array.reduce(callback[, initialValue])
// array.reduce(function(total, currentValue, currentIndex, arr), initialValue)
// total: required | currentValue: required

// Summing all numbers in an array
// Without Initial Accumulator
const numbersC = [1, 2, 3, 4, 5];
const sum = numbersC.reduce((accumulator, currentValue) => 
  accumulator + currentValue, 0);
console.log("NumbersC: ", numbersC, "\nSum: ", sum);
// With Initial Accumulator
const numbersD = [1, 2, 3, 4, 5];
const sum2 = numbersD.reduce((acc, currentValue) => acc + currentValue, 0);
console.log(sum2); // Output: 15

// Max number in array
function maxNum(numArr) {
  return numArr.reduce((max, current) => {
    if (current > max) {
      return current;
    }
    return max;
  }, numArr[0]);
}
const numbersE = [34, 212, 1023, 112, 1930, 1212, 3802, 1143]
let maxNumber = maxNum(numbersE);
console.log(maxNumber);


/*************************************************************************************
Find(): 
  - find() method is used to retrieve teh first element of array that satisfies a 
    condition
  - returns value of first element that matches the condition, or undefined if no value
    satisfies that condition
**************************************************************************************/
const arrayF = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const foundElement = arrayF.find(element => element > 2);
console.log(foundElement);