import { useState, useEffect } from 'react'
import './App.css'
import ContactsList from './ContactList';
import ContactForm from './ContactForm';

function App() {  
  const [contacts, setContacts] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    fetchContacts();
  }, []);

  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5004/contacts");
    const data = await response.json();
    setContacts(data.contacts);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  }

  const openModal = () => {
    if( !isModalOpen ) setIsModalOpen(true);
  }

  return (
    <>      
      <ContactsList contacts={contacts}/>      
      <button onClick={openModal}>Create New Contact</button>
      <button onClick={() => methodDoesNotExist()}>Break the world</button>
      {
        isModalOpen && (
          <div className="modal">
            <div className="modal-content">
              <span className="close" onClick={closeModal}>&times;</span>
              <ContactForm />
            </div>

          </div>
        )
      }
    </>
  )
}

export default App
