const chatBox = document.getElementById('chat-box');
const sendBtn = document.getElementById('send-btn');
const userInput = document.getElementById('user-input');
const voiceBtn = document.getElementById('voice-btn');

// Append a message to the chat box
function appendMessage(message, isUser) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    messageDiv.classList.add(isUser ? 'user-message' : 'bot-message');
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
}

// Handle sending text messages
sendBtn.addEventListener('click', () => {
    const message = userInput.value.trim();
    if (message) {
        appendMessage(message, true); // Append user message
        userInput.value = ''; // Clear input field
        fetchMessageFromBot(message); // Fetch bot response
    }
});

// Fetch the bot's response from Rasa server
async function fetchMessageFromBot(message) {
    try {
        const response = await fetch('http://localhost:5005/webhooks/rest/webhook', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message }) // Send message to Rasa
        });

        const botMessages = await response.json(); // Get bot responses
        botMessages.forEach(botMsg => {
            appendMessage(botMsg.text, false); // Append bot message
            speak(botMsg.text); // Speak bot response
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

// Voice recognition setup
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'en-US'; // Set recognition language
recognition.interimResults = false; // Final results only

// Start voice recognition on button click
voiceBtn.addEventListener('click', () => {
    recognition.start(); // Start voice recognition
});

// Handle voice recognition results
recognition.onresult = (event) => {
    const voiceMessage = event.results[0][0].transcript; // Get recognized text
    appendMessage(voiceMessage, true); // Append user message
    fetchMessageFromBot(voiceMessage); // Fetch bot response
};

// Handle recognition errors
recognition.onerror = (event) => {
    console.error('Speech Recognition Error:', event.error);
    appendMessage('Sorry, I could not understand. Please try again.', false);
};

// Speak bot's response
function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text); // Create speech synthesis utterance
    utterance.lang = 'en-US'; // Set speech language
    window.speechSynthesis.speak(utterance); // Speak the text
}
