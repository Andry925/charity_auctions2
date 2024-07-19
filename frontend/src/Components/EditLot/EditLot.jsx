import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import clip from '../Assets/clip.svg';
import './EditLot.css';

const EditLot = () => {
    const { lotId } = useParams();
    const [price, setPrice] = useState('');
    const [descr, setDescr] = useState('');
    const [photo, setPhoto] = useState('');

    const saveChanges = () => {
        const editedLot = { price, descr, photo };
        localStorage.setItem('editedLot', JSON.stringify(editedLot));
        window.location.href = '/cabinet';
    };

    return (
        <div className='container'>
            <div className="header">
                <div className="text">Редагування</div>
                <div className="underline"></div>
            </div>
            <div className='price-category'>
                <div className='price-div'>
                    <div className="price-caption">Ціна</div>
                    <input
                        className='price-input'
                        type="text"
                        placeholder='350'
                        maxLength="5"
                        value={price}
                        onChange={(e) => setPrice(e.target.value)}
                    />
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
            <div className='description-photo'>
                <div className="descr-div">
                    <div className='descr-caption'>Опис</div>
                    <input
                        type="text"
                        className='descr-text'
                        placeholder="Альбом для монет"
                        maxLength="50"
                        value={descr}
                        onChange={(e) => setDescr(e.target.value)}
                    />
                </div>
                <div className="photo-div">
                    <div className='photo-caption'>Додати фото</div>
                    <div className="photo-div-components">
                        <div className="lot-photo-edit-page">
                            {photo && <img src={photo} alt="lot" style={{ width: '100%', height: '100%' }} />}
                        </div>
                        <label htmlFor="fileInput" className="pin">
                            <input
                                id="fileInput"
                                type="file"
                                accept="image/*"
                                style={{ display: 'none' }}
                                onChange={(e) => {
                                    const file = e.target.files[0];
                                    const imageUrl = URL.createObjectURL(file);
                                    setPhoto(imageUrl);
                                }}
                            />
                            <img src={clip} alt="clip" className="clip" />
                        </label>
                    </div>
                </div>
            </div>
            <div className='edit-page-button'>
                <button className='submit' onClick={saveChanges}>Зберегти зміни</button>
            </div>
        </div>
    )
}

export default EditLot;
