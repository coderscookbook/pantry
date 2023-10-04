1. What is the type of A, and why?
So usually I would always start with the same question to the candidate because it’s a really simple piece of code, but I'm my opinion answer to that question can give you so much understanding of the candidate's knowledge of the subject.

type A = number & string;
The answer is really simple, the type of A is never and why, because & is intersection operator, and if we think about string and number as sets of values it can be assigned, then the intersection of those sets is — empty set, which in typescript is represented by never type, or in other words there's no value that exists which can belong to number and string at the same time:


But I heard so many times when people getting confused and saying something like:

there will be a TypeScript error, you can not create a type like this
type of A — is string and number, so you can assign string and number to A (like it would be union string|number)
… etc
I think it’s not just about not knowing TypeScript, but the issue here — it is a lack of general understanding of how types are working. And this is the really important thing because it is literally based on everything else, and if you have a good understanding of it, then other things will be really easy to learn.

Guys if you have the same problem I recommend your to read this article, which explains it perfectly: https://ivov.dev/notes/typescript-and-set-theory

2. Runtime validation
So let's say our candidate successfully answered the first question, so for me, it would mean the candidate got a good understanding of the basis. Now, let's get a bit more complex and this time, we going to get really practical: Let's say we have an API, which returns to us a JSON string, which contains information about the user.

The question is: How can we validate the user object, and make sure it actually satisfies the User type?

type User = {
  name: string;
  age: number;
};

const data = `{"name":"Bob","age":30}`;
const user: User = JSON.parse(data);

console.log(`Username: ${user.name.toLowerCase()}`);
console.log(`Age: ${user.age.toFixed(0)}`);
The answer is basically there two ways:

First, if the User type is small, like now with just two fields and it’s ok for us, then we can write a simple validation function:

function isUser(obj: unknown): obj is User {
  return (
    typeof obj['name'] === 'string' && 
    typeof obj['age'] === 'number'
  );
}
and use it like this:

const data = `{"name":"Bob","age":30}`;
const user = JSON.parse(data); // user type if any here

if (isUser(user)) {
  console.log(`Username: ${user.name.toLowerCase()}`);
  console.log(`Age: ${user.age.toFixed(0)}`);
}
The second variant, and it’s more convenient – to use schema validation using any library you like: class-validator, zod, runtypes, joi, … etc:

import Joi from 'joi';

const UserSchema = Joi.object({
  name: Joi.string(),
  age: Joi.number(),
});

const data = `{"name":"Bob","age":30}`;
const userData = JSON.parse(data)

try {
  const user = UserSchema.validate(userData);

  console.log(`Username: ${user.name.toLowerCase()}`);
  console.log(`Age: ${user.age.toFixed(0)}`);
} catch(e) {}
Surprisingly many candidates would answer something like:

JSON.parse(data) as User is enough
const user: User = JSON.parse(data) is enough
or even if (typeof user === User) { …. }
This question is to check not just the knowledge about data validation, but also to check how well the candidate knows the tech stack, which ways it can be done and etc.

3. Using recursion in types
The last question usually would be practical, and it’s about how to write a recursive type. In this example, the candidate needs to offer the solution for the problem: let’s say I’m writing a function find()to search users in the database. The problem is the type User has properties such as an address, which is also an object. I would like to build find() function the way, so I would be able to search by nested properties of User as well, with full types support:

function find<T>(criteria: ...): T[] {
  ...
}

type User = {
  id: number;
  name: string;
  address: {
    country: string;
    city: string;
    house: string;
    zipcode: string;
  };
};

// in this example im searching by country only, even if 
// address has other properties.

const users = find({
  address: { coutry: 'UK' }
});
How it can be implmented: let’s create another type called DeepPartial, and use it in find() function, for criteria argument:

type DeepPartial<T> = {
  [P in keyof T]?: DeepPartial<T[P]>;
};

function find<T>(criteria: DeepPartial<T>): T[] {
  ...
}

type User = {
  id: number;
  name: string;
  address: {
    country: string;
    city: string;
    house: string;
    zipcode: string;
  };
};

const users = find({
  address: { coutry: 'UK' }
});
DeepPartial<T> works almost as Partial<T>, but the only difference it applies recursively to each nested property of the object:

type User = {
  id: number;
  name: string;
  address: {
    country: string;
    city: string;
    house: string;
    zipcode: string;
  };
};

// DeepPartial<User>
type DeepPartiallUser = {
  id?: number;
  name?: string;
  address?: {
    country?: string;
    city?: string;
    house?: string;
    zipcode?: string;
  };
};
This question is to check how good a candidate is with TypeScript in practice, when it comes to software design or architecture, because it covers lots of topics at once, and makes the candidate think about how to solve given problems the right way.