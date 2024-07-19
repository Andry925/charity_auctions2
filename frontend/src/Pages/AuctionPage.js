import React from 'react';

import HeaderAccount from '../Components/HeaderAccount/HeaderAccount';
import Search from '../Components/Search/Search';
import Auction from '../Components/Auction/Auction'
import FooterAccount from '../Components/FooterAccount/FooterAccount'

function AuctionPage() {
  return (
    <div>
      <HeaderAccount/>
      <Search/>
      <Auction/>
      <FooterAccount/>
    </div>
  );
}

export default AuctionPage;