import React from 'react'
import './ActualCollections.css'

import victim from '../Assets/victim.svg';
import refugee from '../Assets/refugee.svg';
import zsu from '../Assets/zsu.svg';
import patient from '../Assets/patient.svg';
import shelter from '../Assets/shelter.svg';

const ActualCollections = () => {
  return (
    <div className='actual-collections-container'>
        <div className='actual-caption'>
            <p>Актуальні збори</p>
        </div>
        <div className='collection-buttons'>
            <button className='victim-button'>
                <img src={victim} alt="victim" className="victim" />
                <p>Для постраждалих</p>
            </button>
            <button className='refugee-button'>
                <img src={refugee} alt="refugee" className="refugee" />
                <p>Для біженців</p>
            </button>
            <button className='zsu-button'>
                <img src={zsu} alt="zsu" className="zsu" />
                <p>Для ЗСУ</p>
            </button>
            <button className='patient-button'>
                <img src={patient} alt="patient" className="patient" />
                <p>Для пацієнтів</p>
            </button>
            <button className='shelter-button'>
                <img src={shelter} alt="shelter" className="shelter" />
                <p>Для притулків</p>
            </button>
        </div>
    </div>
  )
}

export default ActualCollections;