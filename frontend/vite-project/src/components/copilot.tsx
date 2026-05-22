import Markdown from 'react-markdown';
import Button from './button'
import './copilot.css'
import { useState, useRef } from "react";

function CoPilot(props: any) {
  const inputRef = useRef<HTMLInputElement | null>(null); //ref hook to access the input element, initialized with null
  const [textres, setTextres] = useState("Response will appear here..."); //state hook for the response text, initialized with a default message

async function handleSubmit() {
  const message = inputRef.current?.value;
  if (textres === "Response will appear here...") {
    setTextres(""); // Clear the default message on first response
  }

  if (!message) return;

  const res = await fetch("http://127.0.0.1:8000/users/res", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      prompt: message
    })
  });
  if (!res.ok) {
    console.error("Failed to fetch response");
    return;
  }

  const reader = res.body.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);

    setTextres((prev) => prev + chunk);

  }
  setTextres((prev) => prev + "\n\n"); // Optionally indicate the end of the response
}


  return (
    <>
    <div className="coPilot_container" {...props}>
        <div className="response_box">
          <div className="reply_display">
            <Markdown>{textres}</Markdown>
            </div>
        </div>
        <div className="input_box">
            <input ref={inputRef} type="text" placeholder="Ask me anything..." />
            <Button text="Send" onClick={handleSubmit}/>
        </div>
    </div>
    </>
  )
}

export default CoPilot
