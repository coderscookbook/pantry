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
// Doubling each number in an array
const numbersA = [1, 2, 3, 4, 5];
const doubleNumbers = numbersA.map(num => num*2);
console.log("NumbersA: ", numbersA, "\nDoubleNumbers: ", doubleNumbers);

/*************************************************************************************
Filter(): 
  - creates a new array with all elements that pass the test implemented by a function 
  - does not change the original array
  - returns a new array with only the elements that meet the condition
**************************************************************************************/
// Filtering even numbers from an array
const numbersB = [1, 2, 3, 4, 5];
const evenNumbers = numbersB.filter(num => num % 2 === 0);
console.log("NumbersB: ", numbersB, "\nEvenNumbers: ", evenNumbers);

/*************************************************************************************
Reduce(): 
  - applies a function against an accumulator & each element in the array to redude it
    to a single value
  - takes a callback function with an accumulator and current value as arguments and 
    returns a single value
**************************************************************************************/
// Summing all numbers in an array
const numbersC = [1, 2, 3, 4, 5];
const sum = numbersC.reduce((accumulator, currentValue) => 
  accumulator + currentValue, 0);
console.log("NumbersC: ", numbersC, "\nSum: ", sum);