import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import user from "../Assets/user.svg";
import envelope from "../Assets/envelope.svg";
import lock from "../Assets/lock.svg";
import './Signup.css'

axios.defaults.withCredentials = true;

const Signup = ({ setCurrentUser }) => {
  const navigate = useNavigate();

  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const Registration = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/registration", {
        email,
        username,
        password,
      });

      if (response.status === 201 || response.status === 200) {
        navigate('/login');
      }
    } catch (error) {
      console.error("Failed registration", error);
    }

    console.log('Registration function called');
  };

  return (
    <div className='container'>
      <div className="header">
        <div className="text">Реєстрація</div>
        <div className="underline"></div>
      </div>
      <div className="inputs">
        <div className="input">
          <img src={user} alt="user"/>
          <input type="text" placeholder="Ім'я" onChange={(e) => setUsername(e.target.value)}/>
        </div>
        <div className="input">
          <img src={envelope} alt="email"/>
          <input type="email" placeholder='E-mail' onChange={(e) => setEmail(e.target.value)}/>
        </div>
        <div className="input">
          <img src={lock} alt="lock"/>
          <input type="password" placeholder='Пароль' onChange={(e) => setPassword(e.target.value)}/>
        </div>
      </div>
      <div className="submit-container">
        <button className="submit" onClick={Registration}>Реєстрація</button>
      </div>
    </div>
  )
}

export default Signup;