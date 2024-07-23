document.addEventListener('DOMContentLoaded', () => {
  const observerOptions = {
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  const observeImages = (selector) => {
    document.querySelectorAll(selector).forEach(img => {
      // Check if the image is already in view
      if (img.getBoundingClientRect().top < window.innerHeight) {
        img.classList.add('fade-in');
      } else {
        observer.observe(img);
      }
    });
  };

  // Observe images in the entire gallery
  observeImages('#entire-gallery img');

  // Observe images in the front page gallery
  observeImages('#gallery-container .gallery img');
});
