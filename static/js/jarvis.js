document.addEventListener('DOMContentLoaded', function() {
    const talkButton = document.querySelector('.talk');
    const stopButton = document.querySelector('.stop');
    const recognition = new webkitSpeechRecognition();
    recognition.lang = 'es-ES';
    recognition.interimResults = false;
    recognition.continuous = false;
    recognition.maxAlternatives = 1;
    const speechSynthesis = window.speechSynthesis;
    let speaking = false;
    let utterance;
    let firstTime = true;

    function welcomeMessage() {
        const userName = talkButton.getAttribute('data-username');
        const welcomeText = `Hola ${userName}, Bienvenido a Uniconnect, soy tu asistente virtual Jarvis. ¿En qué puedo ayudarte?`;
        speak(welcomeText);
        firstTime = false;
    }

    talkButton.addEventListener('click', function() {
        
        if (!speaking) {
            if (firstTime) {
                welcomeMessage();
            } else {
                recognition.start();
            }
            speaking = true;
        } else {
            recognition.start();
        }

        recognition.onresult = function(event) {
            const userInput = event.results[0][0].transcript;

            fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ input: userInput })
            })
                .then(response => response.json())
                .then(data => {
                    if (speaking) {
                        speak(data.response);
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        };
    });

    stopButton.addEventListener('click', function() {
        speaking = false;
        if (utterance) {
            speechSynthesis.cancel();
        }
    });

    function speak(text) {
        utterance = new SpeechSynthesisUtterance(text);
        speechSynthesis.speak(utterance);
    }
});
