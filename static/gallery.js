document.addEventListener("DOMContentLoaded", () => {
    // Select the loading screen and gallery container
    const loadingScreen = document.getElementById("loading-screen");
    const gallery = document.getElementById("gallery");

    // Ensure the spinner is removed and the gallery is displayed after DOM is loaded
    if (loadingScreen && gallery) {
        setTimeout(() => {
            loadingScreen.style.display = "none"; // Completely hide the loading screen
            gallery.classList.remove("hidden"); // Remove 'hidden' class to show the gallery
        }, 1000); // Optional delay for better UX, adjust as needed
    }

    const options = { threshold: 0.1 };

    // Intersection Observer to handle the fade-in effect
    const observer = new IntersectionObserver((entries, observerInstance) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                const img = entry.target;

                // Add fade-in class after the image is fully loaded
                if (img.complete) {
                    img.classList.add("fade-in");
                } else {
                    img.onload = () => img.classList.add("fade-in");
                }

                observerInstance.unobserve(img); // Stop observing once the effect is applied
            }
        });
    }, options);

    // Initialize the observer for images in the gallery
    if (gallery) {
        const images = document.querySelectorAll("#gallery img");
        images.forEach((img) => observer.observe(img));
    }
});
