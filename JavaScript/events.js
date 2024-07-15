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
