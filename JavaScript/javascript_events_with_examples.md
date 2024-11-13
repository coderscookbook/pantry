
# JavaScript Events with Examples

- **click**: Fired when an element is clicked.
  ```javascript
  element.addEventListener('click', () => {
    console.log('Element clicked');
  });
  ```

- **dblclick**: Fired when an element is double-clicked.
  ```javascript
  element.addEventListener('dblclick', () => {
    console.log('Element double-clicked');
  });
  ```

- **mouseover**: Fired when the mouse pointer is moved onto an element.
  ```javascript
  element.addEventListener('mouseover', () => {
    console.log('Mouse over element');
  });
  ```

- **mouseout**: Fired when the mouse pointer is moved out of an element.
  ```javascript
  element.addEventListener('mouseout', () => {
    console.log('Mouse out of element');
  });
  ```

- **mousedown**: Fired when a mouse button is pressed down on an element.
  ```javascript
  element.addEventListener('mousedown', () => {
    console.log('Mouse button down on element');
  });
  ```

- **mouseup**: Fired when a mouse button is released over an element.
  ```javascript
  element.addEventListener('mouseup', () => {
    console.log('Mouse button released on element');
  });
  ```

- **keydown**: Fired when a key is pressed down.
  ```javascript
  window.addEventListener('keydown', (event) => {
    console.log('Key down:', event.key);
  });
  ```

- **keyup**: Fired when a key is released.
  ```javascript
  window.addEventListener('keyup', (event) => {
    console.log('Key up:', event.key);
  });
  ```

- **keypress**: Fired when a key is pressed (deprecated in modern browsers; use `keydown`).
  ```javascript
  window.addEventListener('keypress', (event) => {
    console.log('Key press:', event.key);
  });
  ```

- **change**: Fired when the value of an element changes (like a text input or select).
  ```javascript
  inputElement.addEventListener('change', () => {
    console.log('Value changed');
  });
  ```

- **submit**: Fired when a form is submitted.
  ```javascript
  formElement.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent form from submitting
    console.log('Form submitted');
  });
  ```

- **focus**: Fired when an element gains focus.
  ```javascript
  inputElement.addEventListener('focus', () => {
    console.log('Element focused');
  });
  ```

- **blur**: Fired when an element loses focus.
  ```javascript
  inputElement.addEventListener('blur', () => {
    console.log('Element lost focus');
  });
  ```

- **resize**: Fired when the window is resized.
  ```javascript
  window.addEventListener('resize', () => {
    console.log('Window resized');
  });
  ```

- **scroll**: Fired when the page or an element is scrolled.
  ```javascript
  window.addEventListener('scroll', () => {
    console.log('Page scrolled');
  });
  ```

- **load**: Fired when the page has fully loaded.
  ```javascript
  window.addEventListener('load', () => {
    console.log('Page fully loaded');
  });
  ```

- **unload**: Fired when the document or a child resource is being unloaded (deprecated in favor of `beforeunload`).
  ```javascript
  window.addEventListener('unload', () => {
    console.log('Page is unloading');
  });
  ```

- **beforeunload**: Fired when the window, document, or a resource is about to be unloaded.
  ```javascript
  window.addEventListener('beforeunload', (event) => {
    event.returnValue = ''; // Prompt the user if they want to leave the page
  });
  ```

- **input**: Fired when the value of an `<input>` or `<textarea>` element is changed.
  ```javascript
  inputElement.addEventListener('input', () => {
    console.log('Input value changed');
  });
  ```

- **contextmenu**: Fired when the right mouse button is clicked (to open a context menu).
  ```javascript
  element.addEventListener('contextmenu', (event) => {
    event.preventDefault(); // Prevent default context menu
    console.log('Context menu opened');
  });
  ```

- **wheel**: Fired when the mouse wheel is rotated.
  ```javascript
  window.addEventListener('wheel', (event) => {
    console.log('Mouse wheel event:', event.deltaY);
  });
  ```
