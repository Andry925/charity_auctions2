import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom'; // For navigation
import './HomeAllAuctions.css';

import flag from '../Assets/flag.svg';
import logoName from '../Assets/logoName.svg';

const HomeAllAuctions = () => {
  const [auctions, setAuctions] = useState([
    { id: 1, img: 'path/to/image1.jpg', title: 'Auction 1', description: 'Description 1' },
    { id: 2, img: 'path/to/image2.jpg', title: 'Auction 2', description: 'Description 2' },
    { id: 3, img: 'path/to/image3.jpg', title: 'Auction 3', description: 'Description 3' },
    { id: 4, img: 'path/to/image4.jpg', title: 'Auction 4', description: 'Description 4' },
    { id: 5, img: 'path/to/image5.jpg', title: 'Auction 5', description: 'Description 5' },
  ]);
  const navigate = useNavigate();

  useEffect(() => {
    console.log('HomeAllAuctions component mounted');
  }, []);

  const navigateToCreateAuction = () => {
    navigate('/all-auctions');
  };

  return (
    <main>
      <div className='home-first-container'>
        <div className='article-container'>
          <p className='text-charity'>Благодійні аукціони по всій Україні<img src={flag} alt="flag" className='flag'/></p>
          <p className='text-register'>Реєструйся</p>
          <p className='text-buy'>Купуй лот</p>
          <p className='text-help'>Допомагай закрити збір!</p>
          <button className='all-auctions' onClick={navigateToCreateAuction}>Створити аукціон</button>
        </div>
        <div className='logo-name-container'>
          <img src={logoName} alt="logo" className='logoName'/>
        </div>
      </div>

      <section className='auctions-section'>
        {auctions.map(auction => (
          <div key={auction.id} className='auction-item'>
            <img src={auction.img} alt={auction.title} className="auction-image"/>
            <h3>{auction.title}</h3>
            <p>{auction.description}</p>
          </div>
        ))}
      </section>
    </main>
  );
}

export default HomeAllAuctions;
