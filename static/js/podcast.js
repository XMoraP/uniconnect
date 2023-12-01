        // Obtener el ID del podcast del contenedor del reproductor de audio actual
        var cardElements = document.querySelectorAll('.card');

        // Itera sobre cada elemento y configura la fuente del audio
        cardElements.forEach(function(cardElement) {
            // Obtiene el ID del podcast desde el atributo de datos del elemento actual
            var currentPodcastId = cardElement.dataset.podcastId;
        
            // Configura la fuente del audio para el elemento de esta tarjeta
            var song = cardElement.querySelector('audio');
            if (song) {
                song.src = '/get_audio/' + currentPodcastId;
            }
<<<<<<< HEAD
        });
=======
        });
        
        function skip(time) {
            if (time == 'back') {
                song.currentTime = (song.currentTime - 5);
            } else if (time == 'fwd') {
                song.currentTime = (song.currentTime + 5);
            }
        }

        function playpause() {
            if (!song.paused) {
                song.pause();
            } else {
                song.play();
            }
        }

        function stop() {
            song.pause();
            song.currentTime = 0;
            document.getElementById('seek').value = 0;
        }

        function setPos(pos) {
            song.currentTime = pos;
        }

        function mute() {
            if (muted) {
                song.volume = vol;
                muted = false;
                document.getElementById('mute').innerHTML = '<i class="fa fa-volume-up"></i>';
            } else {
                song.volume = 0;
                muted = true;
                document.getElementById('mute').innerHTML = '<i class="fa fa-volume-off"></i>';
            }
        }

        function setVolume(volume) {
            song.volume = volume;
            vol = volume;
        }

        song.addEventListener('timeupdate', function () {
            curtime = parseInt(song.currentTime, 10);
            document.getElementById('seek').max = song.duration;
            document.getElementById('seek').value = curtime;
        })

/* GRABAR*/
document.addEventListener('DOMContentLoaded', function() {
    const addPodcast = document.getElementById('addPodcastModal');
    const startRecordingBtn = document.getElementById('startRecording');
    const voiceRecordingModal = document.getElementById('voiceRecordingModal');

    startRecordingBtn.addEventListener('click', function() {
        $('#addPodcast').modal('hide'); 
        $('#voiceRecordingModal').modal('show'); // Mostrar el modal de grabación de voz
        initRecorder(); // Iniciar la grabación de voz
    });

    function initRecorder() {
        let mediaRecorder;
        let chunks = [];
        const audioElement = document.getElementById('audioElement');
        const startRecordingBtn = document.getElementById('startRecordingBtn');
        const stopRecordingBtn = document.getElementById('stopRecordingBtn');

        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(function(stream) {
                mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.ondataavailable = function(e) {
                    chunks.push(e.data);
                };

                mediaRecorder.onstop = function() {
                    const blob = new Blob(chunks, { type: 'audio/ogg; codecs=opus' });
                    chunks = [];
                    const audioURL = window.URL.createObjectURL(blob);
                    audioElement.src = audioURL;
                };

                startRecordingBtn.addEventListener('click', function() {
                    mediaRecorder.start();
                    startRecordingBtn.disabled = true;
                    stopRecordingBtn.disabled = false;
                });

                stopRecordingBtn.addEventListener('click', function() {
                    mediaRecorder.stop();
                    startRecordingBtn.disabled = false;
                    stopRecordingBtn.disabled = true;
                });
            })
            .catch(function(err) {
                console.error('Error al obtener el acceso al micrófono:', err);
            });
    }
});


        

>>>>>>> refs/remotes/origin/main
