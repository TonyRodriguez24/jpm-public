document.addEventListener("DOMContentLoaded", () => {
    if (window.location.hash === "#ContactForm") {
        const form = document.getElementById("Form");
        if (form) {
            const headerHeight = document.querySelector("header")?.offsetHeight || 0;
            window.scrollTo({
                top: quickForm.offsetTop - headerHeight,
                behavior: "smooth"
            });
        }
    }

    const deleteModal = document.getElementById('deleteModal');
    const deleteForm = document.getElementById('deleteForm');
    const deleteItemType = document.getElementById('deleteItemType');

    deleteModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget; // Button that triggered the modal
        const id = button.getAttribute('data-id'); // Get ID from data-id
        const type = button.getAttribute('data-type'); // Get type (contact/project)

        // Update modal content
        deleteItemType.textContent = type === 'contact' ? 'contact' : 'project';

        // Update the form's action URL
        deleteForm.action = type === 'contact' ? `/admin/delete-contact/${id}` : `/admin/delete-project/${id}`;
    });

});
