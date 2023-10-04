//https://medium.com/@kmariappan_tn72/some-modern-javascript-tricks-895c23449615
// 1. AND (&&) ////////////////////////////////////////////////////////////////////////////////////
// The logical AND (&&) operator for a set of boolean operands will be true if and 
//only if all the operands are true. Otherwise it will be false.
/* 
  Example :
    true && true && true //true
    false && true && true //false
*/
// More generally, the operator returns the value of the first falsy.
// and the use case of variables
let a="one",b="two",c="three";

let d = a && b && c;  // "three"

/*In above the case , the first two input should have some values, then only 
I can access the last one, otherwise it will return the falsy value*/

let a = "",b="two",c="three";

let d = a && b && c;  // ""

// 2. OR (||) /////////////////////////////////////////////////////////////////////////////////////
// The logical OR (||) operator for a set of operands is true if and only if one or 
//more of its operands is true. If any of its arguments are true, it returns true, otherwise it returns false.
// Use above-mentioned examples, so that will compare
/* 
  Example:
    1. true || true || true =//true
    2. false || true || true =//true
    3. false || false || false =//false
*/
/**input1*/
let a="one",b="two",c="three";

let d = a || b || c;  // "one"


/**input2*/
let a = "",b="two",c="three"; 

let d = a || b || c;  // "two"


/**input3*/
let a = "",b="",c="";

let d = a || b || c;  // ""


// 3. Dynamic property Name in Object /////////////////////////////////////////////////////////////
// In modern javascript is setting an Object with a dynamic key is simple. using 
//“[‘key’]” can add properties.
var stu_address = 'address';
var student = {
    name:'mick',
    age : 10,
    stu_address : 'chennai'    
    
}
// {name:'mick', age : 10, stu_address : 'chennai'}

/*Using notations you can change the key dynamically*/

var stu_address = 'address';
var student = {
    name:'mick',
    age : 10,
    [stu_address] : 'chennai'    
    
}

//{name: 'mick', age: 10, address: 'chennai'}

// 4. Array to Object , Object to Array ///////////////////////////////////////////////////////////
// In modern javascript world, you can convert array to Object or Object to array is easiest way. I think you know about spread operator, you may used many places , like that we are going to use here
/* 
  Example :
  Array to Object
*/
let arr = [1,2,3,4,5,6,7,8,9]

const convert_obj = {...arr}; 
// {"0": 1, "1": 2, "2": 3, "3": 4, "4": 5, "5": 6, "6": 7, "7": 8, "8": 9,"9": 10}

/* 
  Example :
  Object to Array
  We have 3 types convert Object to array
  1. Object.Keys : using this method, will get a all keys as an array
  2. Object.values: using this method will get all values as an array
  3. Object.entries: will get both key and value in array
*/
let obj = {
  one : 'a',
  two : 'b',
  three : 'c'
};

/*1. Object.keys*/
const keys = Object.keys(obj) //['one', 'two', 'three']

/*2. Object.values*/             
const values = Object.values(obj) // ['a', 'b', 'c']

/*3. Object.entries*/
const entries = Object.entries(obj) // [ ["one", "a"], ["two", "b"], ["three","c"] ]

//5. Destructuring assignment ///////////////////////////////////////////////////////////
// Destructuring assignment is a special syntax that allows us to “unpack” arrays or 
//  objects into a bunch of variables, as sometimes that’s more convenient.
// The destructuring assignment introduced in ES6 makes it easy to assign array values
//  and object properties to distinct variable,most of the people used this feature in
//  javascript frameworks like react, angular.
const student = {
    name : 'mick',
    age : 10,
    gender : 'male'
}

/*Before ES6 : */
 student.name // "mick"
 student.age //10
 student.gender // "male"   

/*From ES6 (using this feature) : */

const {name,age,gender} = student;
 name // "mick"
 age // 10
 gender // "male"

// Note: When destructuring objects, you should use the same name for the variable as
//  the corresponding object key.
const {name1,age,gender} = student;
name1 // undefined
/*if you want to assign different variable names, you can use key and pair*/
const {name : name1,age : age1 , gender: gender2} = student;
name1 // "mick"
/*and you can assign default values */
const {name,age,gender,score=70} = student;
score // 70
// if the keys is not then, the default value will assigned

// In Array :
const num = [11,12,13,14,15,16,17,18,19];
    const [firstElement, secondElement, thirdElement] = num;
    firstElement // 11
    secondElement // 12
    thirdElement // 13
    
// is equivalent to:
const firstElement = num[0];
const secondElement = num[1];

let [a, b, c] = "mick"; // ["m", "i", "c"]

// ADDED: 08/29/23 MORE QUICK TIPS
[69, 420].forEach(alert) // 69, 420 as alerts on webpage

0 == false // true
0 == ''    // true

