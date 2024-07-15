let array = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10];
let object = {
  species: "penguin", 
  type: "bird"
};
let string = "Supercalifragilisticexpialidocious";

// Check if array contains a value
const hasValue = arr => arr.includes(5);
console.log(hasValue(array)); // true

// Scroll to top of the page
window.scrollTo(0,0);

// Deep clone an object
// - make a deep copy of an object w/out referencing the original
const deepClone = obj => JSON.parse(JSON.stringify(obj));
console.log(deepClone(object)); // {species: "penguin", type: "bird"}

// Truncate a string to a specified length
// - if a string exceeds a certain length, you can truncate it and append "..."
const truncate = (str, len) => str.length > len ? str.slice(0, len) + "..." : str;
console.log(truncate(string, 8)) // Supercal...

// Remove duplicate items from an array
// - create a new array w/out repeating values
const deDuplicate = arr => [...new Set(arr)];
console.log(deDuplicate(array)) // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Check if all array items are the same
// - determine if every item in an array is identical
const allIdentical = arr => arr.every(val => val === arr[0]);
console.log(allIdentical(array)); // false

// Get the last item of an array
const lastItem = arr => arr[arr.length - 1];
console.log(lastItem(array)); // 10