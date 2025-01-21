from PIL import Image, ImageOps
import os

# Specify the directory containing the .webp images
input_directory = "/mnt/c/Users/TonyR/OneDrive/Documents/GitHub/jpm/static/images-webp/home/service-cards"
output_directory = "/mnt/c/Users/TonyR/OneDrive/Documents/GitHub/jpm/static/images-webp/home/service-cards-resized"

# Target dimensions
target_width = 600
target_height = 600

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Loop through all files in the input directory
for file_name in os.listdir(input_directory):
    if file_name.endswith(".webp"):
        input_path = os.path.join(input_directory, file_name)
        output_path = os.path.join(output_directory, file_name)

        try:
            # Open the .webp image
            with Image.open(input_path) as img:
                # Preserve aspect ratio and resize
                img = ImageOps.contain(img, (target_width, target_height), Image.Resampling.LANCZOS)

                # Save the resized image to the output directory
                img.save(output_path, "WEBP", quality=100)
                print(f"Resized and saved: {output_path}")
        except Exception as e:
            print(f"Error resizing {file_name}: {e}")
