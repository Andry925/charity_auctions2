import React from 'react'
import { useState } from 'react';
import './Search.css'

import search from '../Assets/search.svg';
import filter from '../Assets/filter.svg'

const Search = () => {
  const [isFilterOpen, setIsFilterOpen] = useState(false);

  // const [selectedFilters, setSelectedFilters] = useState({
  //   category: '',
  //   price: '',
  // });

  const handleApplyFilters = () => {
    setIsFilterOpen(false);
  };

  const handleSearch = () => {
  };

  const [value, setValue] = useState(1);

  const handleSliderChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <div className="search-container">
        <div className='search-box'>
          <input type="text" className="search-box-text" placeholder='...Знайти лот' />
          <a onClick={handleSearch}>
            <a href="all-auctions">
              <img src={search} alt="search" className='search' />
            </a>
          </a>
        </div>
        <div className='filter-container'>
          <div className='filter-box' onClick={() => setIsFilterOpen(true)}>
            <img src={filter} alt="filter" className="filter" />
          </div> {isFilterOpen && (
            <div className='filter-window'>
                <div className='first-filter'>
                  <div className='filter-categories-caption'>
                    <p>Категорії</p>
                  </div>
                    <ul className='filter-categories'>
                      <li><a>Антикваріат і<br></br>Колекціонування</a></li>
                      <li><a>Ноутбуки<br></br>ПК та планшети</a></li>
                      <li><a>Телефони та Смартфони</a></li>
                      <li><a>Електроніка та Техніка</a></li>
                      <li><a>Мода | Краса</a></li>
                      <li><a>Дитячий світ</a></li>
                      <li><a>Дім | Дозвілля</a></li>
                      <li><a>Спорт та Здоров’я</a></li>
                      <li><a>Авто | Мото</a></li>
                      <li><a>Інші товари</a></li>
                    </ul>
              </div>

              <div className='second-filter'>
                <div className='filter-price-caption'>
                  <p>Ціна</p>
                </div>
                <div className="sliderPrice">
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
              </div>
              
              <button className='use-filter' onClick={handleApplyFilters}>Застосувати</button>
            </div>
          )}
        </div>
    </div>
   
  )
}

export default Search;