$(document).ready(function() {
    // Store created courses in an array
    var courses = [];

    // Function to add a new course container
    function addCourseContainer(title, description, classroom, teacher, image, documents) {

        var courseContainer = document.createElement('div');
        courseContainer.className = 'course-card';

        // Check if an image is provided, otherwise set a default image source
        var imageSource = image ? image : '../static/images/default_image.jpg';
        var imageAlt = image ? 'Course Image' : 'Default Image'; // Define the alt text
        
        // Create the course container content
        var content = `
            <!-- Course Image -->
            <img class="course-image" src="${imageSource}" alt="${imageAlt}">
            <!-- Course Content -->
            <div class="course-content">
                <!-- Course Title -->
                <div class="course-title"><h4>${title}</h4></div>
                <!-- Course Description -->
                <div class="course-description"><p><strong>Descripción: </strong>${description}</p></div>
                <!-- Course Details (classroom, teacher, weekdaysTime) -->
                <div class="course-details">
                    <strong>Aula: </strong>${classroom}<br>
                    <strong>Profesor/a: </strong>${teacher}
                </div>
                <!-- ... (Other content) ... -->
            </div>
        `;

        courseContainer.innerHTML = content;
        // Append the course container to the main content
        document.getElementById('courseContainers').appendChild(courseContainer);

        // Add hover effect and click event to open modal
        $(courseContainer).hover(function () {
            $(this).css('cursor', 'pointer');
        }).click(function () {
            // Open the modal with course details
            // You can implement this part using Bootstrap modal functionality
            // Example: $('#courseModal').modal('show');
        });

        // Add click event to delete the course
        $(courseContainer).find('#deleteCourse').click(function (event) {
            event.stopPropagation(); // Prevent the click event from propagating to the container
            // Implement course deletion logic here
        });
        
    }

    // Event listener for the "Guardar" button
    $('#saveCourse').on('click', function () {
        var title = $('#courseTitle').val();
        var description = $('#courseDescription').val();
        var classroom = $('#classroomInput').val();
        var teacher = $('#teacherInput').val();
        var image = $('#courseImage').val(); // Get the image source
        // var weekdaysTime = $('#weekdaysTimeInput').val();
        var documents = $('#courseDocument').val();

        // Create a new course object and add it to the courses array
        var course = {
            title: title,
            description: description,
            classroom: classroom,
            teacher: teacher,
            image: image, // Store the image source
            // weekdaysTime: weekdaysTime,
            documents: documents
        };
        courses.push(course);

        // Add the course container to the page
        addCourseContainer(title, description, classroom, teacher, image, documents);

        // Close the modal
        $('#addCourseModal').modal('hide');

        // Clear the form fields
        $('#courseTitle').val('');
        $('#courseDescription').val('');
        $('#classroomInput').val('');
        $('#teacherInput').val('');
        $('#courseImage').val('');
        // $('#weekdaysTimeInput').val('');
        $('#courseDocument').val('');
    });


});