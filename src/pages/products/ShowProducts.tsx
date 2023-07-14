import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { BaseApi,headers } from '../../utils/baseApi'
import ProductCard from './ProductCard'
// import '../../assests/styles/product.css'





export default function ShowProducts({result}:any) {

    const [category,setCategory]=useState([])
    const [data,setData]=useState(result)
    const [loading,setLoading] = useState(true)
    const [selectedcategory,setselectedcategory] = useState<string>('All')
    

    useEffect(()=>{

        const getcategory=async()=>{
            try{
                let url=BaseApi+'home/api/category-list/'
                let response= await axios.get(url,{headers})
            
                setCategory(response.data)
                setLoading(false)
            }
            catch(e){
                console.log(e)
            }


        }

        const getcategoryProducts = async()=>{
            try{
          
                // let url=BaseApi+''
                let result;
               if( selectedcategory == 'All'){
                   result = await axios.get('https://fakestoreapi.com/products/')
                  

               }
               else{
                    result = await axios.get(`https://fakestoreapi.com/products/category/${selectedcategory}`) 

               }
               setLoading(false)
               console.log(result.data,"dat")

                setData(result.data)
            }
            catch(e){
                console.log(e)
            }

        }

        getcategory()
        getcategoryProducts()
    },[selectedcategory])

    // console.log(data,"dssdadasas====================================")

        
  return (
    <div>
      
                <div className="d-flex justify-content-center ">
            <div className='buttons'>

            <button  className={ 'All'==selectedcategory ?"btn btn-outline dark me-2 btn-dark ": "btn btn-outline dark me-2 btn-light"} onClick={()=>setselectedcategory('All')}>
                 All
                    </button>
                {
                    loading ? <div></div>:
              
                    
            category.map((item:any,index)=>(

                   

                    <button   key={item.id}  id={item.category_name} className={ item.category_name==selectedcategory ?"btn btn-outline dark me-2 btn-dark ": "btn btn-outline dark me-2 btn-light"}
                    onClick={()=>setselectedcategory(item.category_name)}>
                        {item.category_name}
                    </button>
                    
         
            )
     )
                
           
             }
              </div>
            </div>


            {
                loading?<div>asSsASAs</div>
                :
                <div className='d-flex flex-row flex-wrap m-5 ' style={{justifyContent:"space-around"}}>
                 
                    {
                        data.map((value:any,index:number)=>{

                        // {console.log(value,"asdasdasdasdasdasas")}
                        return(

                            <div key={value.id}>
                                <ProductCard result={value}/>

                            </div>
                        )
                      
                        })
                    }
                </div>
            }



    </div>
  )
}
