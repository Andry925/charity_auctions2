import React from 'react';
import { Navigate } from 'react-router-dom';

const PrivateRoute = ({ element, redirectTo = '/login' }) => {

  const isAuthenticated = localStorage.getItem('sessionId') !== null;

  return isAuthenticated ? (

    element
  )
      : (

    <Navigate to={redirectTo} replace />
  );
};

export default PrivateRoute;