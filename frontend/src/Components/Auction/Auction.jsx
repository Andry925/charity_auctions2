import React, { useState } from 'react';
import "./Auction.css";
import { Link } from 'react-router-dom';

const Auction = () => {
    const [lots, setLots] = useState([
        // Example data to replace fetched data
        { id: 1, image_url: 'path/to/image1.jpg', description: 'Example Lot 1', current_bid: '100' },
        { id: 2, image_url: 'path/to/image2.jpg', description: 'Example Lot 2', current_bid: '200' },
    ]);
    const [nickname, setNickname] = useState('');
    const [ratePrice, setRatePrice] = useState('');

    const handleSearch = () => {
        // Search functionality placeholder
    };

    const [value, setValue] = useState(1);

    const handleSliderChange = (event) => {
        setValue(event.target.value);
    };

    const makeBid = () => {
        setNickname('Найдобріша людина в світі');
        setRatePrice(value);
    };

    return (
        <div className='container'>
            <div className="header">
                <div className="text">Аукціон</div>
                <div className="underline"></div>
            </div>
            <div className='auction'>
                <div className="lot-auction">
                    <div className="lot-auction-photo">
                        {lots.map(lot => (
                            <div key={lot.id}>
                                <img src={lot.image_url} alt="lot"/>
                                <p className='lot-auction-descr'>{lot.description}</p>
                                <p className='lot-auction-price'>{lot.current_bid} грн</p>
                            </div>
                        ))}
                    </div>
                </div>
                <div className='rates'>
                    <p className='rate-history'>Історія ставок</p>
                    <div className='rates'>
                        <div className='rate'>
                            <p className='nickname'>Вперше працюємо з React :3</p>
                            <p className='rate-price'>100%</p>
                        </div>
                        <div className='rate'>
                            <p className='nickname'>Мама Тереза</p>
                            <p className='rate-price'>48789 грн</p>
                        </div>
                        <div className='rate'>
                            <p className='nickname'>Пес Патрон - в розмінуваннях чемпіон</p>
                            <p className='rate-price'>49999 грн</p>
                        </div>
                        <div className='rate'>
                            <p className='nickname'>{nickname}</p>
                            <p className='rate-price'>{ratePrice} грн</p>
                        </div>
                        <div className="sliderPrice-rate">
                            <p className='slider-price-value'><span>{value}</span> грн</p>
                            <input
                                type='range'
                                min='1'
                                max='50000'
                                value={value}
                                onChange={handleSliderChange}
                                className='slider'
                            />
                        </div>
                        <div className='make-rate'>
                            <div className='submit' onClick={makeBid}>
                                <div className="submit">
                                    Зробити ставку
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Auction;
