document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelectorAll('.my-slide');
  let currentSlideIndex = 0;

  function showNextSlide() {
    slides[currentSlideIndex].classList.remove('my-active');
    currentSlideIndex = (currentSlideIndex + 1) % slides.length;
    slides[currentSlideIndex].classList.add('my-active');
  }

  if (slides.length > 0) {
    setInterval(showNextSlide, 3000); // Change slide every 3 seconds
  }

  const images = document.querySelectorAll('.why-us-img');
  let currentImageIndex = 0;

  function showNextImage() {
    images[currentImageIndex].classList.remove('active');
    currentImageIndex = (currentImageIndex + 1) % images.length;
    images[currentImageIndex].classList.add('active');
  }

  if (images.length > 0) {
    setInterval(showNextImage, 6000); // Change image every 6 seconds
  }
});
