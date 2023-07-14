

import React from "react";
import "../assests/styles/slider.css";

import 'font-awesome/css/font-awesome.min.css';


interface btnSliderType{
    direction:string,
    moveSlide:any
}




export default function BtnSlider(props:btnSliderType) {

    const { direction, moveSlide }=props;
  // console.log(direction, moveSlide);
  return (
    <>
   
    <button
      onClick={moveSlide}
      className={direction == "next" ? "btn-slide next" : "btn-slide prev"}
    >
        {direction == "next" ?<i className="fa fa-chevron-right" aria-hidden="true"></i> :<i className="fa fa-chevron-left" aria-hidden="true"></i>}

    </button>

    </>
  );
}