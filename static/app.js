document.addEventListener("DOMContentLoaded", function () {
    // Automatically scroll to the flash messages if they exist
    const flashMessage = document.querySelector(".alert");
    if (flashMessage) {
        const offset = 150; // Adjust this value to add spacing above the message
        const flashPosition = flashMessage.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top: flashPosition, behavior: "smooth" });
    }
});