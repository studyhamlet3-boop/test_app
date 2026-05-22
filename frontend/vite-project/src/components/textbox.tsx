// <!-- From Uiverse.io by Ashon-G --> 

// import { useState } from 'react'
import './textbox.css'

function TextBox() {

  return (
    <>
    <div className="form__group field">
    <input
        id = "name"
        type="text"
        className="form__field"
        placeholder="Name"
        required
    />
    <label htmlFor="name" className="form__label">
        Name
    </label>
    </div>
    
    </>
  )
}

export default TextBox
