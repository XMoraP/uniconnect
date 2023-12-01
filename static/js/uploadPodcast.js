const startButton = document.getElementById('startRecord');
const stopButton = document.getElementById('stopRecord');
const saveButton = document.getElementById('saveRecord'); // Nuevo botón de guardar
const audioPlayer = document.getElementById('audioPlayer');

let mediaRecorder;
let audioChunks = [];

startButton.addEventListener('click', startRecording);
stopButton.addEventListener('click', stopRecording);
saveButton.addEventListener('click', saveRecording); // Nuevo evento para el botón de guardar

function startRecording() {
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      mediaRecorder = new MediaRecorder(stream);

      mediaRecorder.ondataavailable = event => {
        if (event.data.size > 0) {
          audioChunks.push(event.data);
        }
      };

      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        const audioUrl = URL.createObjectURL(audioBlob);
        audioPlayer.src = audioUrl;
        saveButton.disabled = false; // Habilitar el botón de guardar cuando la grabación se detiene
      };

      mediaRecorder.start();
      startButton.disabled = true;
      stopButton.disabled = false;
      saveButton.disabled = true; // Deshabilitar el botón de guardar al iniciar la grabación
    })
    .catch(error => console.error('Error al acceder al micrófono:', error));
}

function stopRecording() {
  mediaRecorder.stop();
  startButton.disabled = false;
  stopButton.disabled = true;
}

function saveRecording() {
  // Envía el archivo de audio al servidor al presionar "Guardar"
  sendAudioToServer(audioChunks);
}

function sendAudioToServer(chunks) {
  // Convertir los chunks en un Blob
  const audioBlob = new Blob(chunks, { type: 'audio/wav' });

  // Crear un formulario para enviar el Blob como parte del cuerpo de la solicitud
  const formData = new FormData();
  formData.append('audio', audioBlob);
  formData.append('nombre_usuario', 'nombre_predeterminado'); // Puedes ajustar esto según tus necesidades

  // Enviar la solicitud al servidor
  fetch('/subir_audio', {
    method: 'POST',
    body: formData
  })
  .then(response => response.text())
  .then(message => {
    console.log(message);

    // Cerrar el modal y recargar la página después de enviar al servidor
    const modal = document.getElementById('recordPodcastModal'); // Reemplaza 'tuModalId' con el ID real de tu modal
    modal.style.display = 'none';
    location.reload();
  })
  .catch(error => console.error('Error al enviar el archivo de audio:', error));
}
