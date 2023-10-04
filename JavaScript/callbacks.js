//show message after 3 seconds
const message = function () {
  console.log("Show this message after 3 seconds")
}
//setTimeout using message() as a parameter = callback
setTimeout(
  message, 
  3000
);

//CALLBACKS as ANONYMOUS FUNCTIONS
/*define function inside another function, instead of
defining it somewhere else -- no name required
= more concise code */

setTimeout(
  function(){
    console.log("Show this message after 3 seconds");
  }, 
  3000
);

//CALLBACKS as ES6 ARROW FUNCTIONS
setTimeout (
  () => {
    console.log("Show this message after 3 seconds");
  }, 
  3000
);

//ONE LINER ARROW FUNCTION
setTimeout(() => console.log("Show this message after 3 seconds"), 3000);

//************************EVENTS********************************
/*used to respond to web page events such as clicking a button, 
hovering over an element, or submitting a form */
//ie: <button id="callback-btn">CLICK HERE</button>
//we want to log a message when the user clicks on the button
document.querySelector("#callback-btn")
  .addEventListener("click", function(){
    console.log("User has clicked on the button!");
})