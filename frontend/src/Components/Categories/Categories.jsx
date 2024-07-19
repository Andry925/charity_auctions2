import React from 'react'
import './Categories.css'

const Categories = () => {
  return (
    <div className='categories-container'>
        <div className='categories-caption'>
            <p>Категорії</p>
        </div>
        <div className='categories-buttons'>
            <button>Антикваріат і<br></br>Колекціонування</button>
            <button>Ноутбуки<br></br> ПК та планшети</button>
            <button>Телефони<br></br>та Смартфони</button>
            <button>Електроніка та<br></br>Техніка</button>
            <button>Мода<br></br>Краса</button>
            <button>Дитячий<br></br>світ</button>
            <button>Дім<br></br>Дозвілля</button>
            <button>Спорт<br></br>Здоров'я</button>
            <button>Авто<br></br>Мото</button>
            <button>Інші<br></br>товари</button>
        </div>
    </div>
  )
}

export default Categories;