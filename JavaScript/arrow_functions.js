/* 1. No Parameters
- if the function takes no parameters, use empty parentheses */
const greet = () => "Hello!";
console.log(greet());

/* 2. Single Parameter
- if there is only one param, parentheses are optional */
const square = x => x * x;
console.log(square(4));

/* 3. Multiple Parameters
- params are separated by commas, both in func definition & function call */
const add = (a, b) => a + b;
console.log(add(2, 3));

/* 4. Function Body w/Multiple Statements
- if the function body has more than one statement, use curley braces and
  specify the return keyword if you want to return something */
  const greetPerson = name => {
    const greeting = "Hello, " + name + "!";
    return greeting;
  }
  console.log(greetPerson("Alice"));

/* 5. Returning Object Literals
- when directly returning an object literal, wrap the literal in parentheses to
  differentiate it from the function block */
// 5.a
const makePerson = (firstName, lastName) =>
({ first: firstName, last: lastName});
console.log(makePerson("John", "Doe"));
// 5.b: Creating User Profile
const createUserProfile = (id, firstName, lastName, email) =>
  ({
    id: id,
    name: {
      first: firstName,
      last: lastName,
    },
    contact: {
      email: email,
    },
    isActive: true,
    createdAt: new Date(),
  });
  console.log(createUserProfile(1, "Jane", "Smith", "jane.smith@example.com"));
// 5.c: Configuring API Endpoints
const createApiEndpoint = (method, path, requiresAuth) =>
({
  method: method,
  path: path,
  requiresAuth: requiresAuth,
  responseType: 'json',
  headers: {
    'Content-Type': 'application/json',
  },
});
console.log(createApiEndpoint("GET", "/users", true));

/* 6. High Order Function and Callbacks
- arrow functions are particularly popular when used as short callbacks */
const numbers = [1,2,3,4,5];
const doubled = numbers.map(num => num * 2);
console.log(doubled);
// 6.b: Filtering and Mapping a List of Orders
const orders = [
  { id: 1, amount: 100, status: 'shipped' },
  { id: 2, amount: 200, status: 'pending' },
  { id: 3, amount: 150, status: 'delivered' },
];
const processedOrders = orders
  .filter(order => order.status === 'shipped' || order.status === 'delivered')
  .map(order => ({
    id: order.id,
    amount: order.amount * 1.1, // applying a 10% tax
    status: order.status,
  }));
console.log(processedOrders);
// 6.c: Transforming and Aggregating Data for a Dashboard
const salesData = [
  { product: 'Laptop', sales: 1500 },
  { product: 'Phone', sales: 3000 },
  { product: 'Tablet', sales: 1000 },
  { product: 'Headphones', sales: 500 },
];
const salesSummary = salesData
  .map(item => ({ ...item, salesWithTax: item.sales * 1.08 })) // adding 8% tax to sales
  .reduce((acc, item) => {
    acc.totalSales += item.salesWithTax;
    acc.productCount += 1;
    return acc;
  }, { totalSales: 0, productCount: 0 });
console.log(salesSummary);
