//Source: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice
//SYNTAX:
splice(start)
splice(start, deleteCount)
splice(start, deleteCount, item1)
splice(start, deleteCount, item1, item2)
splice(start, deleteCount, item1, item2, /* ..., */ itemN)

/* 
start = zero-based index at which to start changing the array, converted to integer
        - neg integer counts back from end of array
*/

// EXAMPLES:
const months = ['Jan', 'March', 'April', 'June'];
months.splice(1, 0, 'Feb');
// Inserts at index 1
console.log(months);
// Expected output: Array ["Jan", "Feb", "March", "April", "June"]

months.splice(4, 1, 'May');
// Replaces 1 element at index 4
console.log(months);
// Expected output: Array ["Jan", "Feb", "March", "April", "May"]

months.splice('June', 4, 1)

// Remove 0(zero) elements before index 2, and insert "drum" and "guitar"
const myFish = ["angel", "clown", "mandarin", "sturgeon"];
const removed = myFish.splice(2, 0, "drum");
// myFish is ["angel", "clown", "drum", "mandarin", "sturgeon"]
// removed is [], no elements removed

// Remove 0 elements at index 0, and insert "angel"
const myFish2 = ["angel", "clown", "mandarin", "sturgeon"];
const removed2 = myFish2.splice(2, 0, "drum", "guitar");
// myFish is ["angel", "clown", "drum", "guitar", "mandarin", "sturgeon"]
// removed is [], no elements removed

// MORE EXAMPLES ON WEBSITE
