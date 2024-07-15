/*
EVENTS are the changes in state when a specific action takes place
- either by user interaction or system operation
*/

/* EXAMPLE:
- clicking on button directs you to next page
- form data sent to server by clicking on submit*/
/* CSS:
.container {
  width:650px;
  height:650px;
  background-color:rgb(25, 15, 30);
}
.box {
  width:300px;
  height:300px;
  background-color:#13352b;
}
*/

/* HTML:
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="src/style.css">
  </head>
  <body>
  <div class="container">
    <div class="box">
    </div>
  </div>
  <script src="src/script.js"></script>
</body>
</html>
*/

// JS:
document.querySelector(".box").addEventListener("dblclick", () => {
  document.querySelector(".box").innerHTML = "Clicked"
});


/* EVENT BUBBLING:
    - if you listen to an event on any element, then its listener will
      be activated and its parent will also be activated because, technically,
      if you clicked on a child, you also clicked on its parent */
/* EXAMPLE:
    - if you click on inner box then you will see "child" as well as "parent"
      in the console screen
    - but if you click on outer box then you will see only "parent" written
      in the console
    - this is what event bubbling does */
document.querySelector(".box").addEventListener('click', () => {
  console.log("child");
}); //Output === child|parent
document.querySelector(".container").addEventListener('click', () => {
  console.log("parent");
}); //Output === parent


/* .STOPPROPAGATION()
    - if we don't want by default action, we can stop this by passing an
      argument ('e') inside the function and write stopPropagation()
    - only write function in the child (in this example)
      - now when inner box is clicked, console will only show 'child' and 'parent'
        will only show when the outer container is clicked */
document.querySelector(".box").addEventListener('click', (e) => {
  e.stopPropagation();
  console.log("child");
}); 
document.querySelector(".container").addEventListener('click', () => {
  console.log("parent");
}); 


/* TIMING BASED EVENTS
    - events which execute over a period of time or scheduled to happen after
      a certain duration
    - it includes two main functions: setInterval and setTimeout */
// setInterval() runs a function for every given interval of time
// - infinite
let x = 0
setInterval(() => {
  console.log(`${x}`);
  x += 1;
}, 1000)
// - stopped with clearInterval()
let a = 1;                            // number of times function will run
let acc = setInterval(() => {
  if (a <= 5) {                       // condition checking
    console.log(`${a}`);
  } 
  else {                              // when the value of 'a' becomes greater than 5
    clearInterval(acc);               // used to terminate the setInterval()
    console.log("Fin");
  }
  a++;                                // increment
}, 1000);
// setTimeout() - runs a function after a certain period of time (only once)
setTimeout(() => {
  console.log("Done")
}, 3000);
// OUTPUT: 1 2 3 DONE 4 5 FIN