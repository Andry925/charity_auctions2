import React from 'react'
import './Footer.css'

import logo from '../Assets/logo.svg'
import companyName from '../Assets/companyName.svg'
import facebook from '../Assets/facebook.svg'
import insta from '../Assets/insta.svg'

const Footer = () => {
  return (
    <div className='footer'>
        {/* <div className="info-footer">
            <ul className='info-ul'>
                <li>
                    <ul className='first-item'>
                        <li>Угода та Правила торгівлі</li>
                        <li>Допомога</li>
                        <li>Зв'язатися з нами</li>
                    </ul>
                </li>
                <li className='second-item'>Сайт живе за київським часом</li>
                <li className='last-item'>
                    <ul className='footer-login-signup'>
                        <li className='login'>Увійти</li>
                        <li className='signup'>Реєстрація</li>
                    </ul>
                </li>
            </ul>
        </div> */}
        <div className="media-footer">
               <div className='media'>
                    <img src={facebook} alt="facebook" className="facebook" />
                    <img src={insta} alt="insta" className="insta" />
                    <p className='copyright'>Copyright ©</p>
                </div>
                <div className='company-name-logo'>
                    <a href="/home" className="home-page">
                   <img src={logo} alt="logo" className="logo" />
                    <img src={companyName} alt="company" className='company'/> 
                    </a>
                </div>        
        </div>
    </div>
  )
}

export default Footer;