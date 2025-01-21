import os

# Define the folder containing your HTML files
html_folder = "templates"  # Adjust for your project structure

# Replace all .jpg/.jpeg/.png with .webp in HTML files
def replace_image_paths(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".jinja"):  # Process only HTML files
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()
                # Replace image paths
                updated_content = content.replace("/static/images/", "/static/images-webp/")
                updated_content = updated_content.replace(".jpg", ".webp")
                updated_content = updated_content.replace(".jpeg", ".webp")
                updated_content = updated_content.replace(".png", ".webp")
                # Write the updated content back
                with open(file_path, "w") as f:
                    f.write(updated_content)
                print(f"Updated: {file_path}")

# Run the script
replace_image_paths(html_folder)
