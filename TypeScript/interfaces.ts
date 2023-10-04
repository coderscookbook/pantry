// Define the PersonProps interface to specify the shape of the object expected by the constructor
interface PersonProps {
  firstName: string;
  lastName: string;
  age: number;
  address?: string; // Optional property
}

// Define the Person class with properties and a constructor that accepts a PersonProps object
class Person {
  firstName: string;
  lastName: string;
  age: number;
  address?: string;

  constructor(props: PersonProps) {
    this.firstName = props.firstName;
    this.lastName = props.lastName;
    this.age = props.age;
    this.address = props.address;
  }

  getFullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }
}

// Creating a new instance of the Person class with valid properties
const person1 = new Person({
  firstName: "John",
  lastName: "Doe",
  age: 30,
});

// Creating another instance of the Person class with valid properties, including the optional address property
const person2 = new Person({
  firstName: "Jane",
  lastName: "Doe",
  age: 28,
  address: "123 Main St",
});

console.log(person1.getFullName()); // Output: "John Doe"
console.log(person2.getFullName()); // Output: "Jane Doe"

// This would result in a TypeScript error because the 'age' property is missing
// const person3 = new Person({
//   firstName: "Tom",
//   lastName: "Smith",
// });


/******************************COMPLEX EXAMPLE***************************************/
// Define the ProductProps interface to specify the shape of the object expected by the constructor
interface ProductProps {
  id: number;
  name: string;
  price: number;
  category: string;
  description?: string; // Optional property
}

// Define the ElectronicsProps interface, which extends ProductProps
interface ElectronicsProps extends ProductProps {
  brand: string;
  model: string;
  warranty: number;
}

// Define the ClothingProps interface, which extends ProductProps
interface ClothingProps extends ProductProps {
  size: string;
  color: string;
  material: string;
}

// Define the Product class with properties and a constructor that accepts a ProductProps object
class Product {
  id: number;
  name: string;
  price: number;
  category: string;
  description?: string;

  constructor(props: ProductProps) {
    this.id = props.id;
    this.name = props.name;
    this.price = props.price;
    this.category = props.category;
    this.description = props.description;
  }
}

// Define the Electronics class which extends the Product class
class Electronics extends Product {
  brand: string;
  model: string;
  warranty: number;

  constructor(props: ElectronicsProps) {
    super(props);
    this.brand = props.brand;
    this.model = props.model;
    this.warranty = props.warranty;
  }
}

// Define the Clothing class which extends the Product class
class Clothing extends Product {
  size: string;
  color: string;
  material: string;

  constructor(props: ClothingProps) {
    super(props);
    this.size = props.size;
    this.color = props.color;
    this.material = props.material;
  }
}

// Creating a new instance of the Electronics class with valid properties
const electronics1 = new Electronics({
  id: 1,
  name: "Smartphone",
  price: 800,
  category: "Electronics",
  brand: "Example Brand",
  model: "X100",
  warranty: 12,
});

// Creating a new instance of the Clothing class with valid properties, including the optional description property
const clothing1 = new Clothing({
  id: 2,
  name: "T-Shirt",
  price: 20,
  category: "Clothing",
  size: "M",
  color: "Blue",
  material: "Cotton",
  description: "Comfortable and stylish T-Shirt",
});

console.log(electronics1); // Output: Electronics {...}
console.log(clothing1); // Output: Clothing {...}
