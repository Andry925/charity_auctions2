import React, { useState } from 'react';
import envelope from "../Assets/envelope.svg";
import lock from "../Assets/lock.svg";
import { useNavigate } from 'react-router-dom';
import './Login.css'

const Login = ({ setCurrentUser }) => {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    console.log('Login function called');
  }

  return (
    <div className='container'>
        <div className="header">
            <div className="text">Увійти</div>
            <div className="underline"></div>
        </div>
        <div className="inputs">
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
          <button
            className="submit"
            onClick={handleLogin}>Увійти
          </button>
      </div>
    </div>
  )
}

export default Login;
