
import React from 'react';
import { Route,RouterProvider,createBrowserRouter,createRoutesFromElements } from 'react-router-dom';

import Home from './pages/home/Home';
import MainProductPage from './pages/products';
import PopupGfg from './pages/profile/Profile'

const PublicRoutes=()=>{
  

const router=createBrowserRouter(
    createRoutesFromElements(
        <Route path='/'>

            <Route path='' element={<Home/>}/>
            <Route path='home/products' element={<MainProductPage/>}/>
            <Route path='profile' element={<PopupGfg/>}/>



        </Route>
    )
)
return (<>
 
<RouterProvider router={router}/>
</>
)

}


export default PublicRoutes