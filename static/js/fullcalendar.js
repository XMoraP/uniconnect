document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: '/get_events',  // Load events from the /get_events route

        eventClick: function(info) {
            // Handle event click here (optional)
            console.log(info.event.title);
        }
    });

    calendar.render();
});