//https://medium.com/@nadeem.ahmad.na/the-power-of-useref-in-react-a-comprehensive-guide-fe0029be1ad8
/*
What We Can Use Refs For:
-Managing focus: We can use ref to manage focus on particular elements or components.
-Animations and transitions: We can use ref to trigger animations and transitions on elements or components.
-Controlling media playback: We can use ref to control media playback on audio or video elements.
-Measuring element size and position: We can use ref to measure the size and position of elements on the page.
-Integrating with third-party libraries: We can use ref to integrate with third-party libraries that rely on direct interaction with the DOM.

Why it's so useful:
-Efficiency: ref provides a more efficient way to interact with the DOM than traditional JavaScript or libraries such as jQuery.
-Predictability: ref provides a predictable way to reference and interact with elements and components in the DOM.
-Flexibility: ref provides a flexible way to reference and interact with elements and components in the DOM, allowing for a wide range of use cases.
*/

//logging a message to the console, use ref to reference the button element directly, and add an event listener to it:
import React, { useRef } from 'react';
  
//Example 1: component that renders button
const MyButton = () => {
const buttonRef = useRef(null);

const handleClick = () => {
  console.log('Button clicked');
};

return (
  <button ref={buttonRef} onClick={handleClick}>
    Click me
  </button>
);
};

export default MyButton;

//Example 2: a form that contains multiple inputs, and we want to focus on the first input when the form is rendered:
//create a reference to the first input element in the form
//using the useEffect hook to focus on the input element when the form is rendered
//using ref, we can interact with the DOM in a more efficient and predictable manner, and solve a common problem in web development
const MyForm = () => {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return (
    <form>
      <input type="text" ref={inputRef} />
      <input type="text" />
      <input type="text" />
      <input type="text" />
    </form>
  );
};

export default MyForm;

//EXAMPLE 3: demonstrate flexibility of ref
//component renders list of items, want to allow users to sort the list by dragging and dropping
//using ref to create an array of references to the list item elements
//using the react-beautiful-dnd library to enable dragging and dropping of list items
//using ref, able to reference the list item elements directly and update their positions in the list when they're dragged and dropped

import React, { useRef, useState } from 'react';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';

const MyList = () => {
  const [items, setItems] = useState([
    { id: 'item-1', content: 'Item 1' },
    { id: 'item-2', content: 'Item 2' },
    { id: 'item-3', content: 'Item 3' },
  ]);

  const itemRefs = useRef(items.map(() => React.createRef()));

  const handleDragEnd = (result) => {
    if (!result.destination) return;

    const itemsCopy = Array.from(items);
    const [removed] = itemsCopy.splice(result.source.index, 1);
    itemsCopy.splice(result.destination.index, 0, removed);

    setItems(itemsCopy);
  };

  return (
    <DragDropContext onDragEnd={handleDragEnd}>
      <Droppable droppableId="items">
        {(provided) => (
          <ul {...provided.droppableProps} ref={provided.innerRef}>
            {items.map((item, index) => (
              <Draggable key={item.id} draggableId={item.id} index={index}>
                {(provided, snapshot) => (
                  <li
                    ref={(el) => (itemRefs.current[index] = el)}
                    {...provided.draggableProps}
                    {...provided.dragHandleProps}
                    style={{
                      backgroundColor: snapshot.isDragging ? '#ddd' : '#fff',
                      ...provided.draggableProps.style,
                    }}
                  >
                    {item.content}
                  </li>
                )}
              </Draggable>
            ))}
            {provided.placeholder}
          </ul>
        )}
      </Droppable>
    </DragDropContext>
  );
};

export default MyList;

//The Cons of Using Refs
//-Tight coupling: Using ref can create tight coupling between components and the DOM, making it more difficult to refactor or maintain the codebase in the future.
//-Overuse: Overusing ref can make the code more complex and difficult to understand.
//-Compatibility: ref may not be compatible with certain React features, such as server-side rendering.

//BAD EXAMPLE 1:
//using ref to create a reference to the input element so that we can focus it when the form is submitted
//while this is a valid use case for ref, it may not be necessary in this particular case
//instead, we could simply call event.target.reset() in the handleSubmit function to clear the form and refocus the input
import React, { useRef, useState } from 'react';

const MyComponent = () => {
  const inputRef = useRef(null);
  const [value, setValue] = useState('');

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    inputRef.current.focus();
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input type="text" value={value} onChange={handleChange} ref={inputRef} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
};

export default MyComponent;

The Effects of Ref on Performance
Using ref can have a positive effect on performance in certain situations. Because ref provides a more efficient way to interact with the DOM than traditional JavaScript or libraries such as jQuery, it can help reduce the amount of work that React has to do to update the DOM. However, overusing ref can have a negative effect on performance by increasing the complexity of the code and making it more difficult for React to optimise updates.

In this example, we’re using ref to create a reference to the button element so that we can blur it after clicking. By doing this, we can ensure that the focus is returned to the document after the user clicks the button, which can improve accessibility and usability. Additionally, because we're using ref to interact with the DOM directly, we can avoid forcing React to update the entire component when the button is clicked. This can result in a more efficient and performant application, especially if the component has a large number of child elements or is frequently updated.
import React, { useState, useEffect, useRef } from 'react';

const MyComponent = () => {
  const [count, setCount] = useState(0);
  const buttonRef = useRef(null);

  useEffect(() => {
    // This effect will run every time the component re-renders
    console.log('Component re-rendered');
  });

  const handleClick = () => {
    setCount(count + 1);
    buttonRef.current.blur(); // Uses ref to blur the button after clicking
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={handleClick} ref={buttonRef}>
        Click me
      </button>
    </div>
  );
};

export default MyComponent;


//Forwarding Refs
forwardRef is a feature that allows a parent component to pass a ref to one of its child components. This is useful when the child component needs to expose a DOM node or a component instance to its parent component, or when the parent component needs to modify a child component's properties directly.

Here’s an example of how you might use forwardRef:
In this example, we’re using forwardRef to pass a ref to the ChildComponent. This allows us to access the child component's properties directly in the ParentComponent using childRef.current. We can use this to change the child component's color when the button is clicked.

const ChildComponent = React.forwardRef((props, ref) => {
  return <div ref={ref}>I'm a child component</div>;
});

const ParentComponent = () => {
  const childRef = React.useRef(null);

  const handleClick = () => {
    // Here we can access the child component's properties directly
    childRef.current.style.color = 'red';
  };

  return (
    <div>
      <ChildComponent ref={childRef} />
      <button onClick={handleClick}>Change child color</button>
    </div>
  );
};

//Advanced Use Cases
forwardRef can be used for more advanced use cases beyond simply passing a ref down to a child component. Here are a few examples:

a) Triggering Child Component Functions: If you want the parent component to be able to call functions on the child component, you can use forwardRef to pass a reference to those functions. This can be useful for triggering events or updating state in the child component. Here's an example:

const ChildComponent = React.forwardRef((props, ref) => {
  const handleClick = () => {
    // Trigger an event in the child component
    props.onClick();
  };
  
  return (
    <div ref={ref}>
      <button onClick={handleClick}>Click me!</button>
    </div>
  );
});

const ParentComponent = () => {
  const childRef = React.useRef(null);

  const handleClick = () => {
    // Trigger the child component's onClick function
    childRef.current.onClick();
  };

  return (
    <div>
      <ChildComponent ref={childRef} onClick={() => alert("Child component clicked!")} />
      <button onClick={handleClick}>Click child component</button>
    </div>
  );
};
In this example, we’re passing a function down to the child component through its props, and then calling that function from the parent component by calling childRef.current.onClick(). This allows us to trigger an event in the child component from the parent component.

b) Accessing Multiple Child Components: If you have multiple child components that you need to access from the parent component, you can use an array of refs with forwardRef. This allows you to keep track of multiple child components with a single variable. Here's an example:

const ChildComponent = React.forwardRef((props, ref) => {
  return <div ref={ref}>{props.children}</div>;
});

const ParentComponent = () => {
  const childRefs = React.useRef([]);

  const handleButtonClick = () => {
    // Change the background color of all child components
    childRefs.current.forEach(childRef => {
      childRef.current.style.backgroundColor = 'red';
    });
  };

  return (
    <div>
      <ChildComponent ref={el => childRefs.current[0] = el}>Child component 1</ChildComponent>
      <ChildComponent ref={el => childRefs.current[1] = el}>Child component 2</ChildComponent>
      <ChildComponent ref={el => childRefs.current[2] = el}>Child component 3</ChildComponent>
      <button onClick={handleButtonClick}>Change child colors</button>
    </div>
  );
};
In this example, we’re using an array of refs to keep track of multiple child components. We're setting each child component's ref to the corresponding index of the array. This allows us to access and modify the properties of each child component using the array of refs.

c) Accessing Child Component Properties: If you need to access a specific property of a child component, like its size or position, you can use forwardRef to pass a reference to that property. This allows you to access and modify the property directly from the parent component. Here's an example:

import React, { forwardRef, useRef, useEffect, useState } from 'react';

const ChildComponent = forwardRef((props, ref) => {
  const [size, setSize] = useState({ width: 0, height: 0 });

  useEffect(() => {
    const handleResize = () => {
      setSize({
        width: ref.current.offsetWidth,
        height: ref.current.offsetHeight,
      });
    };

    handleResize();
    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, [ref]);

  return (
    <div ref={ref}>
      <p>Child component</p>
      <p>Width: {size.width}</p>
      <p>Height: {size.height}</p>
    </div>
  );
});

const ParentComponent = () => {
  const childRef = useRef(null);

  const handleClick = () => {
    console.log('Child width:', childRef.current.offsetWidth);
    console.log('Child height:', childRef.current.offsetHeight);
  };

  return (
    <div>
      <button onClick={handleClick}>Get child size</button>
      <ChildComponent ref={childRef} />
    </div>
  );
};
In this example, the ChildComponent is a functional component that accepts a ref using forwardRef. The ref is attached to the <div> element inside the component. Whenever the component is resized, the handleResize function is called, which updates the size state with the current width and height of the <div> element.

In the ParentComponent, a childRef is created using the useRef hook, and passed down to the ChildComponent as a prop. When the "Get child size" button is clicked, the handleClick function is called, which logs the current width and height of the childRef to the console. This allows the parent component to access the size of the child component directly, without having to manually pass down the size as a prop.

In this example, the ChildComponent is a functional component that accepts a ref using forwardRef. The ref is attached to the <div> element inside the component. Whenever the component is resized, the handleResize function is called, which updates the size state with the current width and height of the <div> element.

In the ParentComponent, a childRef is created using the useRef hook, and passed down to the ChildComponent as a prop. When the "Get child size" button is clicked, the handleClick function is called, which logs the current width and height of the childRef to the console. This allows the parent component to access the size of the child component directly, without having to manually pass down the size as a prop.