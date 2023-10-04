// @ts-nocheck
// source: https://hackernoon.com/mastering-solid-principles-like-the-back-of-your-hand-in-just-8-minutes?source=rss

/* 
WHAT: 5 Design Principles that make application reusable, maintainable, and scalable, and loosely coupled:
- SINGLE-RESPONSIBILITY PRINCIPLE
- OPEN-CLOSED PRINCIPLE
- LISKOV SUBSTITUTION PRINCIPLE
- INTERFACE SEGREGATION PRINCIPLE
- DEPENDENCY INVERSION PRINCIPLE
*/

/*************************************************************************************
                     SINGLE-RESPONSIBILITY PRINCIPLE
    "A module should be responsible to one, and only one, actor."
    - states that a component should hav eone clear purpose or responsibility
    - focus on specific functionality or behavior and avoid taking on unrelated tasks
    - SRP makes components more focused, modular, easily comprehensible, and modified
EXAMPLE: BAD PRACTICE: Component with Multiple Responsibilities
  - violates the SRP by taking on multiple responsibilities
  - manages iteration of products and handles the UI rendering for each product
  == challenging to understand, maintain, and test in the future
*/
//#region
const Products = () => {
  return (
    <div className="products">
      {products.map((product) => (
        <div key={product?.id} className="product">
          <h3>{product?.name}</h3>
          <p>${product?.price}</p>
        </div>
      ))}
    </div>
  )
}
// GOOD PRACTICE: Separating Responsibilities into Smaller Components
// @ts-ignore
import Product from './Product'
import products from '../../data/products.json'
const Products = () => {
  return (
    <div className="products">
      {products.map((product) => (
        <Product key={product?.id} product={product} />
      ))}
    </div>
  )
}
// Product.js
// Separate component responsible for rendering the product details
// - ensures each component has a single responsibility = easier to understand, test, maintain
const Product = ({product}) => {
  return (
    <div className="product">
      <h3>{product?.name}</h3>
      <p>${product?.price}</p>
    </div>
  )
}
//#endregion
 
/*************************************************************************************
                          OPEN-CLOSED PRINCIPLE
*/


/*************************************************************************************
                            LISKOV SUBSTITUTION PRINCIPLE
*/


/*************************************************************************************
                            INTERFACE SEGREGATION PRINCIPLE
*/


/*************************************************************************************
                            DEPENDENCY INVERSION PRINCIPLE
*/
