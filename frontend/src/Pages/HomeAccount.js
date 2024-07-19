import React from 'react'

import HeaderAccount from '../Components/HeaderAccount/HeaderAccount';
import Search from '../Components/Search/Search';
import HomeAllAuctions from '../Components/HomeAllAuctions/HomeAllAuctions';
import ActualCollections from '../Components/ActualCollections/ActualCollections';
import Categories from '../Components/Categories/Categories';
import LastLots from '../Components/LastLots/LastLots';
import FooterAccount from '../Components/FooterAccount/FooterAccount'

const Home = () => {
  return (
    <div>
        <HeaderAccount/>
        <Search/>
        <HomeAllAuctions/>
        <ActualCollections/>
        <LastLots/>
        <Categories/>
        <FooterAccount/>
    </div>
  )
}

export default Home;