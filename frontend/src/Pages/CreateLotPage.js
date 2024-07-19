import React from 'react';

import HeaderAccount from '../Components/HeaderAccount/HeaderAccount';
import Search from '../Components/Search/Search';
import CreateLot from '../Components/CreateLot/CreateLot'
import FooterAccount from '../Components/FooterAccount/FooterAccount'

function CreateLotPage() {
  return (
    <div>
      <HeaderAccount/>
      <Search/>
      <CreateLot/>
      <FooterAccount/>
    </div>
  );
}

export default CreateLotPage;