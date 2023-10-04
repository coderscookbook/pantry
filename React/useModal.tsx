//https://blog.jsexpert.io/modals-in-react-with-the-usemodal-hook-b5ff8ade612c
//used to display important information, ask for user input, or confirm an action. 
//While modal windows can be helpful, they can also be difficult to manage, 
//  especially if you have several modals on your page
//With this hook, you can easily open and close modals, pass data to them, 
//  and handle user interactions.

//useModal hook:
import { useState } from 'react';

function useModal() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalContent, setModalContent] = useState(null);

  function openModal(content) {
    setModalContent(content);
    setIsModalOpen(true);
  }

  function closeModal() {
    setModalContent(null);
    setIsModalOpen(false);
  }

  return {
    isModalOpen,
    openModal,
    closeModal,
    modalContent,
  };
}

//USING useModal Hook in another component/file
import { useState } from 'react';
import useModal from './useModal';

function App() {
  const [data, setData] = useState(null);
  const { isModalOpen, openModal, closeModal, modalContent } = useModal();

  function handleButtonClick() {
    setData('example data');
    openModal(<Modal onClose={closeModal} data={data} />);
  }

  return (
    <div>
      <button onClick={handleButtonClick}>Open Modal</button>
      {isModalOpen && modalContent}
    </div>
  );
}

function Modal({ onClose, data }) {
  function handleConfirm() {
    console.log('Confirmed with data:', data);
    onClose();
  }

  return (
    <div>
      <h2>Modal Content</h2>
      <p>Data: {data}</p>
      <button onClick={onClose}>Cancel</button>
      <button onClick={handleConfirm}>Confirm</button>
    </div>
  );
}

/*In this example, the App component uses the useModal hook to create and manage a modal window. When the user clicks the "Open Modal" button, the handleButtonClick function is called. This function sets some data and calls openModal with a Modal component as the content.

The `Modal component receives two props: onClose and data. onClose is a function that will be called when the user clicks the "Cancel" button or the "Confirm" button. data is the data that was set in the handleButtonClick function.

The Modal component displays the content of the modal window, including the data passed in as a prop. It also includes a "Cancel" button and a "Confirm" button. When the user clicks the "Cancel" button, the onClose function is called, which will close the modal window. When the user clicks the "Confirm" button, the handleConfirm function is called, which logs the data to the console and then calls onClose to close the modal window.

Finally, in the App component, we render a button that opens the modal when clicked, and conditionally render the modal by checking whether isModalOpen is true and rendering the modalContent in the DOM.

Conclusion
In this article, we’ve shown you how to create a useModal hook in React that simplifies creating and managing modal windows. With this hook, you can easily open and close modals, pass data to them, and handle user interactions.

The useModal hook can be customized to fit your specific needs. For example, you can add more state variables to track different types of modals or add additional functions to handle specific user interactions.

By using the useModal hook, you can make your React code cleaner and more organized, and avoid the complexity of managing modals directly in your components. We hope this article was helpful, and that you'll find the useModal hook useful in your React projects*/