import { useState } from "react";
import { TextField, Button } from "@mui/material";

export default function InputPage () {
    const [inputText, setInputText] = useState("");
    const handleSend = () => {
        fetch("backend-url", {
            method: "POST",
            body: JSON.stringify({ text: inputText }),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
    }

    return (
        <div>
            <TextField
                label="Input Text"
                value={inputText}
                onChange={(event) => setInputText(event.target.value)}
            />
            <Button variant="text" onClick={handleSend}>Send</Button>
        </div>
    );
}