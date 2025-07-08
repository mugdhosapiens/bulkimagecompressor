import os
from PIL import Image
import math
input_folder = "C:/Users/gmfah/Documents/Compress Images/input_images"
output_folder = "C:/Users/gmfah/Documents/Compress Images/compressed_images"
def get_file_size(file_path):
    """Return the file size in KB."""
    return os.path.getsize(file_path) / 1024

def compress_image(input_path, output_path, target_size_kb=1000, max_attempts=10):
    """Compress an image to a target size in KB."""
    img = Image.open(input_path)
    
    # Convert to RGB if image is in RGBA or other modes
    if img.mode in ('RGBA', 'LA', 'P'):
        img = img.convert('RGB')
    
    # Initial quality setting
    quality = 85
    step = 5
    attempt = 0
    
    # Save original image dimensions
    original_width, original_height = img.size
    
    # Temporary file to save intermediate results
    temp_output = output_path + '_temp.jpg'
    
    while attempt < max_attempts:
        # Save the image with current quality
        img.save(temp_output, 'JPEG', quality=quality, optimize=True)
        
        # Check the size of the saved image
        current_size = get_file_size(temp_output)
        
        # If size is within target, save final image
        if current_size <= target_size_kb:
            os.rename(temp_output, output_path)
            return True
        
        # Reduce quality for next iteration
        quality -= step
        
        # If quality becomes too low, resize image slightly
        if quality < 20:
            # Reduce dimensions by 10%
            new_width = int(original_width * 0.9)
            new_height = int(original_height * 0.9)
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            original_width, original_height = new_width, new_height
            quality = 85  # Reset quality for resized image
            step = max(2, step - 1)  # Reduce step size for finer control
        
        attempt += 1
    
    # If compression fails, save the last attempt
    if os.path.exists(temp_output):
        os.rename(temp_output, output_path)
    return False

def process_images(input_folder, output_folder, target_size_kb=1000):
    """Process all images in the input folder and save compressed versions to output folder."""
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Supported image formats
    supported_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    
    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in supported_formats:
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '_compressed.jpg'
            output_path = os.path.join(output_folder, output_filename)
            
            try:
                print(f"Processing {filename}...")
                success = compress_image(input_path, output_path, target_size_kb)
                if success:
                    print(f"Successfully compressed {filename} to {get_file_size(output_path):.2f} KB")
                else:
                    print(f"Reached maximum compression attempts for {filename}, saved at {get_file_size(output_path):.2f} KB")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
        else:
            print(f"Skipping {filename}: Unsupported format")

def main():
    # Define input and output folders
    input_folder = "C:/Users/gmfah/Documents/Compress Images/input_images"
    output_folder = "C:/Users/gmfah/Documents/Compress Images/compressed_images"
    
    # Create input folder if it doesn't exist
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"Created input folder: {input_folder}")
        print("Please place your images in the 'input_images' folder and run the script again.")
        return
    
    # Process images
    print("Starting image compression...")
    process_images(input_folder, output_folder)
    print("Compression completed!")

if __name__ == "__main__":
    main()