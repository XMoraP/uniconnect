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
          $('#createStudyGroupModal').modal('hide');
        },
        error: function(error) {
          // Handle error, e.g., display an error message
          console.error(error);
        }
      });
    });
  });
  