/*
                                             |--- img
                                |--- Body ---|--- H1-H6
                                |            |--- p
                                |
Window --- Document --- HTML ---|
                                |
                                |            |--- Title
                                |--- Head ---|
                                             |--- Meta
*/

/*------------------------------ Accessing DOM Elements ------------------------------*/
// 1. By ID
let idElement = document.getElementById('#element-id');
// 2. By Class Name
let classElements = document.getElementsByClassName('.class-name');
// 3. By Tag Name
let tagElements = document.getElementsByTagName('tag-name');
// 4. By CSS Selector
let cssElement1 = document.querySelector('div');
let cssElement2 = document.querySelectorAll('css-selector');
let cssElement3 = document.querySelector('.myClass');
let cssElement4 = document.querySelector('[data-my-attribute]');
let cssElement5 = document.querySelector('div.container > p.first-paragraph');


/*---------------------------- Manipulating DOM Elements ----------------------------*/
// 1. CHANGING CONTENT 
// - modify content of HTML elements using properties like textContent or innerHTML
element.innerHTML = 'New Content';
element.textContent = 'New Text Content';


// 2. MODIFYING ATTRIBUTES
// - JS can change HTML attributes (e.g., src, href, class) dynamically
// - use methods like setAttribute or directly modify the attribute properties
element.setAttribute('attribute-name', 'value');
let value = element.getAttribute('attribute-name');
element.removeAttribute('attribute-name');

element.style.fontSize = '18px';
element.style.backgroundColor = '#ffffff';
element.id = 'myId';
element.classList.add('myClass');
element.classList.remove('myClass');
element.innerText = "Hello World";


// 3. CHANGING STYLES
// - adjust CSS styles using the style property
element.style.propertyName = 'value';


// 4. ADDING/CREATING and REMOVING ELEMENTS:
// - add new HTML elements dynamically using methods like createElement and appendChild
// - remove elements using removeChild
// SYNTAX:
const element = document.createElement('element');
parentElement.appendChild(element);
// EXAMPLES - ADDING/CREATING: 
// A. 
const newParagraph = document.createElement("p");
newParagraph.textContent = "New Content";
parentElement.appendChild(newParagraph);
// B. 
const div = document.createElement('div');
ReportBody.appendChild(div);
// C.
const ul = document.createElement('ul');
const li = document.createElement('li');
ul.appendChild(li);
// EXAMPLES - REMOVING:  
// A.
parent.removeChild(child);
child.remove();
// B.
ul.removeChild(li);
li.remove();


// 5. HANDLING EVENTS
// - to add an event listener to an element, use the addEventListener method
// - this method takes at least two arguments:
//   1. type of event to listen for 2. the function to execute when that event occurs
const myButton = document.getElementById('myButton');
myButton.addEventListener("click", () => {
  // Handle the button click here
})


// 6. QUERYING ELEMENTS
// The querySelector() method returns the first element that matches a css slector
// To return all matches(not only the first), use the querySelectorAll() method
// SYNTAX:
const elementA = document.querySelector('#elementId');
// EXAMPLES:
const classElementsB = document.querySelectorAll('.className');



















