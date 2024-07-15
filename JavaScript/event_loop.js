/*
The EVENT LOOP enables asynchronous programming, allowing tasks to be executed
  efficiently without blocking the main thread
  - manages the execution of tasks, callbacks, and events in a single-threaded
    environment
*/

/* 1. Call Stack:
    - JS is single-threaded
    - the call stack is a data structure that keeps track of the execution context
      of functions, ensuring they are executed in the correct order
*/
function foo() {
  console.log("foo");
}
function bar() {
  console.log("bar");
}
foo();
bar();

/* 2. Task Queue:
    - Asynchronous operations such as timers, I/O operations, and event listeners are
      handled asynchronously
    - when an async operation completes, its callback is pushed into the task queue
*/
setTimeout(() => {
  console.log("Async Operation");
}, 1000)

/* 3. Event Loop:
    - the event loop continusouly checks the call stack and queue
    - if the call stack is empty, the event loop takes the first callback from the
      task queue and pushes it onto the call stack for execution
*/
console.log("Start");
setTimeoutB(() => {
  console.log("Async Operation B");
}, 0);
console.log("End");

/* 4. Execution:
    - the callback from the task queue is executed, and its associated code runs
    - this process repeats, allowing async operations to be handled w/out blocking the
      main thread
    - Output from above:
      Start
      End
      Async Operation B //after a short delay
*/
