// To use ts scripts: run 'tsc <filename>', then a .js file is created, run 'node <filename>' 

// 1. Using 'let' for variables whose value can change.
let message: string = "Hello, TypeScript!"; // Explicitly typed as string and initialized.
console.log("1. Using 'let':", message);

message = "Hello again!"; // Value can be reassigned.
console.log("   Reassigned 'let':", message);

let count: number; // Declared with type but not initialized.
count = 10;
console.log("   Declared 'let' without initial value:", count);

// 2. Using 'const' for variables whose value should not change after initialization.
const pi: number = 3.14159; // Explicitly typed as number and initialized.
console.log("2. Using 'const':", pi);

// pi = 3.14; // This would cause a compile-time error because 'pi' is a constant.
// console.log("   Attempting to reassign 'const':", pi); // This line will not be reached due to the error.

const greeting = "Hi there!"; // Type is inferred as string.
console.log("   Inferred type 'const':", greeting);

// 3. Type Inference: TypeScript can often infer the type based on the initial value.
let isTrue = true; // TypeScript infers the type as boolean.
console.log("3. Type Inference (boolean):", isTrue);

let price = 9.99; // TypeScript infers the type as number.
console.log("   Type Inference (number):", price);

// 4. Specifying types explicitly (recommended for clarity).
let name2: string;
name2 = "Bob";
console.log("4. Explicit type (string):", name2);

let age: number;
age = 25;
console.log("   Explicit type (number):", age);

let isValid: boolean;
isValid = false;
console.log("   Explicit type (boolean):", isValid);

// 5. Using 'any' (use with caution as it bypasses type checking).
let anything: any = "Can be anything";
console.log("5. Using 'any':", anything);
anything = 123;
console.log("   'any' can hold a number:", anything);
anything = true;
console.log("   'any' can hold a boolean:", anything);

// 6. Using 'unknown' (safer than 'any' as you need to check the type before using it).
let maybeNumber: unknown = 42;
console.log("6. Using 'unknown':", maybeNumber);
if (typeof maybeNumber === 'number') {
  let result: number = maybeNumber * 2;
  console.log("   Using 'unknown' after type check:", result);
}

// 7. Array declarations.
let numbers1: number[] = [1, 2, 3]; // Array of numbers using the basic syntax.
console.log("7. Array (number[]):", numbers1);

let strings: string[] = ["apple", "banana"]; // Array of strings.
console.log("   Array (string[]):", strings);

let numbers2: Array<number> = [4, 5, 6]; // Array of numbers using the generic syntax.
console.log("   Array (Array<number>):", numbers2);

// 8. Tuple declarations (fixed-size, typed arrays).
let coordinates: [number, number] = [10, 20]; // Tuple with two numbers.
console.log("8. Tuple ([number, number]):", coordinates);

let personInfo: [string, number, boolean] = ["Alice", 30, true]; // Tuple with string, number, boolean.
console.log("   Tuple ([string, number, boolean]):", personInfo);

// 9. Enum declarations (set of named constants).
enum Color2 { Red, Green, Blue };
let favoriteColor: Color2 = Color2.Green;
console.log("9. Enum (Color):", favoriteColor); // Output will be the numeric index (1).

enum Status2 { Pending = 1, Processing, Completed = 5 };
let currentStatus: Status2 = Status2.Processing;
console.log("   Enum (Status):", currentStatus); // Output will be the numeric value (2).

// 10. Union types (allows a variable to hold one of several types).
let id: number | string;
id = 101;
console.log("10. Union (number | string):", id);
id = "ID-ABC";
console.log("   Union (number | string) - second value:", id);
// id = true; // This would cause a type error.

// 11. Intersection types (combines multiple types).
interface Point {
  x: number;
  y: number;
}

interface Named {
  name: string;
}

type PointAndName = Point & Named;
let pointObject: PointAndName = { x: 5, y: 10, name: "PointA" };
console.log("11. Intersection (Point & Named):", pointObject);

// 12. 'void' type for functions that don't return a value.
function logMessage2(message: string): void {
  console.log("12. Void function:", message);
}
logMessage2("This function returns nothing.");

// 13. 'never' type for functions that never return (e.g., throw errors).
function throwError2(message: string): never {
  throw new Error(message);
}
// console.log("13. Never function (will throw an error):", throwError("Something went wrong!")); // Uncommenting this will cause an error at runtime.

// 14. 'null' and 'undefined' types.
let maybeNull: string | null = null;
console.log("14. Null:", maybeNull);

let maybeUndefined: number | undefined;
console.log("   Undefined:", maybeUndefined);

// 15. Object type (represents a non-primitive type).
let myObject: object = { key: "value" };
console.log("15. Object:", myObject);
let anotherObject: { name: string, age: number } = { name: "John", age: 35 };
console.log("   Object literal:", anotherObject);