import React, {useEffect, useState} from 'react'
// import './Slider.css'
import "../assests/styles/slider.css";
import BtnSlider from './BtnSlider'
import ethic from "../assests/images/ethic.jpeg"


export default function Slider() {

     const dataSlider= [

      
        {
          id: 2,
          img: "https://sslimages.shoppersstop.com/sys-master/images/hbd/hf7/29301867216926/S23BILSPA1866YE_YELLOW.jpg_2000Wx3000H",
          title: "SUMMER SALE",
          desc: "DON'T COMPROMISE ON STYLE! GET FLAT 30% OFF FOR NEW ARRIVALS.",
          bg: "f5fafd",
        },
        {
          id: 3,
          img: "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg",
          title: "AUTUMN COLLECTION",
          desc: "DON'T COMPROMISE ON STYLE! GET FLAT 30% OFF FOR NEW ARRIVALS.",
          bg: "fcf1ed",
        },
        {
          id: 4,
          img: "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_.jpg",
          title: "LOUNGEWEAR LOVE",
          desc: "DON'T COMPROMISE ON STYLE! GET FLAT 30% OFF FOR NEW ARRIVALS.",
          bg: "fbf0f4",
        },
      ];
    





    // const [dataSlider,setdataSlider]=useState([])
    // useEffect(()=>{
    //     fetch('https://fakestoreapi.com/products')
    //         .then(res=>res.json())
    //         .then(
                
    //             json=>{
    //                 setdataSlider(json)
    //                 // console.log(json)
    //             }
    //                 )
    //         .catch(err=>console.log(err))



    // },[])


    console.log(dataSlider.length,"sASAsA")




    const [slideIndex, setSlideIndex] = useState(1)

    const nextSlide = () => {
        if(slideIndex !== dataSlider.length){
            setSlideIndex(slideIndex + 1)
        } 
        else if (slideIndex === dataSlider.length){
            setSlideIndex(1)
        }
    }

    const prevSlide = () => {
        if(slideIndex !== 1){
            setSlideIndex(slideIndex - 1)
        }
        else if (slideIndex === 1){
            setSlideIndex(dataSlider.length)
        }
    }

    const moveDot = (index:number) => {
        setSlideIndex(index)
    }

    return (
        <>
        
        <div className="container-slider">
            <BtnSlider moveSlide={prevSlide} direction={"prev"}/>
            {dataSlider.map((obj, index:number) => {
                return (
                    <div
                    key={index}
                    className={slideIndex === index + 1 ? "slide active-anim " : "slide"}
                    style={{ backgroundImage:`url("${obj.img}")`, 
                    backgroundSize: "cover",
                    backgroundRepeat: "no-repeat",}}
                       >
                        <div >
                <div className='mx-auto'>
                <button className='btn btn-outline-secondary'>Shop Now</button>
                </div>
                            
                        </div>
                  
                    </div>
                )
            })}
            <BtnSlider moveSlide={nextSlide} direction={"next"} />

        </div>
            <div className="container-dots">
                {Array.from({length: 3}).map((item, index) => (
                    <div key={index}
                    onClick={() => moveDot(index + 1)}
                    className={slideIndex === index + 1 ? "dot-active" : "dot"}
                    ></div>
                ))}
            </div>
      
        </>

    )
}