import React from 'react';

import HeaderAccount from '../Components/HeaderAccount/HeaderAccount';
import Search from '../Components/Search/Search';
import EditLot from '../Components/EditLot/EditLot'
import FooterAccount from '../Components/FooterAccount/FooterAccount'

function EditLotPage() {
  return (
    <div>
      <HeaderAccount/>
      <Search/>
      <EditLot/>
      <FooterAccount/>
    </div>
  );
}

export default EditLotPage;