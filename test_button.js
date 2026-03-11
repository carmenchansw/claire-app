// script.js
const btn = document.getElementById('listenButton');
const output = document.getElementById('output');

btn.onclick = async () => {
    // 1. Update UI to show we are listening
    btn.disabled = true;
    btn.innerText = "Listening...";
    output.innerText = "Please speak into your microphone...";

    try {
        // 2. Call your Python Flask server
        const response = await fetch('http://127.0.0.1:5000/transcribe');
        const data = await response.json();
        
        // 3. Display the result
        if (data.status === "success") {
            output.innerText = data.text;
        } else {
            output.innerText = "Error: " + data.message;
        }
    } catch (err) {
        output.innerText = "Connection failed. Is app.py running?";
        console.error(err);
    } finally {
        // 4. Reset the button
        btn.disabled = false;
        btn.innerText = "Click to Speak";
    }
};