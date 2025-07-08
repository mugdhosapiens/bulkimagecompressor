Python script that allows you to upload and compress multiple images to a maximum size of approximately 1000KB (1MB) using the Pillow library. The script processes all images in a specified input folder and saves the compressed versions to an output folder.


To use this script:

1. Install the required library:
   ```bash
   pip install Pillow
   ```

2. Create a folder named `input_images` in the same directory as the script.
3. Place all the images you want to compress in the `input_images` folder.
4. Run the script. It will:
   - Create an `compressed_images` folder if it doesn't exist.
   - Process all supported images (JPG, JPEG, PNG, BMP, GIF) in the input folder.
   - Save compressed versions as JPEG files in the `compressed_images` folder.
   - Attempt to compress each image to under 1000KB by adjusting quality and, if necessary, resizing.

The script uses an iterative approach to achieve the target size:
- Starts with a high quality (85) and reduces it gradually.
- If quality becomes too low, it slightly reduces the image dimensions and retries.
- Supports common image formats and converts them to JPEG for compression.
- Provides feedback on the compression process for each image.

Note: The compressed images are saved as JPEG files, which may result in some quality loss. Adjust the `target_size_kb` parameter in the script if you need a different maximum size.
