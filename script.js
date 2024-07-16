// script.js
document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelectorAll('.my-slide');
  let currentIndex = 0;

  function showNextSlide() {
    slides[currentIndex].classList.remove('my-active');
    currentIndex = (currentIndex + 1) % slides.length;
    slides[currentIndex].classList.add('my-active');
  }

  setInterval(showNextSlide, 3000); // Change slide every 3 seconds

});


$(document).ready(function() {
  $("#landing-page").css("visibility", "visible").animate({opacity: 1}, 2000);
});


$("#contact-form").on("submit", function(e){
  // Check if the form is valid
  if (this.checkValidity()) {
    e.preventDefault();
    $("#contact-form").hide();  
    $("#form-success-container").show();
    $(".form-container h2").text("JPM and Sons");
  } else {
    // If the form is not valid, let the browser handle the validation
    // This will show the validation messages for required fields
    $(this).find(":submit").click(); 
  }
});
