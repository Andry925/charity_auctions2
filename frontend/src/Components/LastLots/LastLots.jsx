import './LastLots.css'
import React, { useEffect, useState } from 'react';
import './LastLots.css';

const LastLots = () => {
    const [lots, setLots] = useState([
        { id: 1, image_url: 'path/to/image1.jpg', description: 'Description 1', current_bid: 1000 },
        { id: 2, image_url: 'path/to/image2.jpg', description: 'Description 2', current_bid: 2000 },
        { id: 3, image_url: 'path/to/image3.jpg', description: 'Description 3', current_bid: 3000 },
        { id: 4, image_url: 'path/to/image4.jpg', description: 'Description 4', current_bid: 4000 },
        { id: 5, image_url: 'path/to/image5.jpg', description: 'Description 5', current_bid: 5000 },
        { id: 6, image_url: 'path/to/image6.jpg', description: 'Description 6', current_bid: 6000 },
    ]);

    useEffect(() => {
        console.log('LastLots component mounted');
    }, []);

    return (
        <div className='last-lots-container'>
            <div className='last-lots-caption'>
                <p>Останні лоти | <a href="/all-auctions" className="all-lots-caption"> Усі лоти</a>
                </p>
            </div>
            <div className='last-lots'>
                {lots.map(lot => (
                    <a href='/auction' key={lot.id}>
                        <div className="lot-home">
                            <div className="lot-home-photo">
                                <img src={lot.image_url} alt="lot"/>
                                <p className='lot-home-descr'>{lot.description}</p>
                                <p className='lot-home-price'>{lot.current_bid} грн</p>
                            </div>
                        </div>
                    </a>
                ))}
            </div>
        </div>
    );
}

export default LastLots;
