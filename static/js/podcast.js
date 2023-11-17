/* Mostrar reproductor*/
        function showAudioPlayer() {
            document.getElementById('audioPlayer').style.display = 'block';
        }

        function closeAudioPlayer() {
            document.getElementById('audioPlayer').style.display = 'none';
        }
  

 /*Botones de reproductor*/       
        var song = new Audio;
        var muted = false;
        var vol = 1;
        song.type = 'audio/mpeg';
        song.src = '/get_audio'; // Aquí es donde puedes cambiar la URL de la música

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