// from @code_with_fourtix 

//#region FIRST CLASS                                                                   
//component of a dish
class Animal {
    // Constructor eneables the creation of instances(objects) based on class
    constructor (name, age) {
      this.name = name;
      this.age  = age;
    }

    getInfo() {
      return (this.name + ' is this many years old: ' + this.age)
    }

}
//#endregion                                                                            

//#region FIRST INSTANCES                                                               
  // create object from the class's constructor
  const firstAnimal = new Animal ('Rex', 350)
  console.log(firstAnimal)
  console.log(firstAnimal.getInfo())

  const secondAnimal = new Animal ('Tank', 9)
  console.log(secondAnimal.getInfo())
  console.log(secondAnimal)
//#endregion

//#region INHERITANCE
// enables certain classes to take all the methods and properties of another one (parent class)
// makes it possible to extend the parent class by adding more methods and properties
class Dog extends Animal {
  constructor (name, age, weight) {
    super(name, age)
    this.weight =  weight
  }
  
  bark() {
    return 'Woof!'
  }
}

class Cat extends Animal {
  constructor (name, age, weight) {
    super(name, age)
    this.weight = weight
  }

  scratch() {
    return console.clear()
  }
}

const myDog = new Dog ('Tank', 5, 10)
const myCat = new Cat ('Luna', 3, 5)
console.log(myDog)
console.log(myDog.getInfo())
console.log(myDog.weight)
console.log(myDog.getInfo())
// myCat.scratch() clears the console
//#endregion

//#region ENCAPSULATION
// restriction mechanism making accessing the data impossible without using special methods
// methods are dedicated for accessing and modifying the data
// example below: set weight as private property, need to use get/set to manipulate data
class Cat extends Animal {
  #weight // marked as private
  constructor (name, age, weight) {
    super(name, age)
    this.#weight = weight
  }
  
  getWeight() {
    return this.#weight
  }

  setWeight(value) {
    this.#weight = weight 
  }
}

const imaginaryCat = new Cat('Whiskers', 5, '5kg')
console.log(imaginaryCat.getWeight())
imaginaryCat.setWeight('6kg')
console.log(imaginaryCat.getWeight())
//#endregion

//#region POLYMORPHISM
// concept utilizes inheritance for reusing methods multiple times w/a different behavior depending on class types
// example below: in the dog class, remove the bark method and in the animal class, add makeSound method
// example below: makeSound method will be overidden by cat and dog classes
class Animal {
  constructor (name, age) {
    this.name = name;
    this.age  = age;
  }

  makeSound() {
    return ('Some nice sound made')
  }
}
class Dog extends Animal {
  constructor (name, age, breed){
    super(name, age)
    this.breed = breed
  }
  makeSound() {
    return 'Woof!'
  }
}
class Cat extends Animal {
  constructor (name, age, weight) {
    super(name, age)
    this.weight = weight
  }
  makeSound() {
    return 'Meow!'
  }
}

const tempDog = new Dog('Max', 8, 'Yorkshire Terrier')
const newCat  = new Cat('Tippy', 1, '7 lbs')
console.log(tempDog.makeSound())  //Woof!
console.log(newCat.makeSound())   //Moew!
//#endregion

//#region ABSTRACTION
// class which can't be instantiated and require subclasses which inherit from a particular abstract class to provide implementations
// example below: change the Animal class to an abstract class
// example below: it will not be possible to create an instance of this class anymore
// example below: mark makeSound as an abstract method - in order to use it, a subclass must declare its own implementation of this method
class Animal {
  constructor (name, age) {
    this.name = name;
    this.age  = age;
    if(this.constructor == Animal) {
      throw new Error("Can't create an instance of an Abstract Class")
    }
  }
  makeSound() {
    throw new Error("Abstract method doesn't have an implementation")
  }
}

class Dog extends Animal {
  constructor(name, age, breed) {
    super(name, age)
    this.breed = breed
  }
  makeSound() {
    return 'Woof!'
  }
}
class Cat extends Animal {
  constructor(name, age, weight) {
    super(name, age)
    this.weight = weight
}
//makeSound() {
//  return 'Meow!'
//}
}

//const abstractAnimal = new Animal('Churro', 99999, '1 ton') // throws error
const abstractDog = ('Rex', 1000, 'Cloud Buffalo')
const abstractCat = ('Moowdecai', 1000, '0.00001lbs')
//console.log(abstractAnimal.makeSound()) // throws error
//#endregion
