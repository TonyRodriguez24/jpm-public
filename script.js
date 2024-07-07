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


$("#landing-page").fadeIn(2000);
