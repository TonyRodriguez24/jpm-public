document.addEventListener("DOMContentLoaded", () => {
    if (window.location.hash === "#Form-container") {
        const form = document.getElementById("Form");
        if (form) {
            const headerHeight = document.querySelector("header")?.offsetHeight || 0;
            window.scrollTo({
                top: quickForm.offsetTop - headerHeight,
                behavior: "smooth"
            });
        }
    }
});
