
import cv2
import os
import matplotlib.pyplot as plt
from skimage import filters

# Path to the directory with the images
directory_path = 'images'

# Get a list of all the file names in the directory
image_files = os.listdir(directory_path)

for image_file in image_files:
    # Full path to the image file
    image_path = os.path.join(directory_path, image_file)

    # Read the image
    image = cv2.imread(image_path)  # Read image as color

    # Check if image is not None (this means imread successfully read the image)
    if image is not None:

        # Convert image to grayscale for texture analysis
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Compute Gabor filter response
        gabor_response = filters.gabor(gray, frequency=0.6)
        # The Gabor filter returns two arrays: the real and the imaginary response. 
        # You can use either, or combine them. Here we just use the real response.
        gabor_response = gabor_response[0]
        
        # Save Gabor response
        plt.figure()
        plt.imshow(gabor_response, cmap='gray')
        plt.title('Gabor filter response')
        plt.colorbar()
        plt.savefig(directory_path + "/" + image_file.split('.')[0] + "_gabor.png")

        # Close plot
        plt.close()

cv2.destroyAllWindows()
