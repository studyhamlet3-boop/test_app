import Button from './button'
import './header.css'
import { useState } from "react";


function Header(props: any) {
    const [isPanelOpen, setPanelState] = useState(true);

    function togglePanel(){
        setPanelState(!isPanelOpen);
        if (isPanelOpen){
            console.log("closing panel")
        }
        else{
            console.log("opening panel")
        }
    }

  return (
    <>
    <div className="header_container" {...props}>
        <div className="header_main">
            <Button text="Header" onClick={togglePanel}/>
            <div className={isPanelOpen ? "panel" : "panel open"}></div>
        </div>
    </div>
    </>
  )
}

export default Header
