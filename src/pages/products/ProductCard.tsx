import React, { useEffect, useState } from 'react'
import '../../assests/styles/product.css'

import 'font-awesome/css/font-awesome.min.css';

const ProductCard=({result}:any)=>{
    console.log(result,"asdassasasaasasas")

    const [response,setResponse]=useState(result)
    console.log(response,"asdassasasaasasas")
    return(
        
       
                <div className="card p-3 prod-card  mb-5" style={{width: "18rem",height:"30rem"}}>
								<span className="wish-icon"><i className="fa fa-heart-o"></i></span>
								<div className="img-box">
									<img src={response.image} className="img-fluid" alt="Galaxy" style={{width:"100px",height:"100px"}}/>
								</div>
								<div className="thumb-content">
									<h4>{response.title}</h4>
									<p className="item-price"><span>${response.price}</span></p>
									<div className="star-rating">
										<ul className="list-inline">
											<li className="list-inline-item"><i className="fa fa-star"></i></li>
											<li className="list-inline-item"><i className="fa fa-star"></i></li>
											<li className="list-inline-item"><i className="fa fa-star"></i></li>
											<li className="list-inline-item"><i className="fa fa-star"></i></li>
											<li className="list-inline-item"><i className="fa fa-star-o"></i></li>
										</ul>
									</div>
									<a href="#" className="btn btn-primary">Add to Cart</a>
								</div>						
							</div>
                            
                
          
    

    )
}


export default ProductCard