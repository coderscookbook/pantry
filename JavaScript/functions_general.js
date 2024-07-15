// 1. Named: traditional way
function myFunction() {
  console.log("Aloha")
};
myFunction();

// 2. Anonymous
let greet = function(name) {
  console.log(`Aloha, ${name}!`)
};
greet("Pua")

// 3. Arrow
let greeting = () => console.log("Aloha, Pua Okole!");
greeting();
let greetingB = name => console.log(`Aloha, ${name}!`);
greetingB("Kala Poke");

// 4. Immediately Invoked Function Expressions (IIFE)
// - executed immediately after their creation
// - used to create private scopes and avoid polluting the global namespace
(function () {
  let str = "Good Evening";
  console.log(str);
})();

// 5. Higher Order Functions


// 6. Constructor