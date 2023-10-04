import React from 'react';

// Define a class named `MyComponent` that extends `React.Component`
class MyComponent extends React.Component {
  // The constructor method is called when a new object is created
  constructor(props) {
    super(props); // Always call the parent class's constructor with `super(props)`

    // Initialize the component's state
    this.state = {
      message: 'Hello, React!'
    };
  }

  // The `render` method is required for class components and returns the JSX to be rendered
  render() {
    return (
      <div>
        <h1>{this.state.message}</h1>
      </div>
    );
  }
}

export default MyComponent;


//USING IN OTHER PART OF APPLICATION
import React from 'react';
import MyComponent from './MyComponent';

function App() {
  return (
    <div>
      <MyComponent />
    </div>
  );
}

export default App;
