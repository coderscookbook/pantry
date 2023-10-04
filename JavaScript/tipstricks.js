// 1. Number separator*****************************************************************************
// To improve the readability of numbers, you can use underscores as separators.
const largeNumber = 1_000_000_000;
console.log(largeNumber); // 1000000000

// 2. Event listeners run only once****************************************************************
// If you want to add an event listener and run it only once, you can use the once option.
element.addEventListener('click', () => console.log('I run only once'), {
    once: true
});   

// 3. console.log Variable wrapper*****************************************************************
// In console.log(), enclose the arguments in curly braces so that you can see both the variable name and the variable value.
    const name = "Maxwell";
    console.log({ name });

// 4. Check that Caps Lock is on*******************************************************************
// You can use KeyboardEvent.getModifierState() to detect if Caps Lock is on.
const passwordInput = document.getElementById('password');
passwordInput.addEventListener('keyup', function (event) {
    if (event.getModifierState('CapsLock')) {
        // CapsLock is open
    }
});           

// 5. Get min/max values from an array*************************************************************
// You can use Math.min() or Math.max() in combination with the extension operator to find the minimum or maximum value in an array.
const numbers = [5, 7, 1, 4, 9];
console.log(Math.max(...numbers)); // 9
console.log(Math.min(...numbers)); // 1   

// 6. Get the mouse position***********************************************************************
// You can use the values of the clientX and clientY properties of the MouseEvent object to get information about the coordinates of the current mouse position.
document.addEventListener('mousemove', (e) => {
    console.log(`Mouse X: ${e.clientX}, Mouse Y: ${e.clientY}`);
});  

// 7. Copy to clipboard****************************************************************************
// You can use the Clipboard API to create a “Copy to Clipboard” function.
function copyToClipboard(text) {
    navigator.clipboard.writeText(text);
}           

// 8. Write conditional judgment statements in short***********************************************
// If the function is executed only when the condition is true, you can use the && shorthand.
// Common writing method
if (condition) {
    doSomething();
}
// Abbreviations
condition && doSomething();           

// 9. console.table() prints a table in a specific format******************************************
// Grammar:
console.table(data [, columns]);
// Parameters:
// data Indicates the data to be displayed. It must be an array or an object.
// columns Represents an array containing the names of the columns.
   function Person(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
    const p1 = new Person("Mark", "Smith");
    const p2 = new Person("Maxwell", "Siegrist");
    const p3 = new Person("Lucy", "Jones");
    console.table([p1, p2, p3], ["firstName"]);

// 10. Converting strings to numbers***************************************************************
const str = '508';
console.log(+str) // 508;           

// 11. Array de-duplication************************************************************************
const numbers = [2, 3, 5, 5, 2];
console.log([...new Set(numbers)]); // [2, 3, 5]  

// 12. Filter all dummy values from the array******************************************************
const myArray = [1, undefined, NaN, 2, null, '@maxwell', true, 5, false];
console.log(myArray.filter(Boolean)); // [1, 2, "@maxwell", true, 5]

// 13. Great uses include**************************************************************************
const myTech = 'JavaScript';
const techs = ['HTML', 'CSS', 'JavaScript'];
// Common writing method
if (myTech === 'HTML' || myTech === 'CSS' || myTech === 'JavaScript') {
    // do something
}
// includes writing method
if (techs.includes(myTech)) {
    // do something 
} 
          
// 14. Great use of reduce to sum arrays***********************************************************
const myArray = [10, 20, 30, 40];
const reducer = (total, currentValue) => total + currentValue;
console.log(myArray.reduce(reducer)); // 100  

// 15. element’s dataset***************************************************************************
// Use the dataset attribute to access the element’s custom data attributes (data-*).
<div id="user" data-name="Maxwell" data-age="32" data-something="Some Data">
    Hello Maxwell
</div>

<script>
    const user = document.getElementById('user');
  
    console.log(user.dataset); 
    // { name: "Maxwell", age: "32", something: "Some Data" }
  
    console.log(user.dataset.name); // "Maxwell"
    console.log(user.dataset.age); // "32"
    console.log(user.dataset.something); // "Some Data"
</script>     

//-------------------------------------------------------------------------------------------------------------------------------
//USE OPTIONAL CHAINING OPERATOR (?)************************************************************************
const user={
    name: "Max",
    address: {
        city: 'Biloxi'
    }
}
//bad
const response = user
                    && user.address
                    && user.address.city;
//better
const data = user?.address?.city;

//IF w/MULTIPLE CONDITIONS************************************************************************
const isValidUser = (type) => {
    if(type === 'Admin'
        || type === 'Employee'
        || type === 'Customer'){
            return true;
        } else {
            return false;
        }
}
//shorter
const isValidUser = (type) =>
    ['Admin', 'Employee', 'Customer'].includes(type);

//DESTRUCTURING ASSIGNMENT************************************************************************
const user ={
    firstName: 'Sumit',
    lastName: 'Sharma'
};
//bad
const fName = user.firstName;
const lName = user.lastName;
//better
const {firstName, lastName} = user

//OBJECT PROPERTY ASSIGNMENT************************************************************************
const firstName = "Sumit"
const lastName = "Sharma"
//bad
const user1 = {
    firstName: firstName,
    lastName: lastName
}  
//better
const user2 = {firstName, lastName}

//SIMPLIFY THE CONDITION************************************************************************
const age= 10;
let isEligibleForVoting;
//bad
if(age >= 18){
    isEligibleForVoting = true;
} else {
    isEligibleForVoting = false;
}
//better
isEligibleForVoting = age>=18 ? true:false;
//best
isEligibleForVoting = age>=18;