import React from 'react'
import './Header.css'

import logo from '../Assets/logo.svg'
import companyName from '../Assets/companyName.svg'

const Header = () => {
  return (
    <div className='navbar'>
      <div className='company-img'>
        <a href="/home" className="home-page">
          <img src={logo} alt="logo" className="logo" />
        <img src={companyName} alt="company" className='company'/>
        </a>
      </div>
        <ul>
          {/* <li className='live'>LIVE</li>
          <li className='top100'>Top 100</li> */}
          {/* <li><button className="open-collection">Відкрити збір</button></li> */}
          <li><a href="/create" className="create-lot"><button className="sell">Продати</button></a></li>
          <li className='login'>
            <a href="/login" className="login">Увійти</a>
          </li>
          <li className='signup'>
            <a href="/signup" className="signup">Реєстрація</a>
          </li>
        </ul>
    </div>
  )
}

export default Header;