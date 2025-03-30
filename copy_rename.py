import os
import shutil

# Define source and destination folders
fp_folder = "fp"
sp_folder = "sp"
destination_folder = "data"

# Create 'data' folder if it doesn’t exist
os.makedirs(destination_folder, exist_ok=True)

# Function to copy images with new names
def copy_and_rename_images(source_folder, prefix):
    for i, filename in enumerate(sorted(os.listdir(source_folder))):  # Sort for consistent naming
        src_path = os.path.join(source_folder, filename)

        # Check if it's an image file
        if os.path.isfile(src_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            new_name = f"{prefix}_{i+1:03d}{os.path.splitext(filename)[1]}"  # Format as 3-digit (001, 002, ...)
            dest_path = os.path.join(destination_folder, new_name)
            shutil.copy2(src_path, dest_path)
            print(f"Copied: {src_path} -> {dest_path}")

# Copy images from both folders
copy_and_rename_images(fp_folder, "fp")
copy_and_rename_images(sp_folder, "sp")

print("All images copied successfully!")
