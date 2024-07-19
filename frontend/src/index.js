import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Home from './Pages/Home'
import HomeAccount from './Pages/HomeAccount'
import LoginPage from './Pages/LoginPage'
import SignupPage from "./Pages/SignupPage"
import CabinetPage from './Pages/CabinetPage';
import AllAuctions from './Pages/AllAuctions';
import EditLotPage from './Pages/EditLot';
import CreateLotPage from './Pages/CreateLotPage';
import AuctionPage from './Pages/AuctionPage';

import reportWebVitals from './reportWebVitals';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

import PrivateRoute from "./PrivateRoute";

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
  },
  {
    path: '/home',
    element: <Home />,
  },
  {
    path: '/home-acc',
    element: (
      <PrivateRoute
        element={<HomeAccount />}
        isAuthenticated={PrivateRoute.isAuthenticated}
        redirectTo="/login"
      />
    ),
  },
  {
    path: '/signup',
    element: <SignupPage />,
  },
  {
    path: '/login',
    element: <LoginPage />,
  },
  {
    path: '/cabinet',
    element: (
      <PrivateRoute
        element={<CabinetPage />}
        isAuthenticated={PrivateRoute.isAuthenticated}
        redirectTo="/login"
      />
    ),
  },
  {
    path: '/all-auctions',
    element: (
      <PrivateRoute
        element={<AllAuctions />}
        isAuthenticated={PrivateRoute.isAuthenticated}
        redirectTo="/login"
      />
    ),
  },
  {
    path: "/edit",
    element: <EditLotPage/>,
  },
  {
    path: "/create",
    element: <CreateLotPage/>,
  },
  {
    path: "/auction",
    element: <AuctionPage/>,
  },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

reportWebVitals();