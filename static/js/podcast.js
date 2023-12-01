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
        });

        

