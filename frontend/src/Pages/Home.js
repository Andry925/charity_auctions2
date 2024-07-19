import React from 'react'

import Header from '../Components/Header/Header';
import Search from '../Components/Search/Search';
import HomeAllAuctions from '../Components/HomeAllAuctions/HomeAllAuctions';
import ActualCollections from '../Components/ActualCollections/ActualCollections';
import Categories from '../Components/Categories/Categories';
import LastLots from '../Components/LastLots/LastLots';
import Footer from '../Components/Footer/Footer'

const Home = () => {
  return (
    <div>
        <Header/>
        <Search/>
        <HomeAllAuctions/>
        <ActualCollections/>
        <LastLots/>
        <Categories/>
        <Footer/>
    </div>
  )
}

export default Home;