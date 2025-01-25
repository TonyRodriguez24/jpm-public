document.addEventListener("DOMContentLoaded", () => {
    try {
        const deleteModal = document.getElementById('deleteModal');
        const deleteForm = document.getElementById('deleteForm');
        const deleteItemType = document.getElementById('deleteItemType');

        if (deleteModal && deleteForm && deleteItemType) {
            deleteModal.addEventListener('show.bs.modal', function (event) {
                const button = event.relatedTarget; // Button that triggered the modal
                const id = button.getAttribute('data-id'); // Get ID from data-id
                const type = button.getAttribute('data-type'); // Get type (contact/project)

                // Update modal content
                deleteItemType.textContent = type === 'contact' ? 'contact' : 'project';

                // Update the form's action URL
                deleteForm.action = type === 'contact' ? `/admin/delete-contact/${id}` : `/admin/delete-project/${id}`;
            });
        }
    } catch (error) {
        // Suppress error and log it only if needed
        console.info("Error in delete modal setup:", error);
    }
});
