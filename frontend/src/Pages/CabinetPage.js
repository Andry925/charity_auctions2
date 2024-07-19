import React from 'react';

import HeaderAccount from '../Components/HeaderAccount/HeaderAccount';
import Search from '../Components/Search/Search';
import Cabinet from '../Components/Cabinet/Cabinet'
import FooterAccount from '../Components/FooterAccount/FooterAccount'

function CabinetPage() {
  return (
    <div>
      <HeaderAccount/>
      <Search/>
      <Cabinet/>
      <FooterAccount/>
    </div>
  );
}

export default CabinetPage;