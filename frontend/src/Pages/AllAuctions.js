import React from 'react'

import Header from '../Components/Header/Header';
import Search from '../Components/Search/Search';
import AllLots from '../Components/AllLots/AllLots';

import Footer from '../Components/Footer/Footer'

const AllAuctions = () => {
  return (
    <div>
        <Header/>
        <Search/>
        <AllLots/>
        <Footer/>
    </div>
  )
}

export default AllAuctions;