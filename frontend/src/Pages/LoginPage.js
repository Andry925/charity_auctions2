import React from 'react';

import Header from '../Components/Header/Header';
import Search from '../Components/Search/Search';
import Login from '../Components/Login/Login';
import Footer from '../Components/Footer/Footer'

function LoginPage() {
  return (
    <div>
      <Header/>
      <Search/>
      <Login/>
      <Footer/>
    </div>
  );
}

export default LoginPage;