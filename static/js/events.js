$(document).ready(function() {
    // Function to add a new event item
    function addEventItem(eventName, eventDate, eventTime) {
        const eventList = document.getElementById('eventList');
        const newItem = document.createElement('li');
        newItem.classList.add('event-item'); // Add a class for event items
        newItem.innerHTML = `
            <span>
                <span class="name_user">${eventName}</span>
                <span class="msg_user">Fecha: ${eventDate}</span>
                <span class="msg_user">Hora: ${eventTime}</span
            </span>`;
        eventList.appendChild(newItem);

        // Attach event deletion handler to the delete button
        const deleteButtons = document.querySelectorAll('.delete-button');
        deleteButtons.forEach(function (button) {
            button.addEventListener('click', function () {
                const eventItem = button.closest('.event-item');
                if (eventItem) {
                    eventList.removeChild(eventItem);
                }
            });
        });
    }

    // Add Event Button Click Event to open the modal
    const openAddEventModalButton = document.getElementById('openAddEventModalButton');
    if (openAddEventModalButton) {
        openAddEventModalButton.addEventListener('click', function () {
            // Clear the form fields when the modal is opened
            document.getElementById('eventName').value = '';
            document.getElementById('eventDate').value = '';
        });
    }

    // Save Event Button Click Event to add a new event
    const saveEventButton = document.getElementById('saveEventButton');
    if (saveEventButton) {
        saveEventButton.addEventListener('click', function () {
            // Get event details from the form
            const eventName = document.getElementById('eventName').value;
            const eventDate = document.getElementById('eventDate').value;
            const eventTime = document.getElementById('eventTime').value;

            // Add the new event item to the list
            if (eventName && eventDate && eventTime) {
                addEventItem(eventName, eventDate, eventTime);

                // Close the modal
                $('#addEventModal').modal('hide');
            }
        });
    }
});
