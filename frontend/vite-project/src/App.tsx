import { useState, useEffect, useRef } from "react";

import CoPilot from './components/copilot'
import Header from './components/header'

import { StrictMode } from 'react'
import './App.css'


function App() {
  const [width, setWidth] = useState(300);
  const [dragging, setDragging] = useState(false);
  const refOffset = useRef(0); // Ref to store the initial offset during dragging

  const containerRef = useRef<HTMLDivElement | null>(null); // Ref to the container div

  const startDrag = (event: React.MouseEvent) => {
  
    setDragging(true)
    const rect = containerRef.current?.getBoundingClientRect();

    if(!rect) return;

    refOffset.current = event.clientX - width; // Calculate the initial offset
    console.log("offset: ", refOffset.current);

  };
  const stopDrag = () => setDragging(false);

  useEffect(() => {
    const onMove = (e: MouseEvent) => {
      if (!dragging) return;

      const rect = containerRef.current?.getBoundingClientRect();
      if (!rect) return;
      
      // const local_mouse_pos = e.clientX - rect.left;
      const newWidth = e.clientX - rect.left - refOffset.current; // Calculate the new width based on the mouse position and initial offset


      // TO DO: Convert to percentages
      if(newWidth <= 100){ // Lower boundary
        setWidth(100);
      }
      else if(newWidth >= 1000){ // Higer boundary
        setWidth(1000);
      }
      else{setWidth(newWidth)}
    };


    window.addEventListener("mousemove", onMove); //need clerafication on this, should it be on the containerRef.current instead of window?
    window.addEventListener("mouseup", stopDrag);

    return () => {
      window.removeEventListener("mousemove", onMove);
      window.removeEventListener("mouseup", stopDrag);
    };
  }, [dragging]);


  return (
    <>
    <div className="App">
      <StrictMode>
        <div className='container' ref={containerRef} style={{ '--width': `${width}px`} as React.CSSProperties}>
            <Header style={{gridColumn: "1 / span 3", zIndex: 1}}/>
            <div style={{zIndex: 0}} id='sideBar' className='item'/>
            <div style={{zIndex: 0}} id='dragger' className='item' onMouseDown={startDrag}/>
            <div style={{zIndex: 0}} id='content' className='item'>
              <CoPilot></CoPilot>
            </div>
        </div>
      </StrictMode>
    </div>
    </>
  )
}

export default App