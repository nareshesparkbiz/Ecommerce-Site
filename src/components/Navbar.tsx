import React from 'react'
import '../assests/styles/navbar.css'
import logo from  '../assests/images/LV-logo.png'
import 'font-awesome/css/font-awesome.min.css';

import Popup from 'reactjs-popup';
import 'reactjs-popup/dist/index.css';

import { Link } from 'react-router-dom';
import Profile from '../pages/profile/Profile';



export default function Navbar() {





  return (
    <div>
       <nav className="navbar navbar-expand-sm p-3 fixed-top">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">
            <img src={logo} alt="HK Logo" className="logo-img" style={{"width":'90px'}}/> 
          </a>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="collapsibleNavbar">
              <ul className="navbar-nav">
                <li className="nav-item ps-5">
                 
                  <Link className='nav-link' to="/">Home</Link>
                </li>
                <li className="nav-item ps-5">
             
                    <Link className='nav-link' to="/home/products">Products</Link>

                  </li>
                <li className="nav-item ps-5">
                <i className="fa fa-sign-out" aria-hidden="true"></i>
                  <a className="nav-link" href="#">REGISTER</a>
                </li>
                <li className="nav-item ps-5">
                <i className="fa fa-sign-in" aria-hidden="true"></i>
                  <a className="nav-link" href="#">SIGIN</a>

                </li>

                <li className="nav-item ps-5">
                <i className="fa fa-shopping-cart" aria-hidden="true"></i>
                  <a className="nav-link" href="#">Cart</a>

                </li>
             
              </ul>
              <form className="d-flex ms-auto nav-item search-form">
                <div className="search-wrapper">
                  <input className="form-control me-2 p-1 ps-2" type="text" placeholder="Search"/>
                  <button type="submit" className="search-button">
                    <i className="fa fa-search"></i>
                  </button>
                </div>
              </form>
              
            <div className="dropdown nav-item">
                <button type="button" className="btn dropdown-toggle border-0" data-bs-toggle="dropdown">
                    <i className="fa-regular fa-user border border-3 border-dark rounded-circle"></i>
                </button>
                <ul className="dropdown-menu dropdown-menu-center">

                  <Popup trigger={
                    <li><a className="dropdown-item" href="#"><i className="fa fa-user" aria-hidden="true"></i> Profile</a></li> }>
                      <Profile/>
                  </Popup>
                  
                
                  <li><a className="dropdown-item" href="#">
                  <i className="fa fa-sign-out" aria-hidden="true"></i>  Register</a></li>
                  <li><hr className="dropdown-divider"/></li>
                  <li>
                    <a className="dropdown-item" href="#">
                  <i className="fa fa-sign-in" aria-hidden="true"></i> Sign in</a>
                    </li>
                </ul>
              </div>
            </div>
          </div>
        
        
    </nav>

    </div>
  )
}
