import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import "./Cabinet.css";
import { useNavigate } from 'react-router-dom';
import { updateTokens } from "../../utils/refreshToken";

const Cabinet = () => {
    const [lots, setLots] = useState([
        { id: 1, price: '', descr: '' },
        { id: 2, price: '', descr: '' },
        { id: 3, price: '', descr: '' }
    ]);
    const navigate = useNavigate()
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');

    useEffect(() => {
        const editedLot = JSON.parse(localStorage.getItem('editedLot'));
        if (editedLot) {
            setLots(prevLots => {
                return prevLots.map(lot => lot.id === editedLot.id ? editedLot : lot);
            });
        }

        profileData();
    }, []);

    const profileData = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/my-profile/', {
                headers: { 'Authorization': `Bearer ${localStorage.getItem('accessToken')}` }
            });

            if (response.status === 200) {
                const { user, email } = response.data[0];
                setUsername(user);
                setEmail(email);
            } else if (response.status === 401) {
                updateTokens();
            }
        } catch (error) {
            if (error.response && error.response.status === 401) {
                updateTokens();
            } else {
                console.error('Error fetching profile data:', error);
            }
        }
    };

    const handleEdit = (id) => {
        const editedLot = lots.find(lot => lot.id === id);
        localStorage.setItem('editedLot', JSON.stringify(editedLot));
    };

   const handleLogOut = async() => {

       try {
           const response = await axios.post('http://127.0.0.1:8000/api/logout', {
               refresh: localStorage.getItem('refreshToken')
           }, {
               headers: {
                   'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
               }
           })
           if (response.status === 205) {
               localStorage.removeItem('accessToken');
               localStorage.removeItem('refreshToken');
               navigate('/login')
           }
       }

       catch (error){
           console.error("Error here")
       }

    };

    return (
        <div className='container'>
            <div className="header">
                <div className="text">Особистий кабінет</div>
                <div className="underline"></div>
            </div>
            <div className='account'>
                <div className='account-info'>
                    <div className="info-caption">Акаунт</div>
                    <div className="name-info">Ім'я: {username}</div>
                    <div className="email-info">Email: {email}</div>
                </div>
                <div className='account-lots'>
                    <div className="lot-caption">Мої аукціони</div>
                    <div className='lot-edit'>
                        {lots.map((lot) => (
                            <div key={lot.id} className='lot'>
                                <div className="lot-photo"></div>
                                <div className='lot-descr'>
                                    <p>{lot.descr}</p>
                                </div>
                                <div className="lot-price">
                                    <p>{lot.price}</p>
                                </div>
                                <Link to="/edit" className="edit-button-cabinet">
                                    <button className='edit' onClick={() => handleEdit(lot.id)}>Редагувати</button>
                                </Link>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
            <div className='logout'>
                <button className='submit' onClick={handleLogOut}>
                    Вийти
                </button>
            </div>
        </div>
    );
};

export default Cabinet;
