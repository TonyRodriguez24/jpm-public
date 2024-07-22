document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelectorAll('.my-slide');
  let currentIndex = 0;

  function showNextSlide() {
    slides[currentIndex].classList.remove('my-active');
    currentIndex = (currentIndex + 1) % slides.length;
    slides[currentIndex].classList.add('my-active');
  }

  if (slides.length > 0) {
    setInterval(showNextSlide, 3000); // Change slide every 3 seconds
  }
});

$(document).ready(function () {
  let currentIndex = 0;
  const images = $('.why-us-img');
  const imageCount = images.length;

  setInterval(function () {
    const nextIndex = (currentIndex + 1) % imageCount;
    $(images[currentIndex]).removeClass('active');
    $(images[nextIndex]).addClass('active');
    currentIndex = nextIndex;
  }, 6000); // Change image every 3 seconds
});