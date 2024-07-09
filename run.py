import os
from PIL import Image
from tkinter import Tk, filedialog

def resize_and_convert_image(image_path, output_path, size, format='WEBP'):
    """Resize and convert the image to the specified format and size."""
    with Image.open(image_path) as img:
        img.thumbnail(size)
        img.save(output_path, format=format, quality=85)  # quality=85 for good balance

def process_images():
    # Hide the main tkinter window
    root = Tk()
    root.withdraw()
    
    # Open file dialog to select images
    file_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    
    if not file_paths:
        print("No files selected. Exiting.")
        return
    
    # Create output directory if it doesn't exist
    output_dir = "optimized_images"
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each selected image
    for idx, file_path in enumerate(file_paths, start=1):
        base_name = f"EbrookStudios-{idx}" if idx > 1 else "EbrookStudios"
        output_path = os.path.join(output_dir, f"{base_name}.webp")
        placeholder_output_path = os.path.join(output_dir, f"{base_name}-placeholder.webp")
        
        # Convert and resize to main image size
        resize_and_convert_image(file_path, output_path, size=(1200, 900), format='WEBP')
        
        # Convert and resize to placeholder image size
        resize_and_convert_image(file_path, placeholder_output_path, size=(100, 75), format='WEBP')
        
        print(f"Processed {file_path} -> {output_path} and {placeholder_output_path}")

if __name__ == "__main__":
    process_images()
