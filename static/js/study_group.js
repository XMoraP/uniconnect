$(document).ready(function() {
    // Handle form submission
    $('#studyGroupForm').submit(function(e) {
      e.preventDefault();
  
      // Get form data
      const formData = {
        title: $('#title').val(),
        subject: $('#subject').val(),
        description: $('#description').val(),
        location: $('#location').val(),
        days: $('#days').val(),
        time: $('#time').val()
      };
  
      // Send data to Flask backend using AJAX
      $.ajax({
        type: 'POST',
        url: '/create_study_group',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify(formData),
        success: function(response) {
            // Handle success, e.g., display a success message
            console.log(response);

            // Append the new study group to the table
            $('#studyGroupTableBody').append(
                `<tr>
                    <td>${formData.title}</td>
                    <td>${formData.subject}</td>
                    <td>${formData.description}</td>
                    <td>${formData.location}</td>
                    <td>${formData.days}</td>
                    <td>${formData.time}</td>
                </tr>`
                );

            $('#createStudyGroupModal').modal('hide');
        },
        error: function(error) {
          // Handle error, e.g., display an error message
          console.error(error);
        }
      });
    });
  });
  