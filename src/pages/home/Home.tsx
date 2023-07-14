import React from 'react'
import Slider from '../../components/Slider'
import Products from '../products/Products'
import Navbar from '../../components/Navbar'


const Home=()=>{


  return(
    
    <div className='main-home-page'>
      <Navbar/>
        
          <Slider/>
          <Products/>



        
      

    </div>
  )
}




export default Home