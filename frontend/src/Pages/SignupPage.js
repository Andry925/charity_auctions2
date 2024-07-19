import React from 'react';

import Header from '../Components/Header/Header';
import Search from '../Components/Search/Search';
import Signup from '../Components/Signup/Signup';
import Footer from '../Components/Footer/Footer'

function SignupPage() {
  return (
    <div>
      <Header/>
      <Search/>
      <Signup/>
      <Footer/>
    </div>
  );
}

export default SignupPage;