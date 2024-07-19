import React from 'react';
import './App.css';

// import NotLoggedIn from './Components/PageHome/NotLoggedIn'
import Home from './Pages/Home';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

// import NotLoggedIn from './Components/PageHome/NotLoggedIn'
// import LoginPage from './Pages/LoginPage';
// import Signup from './Components/Signup/Signup';

function App() {
  return (
    <div>
      <Home />
    </div>
  );
}

export default App;
