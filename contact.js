$(document).ready(function() {
    // Initialize EmailJS
    emailjs.init("PWX9hwKjZs3ZUe5V3");
  
    // Form submission handling
    $("#contact-form").on("submit", function(e) {
      e.preventDefault();
  
      // Send the form using EmailJS
      emailjs.sendForm('service_88k82ug', 'template_llnmo1o', '#contact-form')
        .then((response) => {
          console.log('SUCCESS!', response.status, response.text);
          $("#contact-form").hide();  
          $("#form-success-container").show();
          $(".form-container h2").text("JPM and Sons");
        }, (error) => {
          console.log('FAILED...', error);
          alert('There was an error sending your message.');
        });
    });
  });
  