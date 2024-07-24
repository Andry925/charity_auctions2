import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import clip from '../Assets/clip.svg';
import { useNavigate } from 'react-router-dom';
import './CreateLot.css';
import { updateTokens } from "../../utils/refreshToken";
import axios from "axios";

const CreateLot = () => {
    const { lotId } = useParams();
    const [starting_price, setPrice] = useState('');
    const [description, setDescr] = useState('');
    const [auction_duration, setDuration] = useState('');
    const [image_url, setPhoto] = useState(null);
    const navigate = useNavigate();

    const saveChanges = () => {
        const editedLot = { starting_price, description, auction_duration, image_url };
        localStorage.setItem('editedLot', JSON.stringify(editedLot));
        window.location.href = '/cabinet';
    };

    const handleLotCreation = async () => {
        try {
            const formData = new FormData();
            formData.append('starting_price', starting_price);
            formData.append('description', description);
            formData.append('auction_duration', auction_duration);
            if (image_url) {
                formData.append('image_url', image_url);
            }

            const response = await axios.post("http://127.0.0.1:8000/api/auctions/all-auctions", formData, {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
                    'Content-Type': 'multipart/form-data'
                }
            });
            if (response.status === 401) {
                updateTokens();
            } else if (response.status === 200 || response.status === 201) {
                navigate('/home-acc');
            }
        } catch (error) {
            console.error("Failed to create lot", error);
        }
    };

    return (
        <div className='container'>
            <div className="header">
                <div className="text">Створити лот</div>
                <div className="underline"></div>
            </div>
            <div className='starting_price-category'>
                <div className='starting_price-div'>
                    <div className="starting_price-caption">Початкова ціна</div>
                    <input
                        className='starting_price-input'
                        type="text"
                        placeholder='350'
                        maxLength="5"
                        value={starting_price}
                        onChange={(e) => setPrice(e.target.value)}
                    />
                    <div className="duration-div">
                        <div className='duration-caption'>Тривалість аукціону (дні)</div>
                        <input
                            type="number"
                            className='duration-input'
                            placeholder="7"
                            min="1"
                            max="30"
                            value={auction_duration}
                            onChange={(e) => setDuration(e.target.value)}
                        />
                    </div>
                </div>
                <div className='category-div'>
                    <div className='category-caption'>Категорія</div>
                    <div className='category-choice1'>
                        <button className='category-choice-vary'>Антикваріат і Колекціонування</button>
                        <button className='category-choice-vary'>Ноутбуки ПК та планшети</button>
                        <button className='category-choice-vary'>Телефони та Смартфони</button>
                        <button className='category-choice-vary'>Електроніка та Техніка</button>
                    </div>
                    <div className='category-choice2'>
                        <button className='category-choice-vary'>Мода | Краса</button>
                        <button className='category-choice-vary'>Дитячий світ</button>
                        <button className='category-choice-vary'>Дім | Дозвілля</button>
                        <button className='category-choice-vary'>Спорт | Здоров’я</button>
                    </div>
                    <div className='category-choice3'>
                        <button className='category-choice-vary'>Авто | Мото</button>
                        <button className='category-choice-vary'>Інші товари</button>
                    </div>
                </div>
            </div>
            <div className='descriptioniption-image_url'>
                <div className="description-div">
                    <div className='description-caption'>Опис</div>
                    <input
                        type="text"
                        className='description-text'
                        placeholder="Альбом для монет"
                        maxLength="50"
                        value={description}
                        onChange={(e) => setDescr(e.target.value)}
                    />
                </div>
                <div className="image_url-div">
                    <div className='image_url-caption'>Додати фото</div>
                    <div className="image_url-div-components">
                        <div className="lot-image_url-edit-page">
                            {image_url && <img src={URL.createObjectURL(image_url)} alt="lot" style={{ width: '100%', height: '100%' }} />}
                        </div>
                        <label htmlFor="fileInput" className="pin">
                            <input
                                id="fileInput"
                                type="file"
                                accept="image/*"
                                style={{ display: 'none' }}
                                onChange={(e) => {
                                    const file = e.target.files[0];
                                    setPhoto(file);
                                }}
                            />
                            <img src={clip} alt="clip" className="clip" />
                        </label>
                    </div>
                </div>
            </div>
            <div className='edit-page-button'>
                <button className='submit' onClick={handleLotCreation}>Зберегти</button>
            </div>
        </div>
    );
};

export default CreateLot;
