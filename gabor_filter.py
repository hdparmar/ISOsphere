
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters

# Path to the directory with the images
directory_path = 'images'

#Path of the analysis
analysis_path = 'images/analysis'

if not os.path.exists(analysis_path):
    os.makedirs(analysis_path)

# Get a list of all the file names in the directory
image_files = os.listdir(directory_path)

for image_file in image_files:
    # Full path to the image file
    image_path = os.path.join(directory_path, image_file)

    # Check if the file is an image by checking the file extension
    if image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
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
            plt.savefig(analysis_path + "/" + image_file.split('.')[0] + "_gabor.png")
            
            # Compute histogram of Gabor response
            hist, bins = np.histogram(gabor_response.flatten(), bins=30, density=True)
            
            # Plot histogram of Gabor response
            plt.figure(figsize=(8, 6))  # Increase figure size
            plt.bar(bins[:-1], hist, width = (bins[1]-bins[0]), color ='cyan', edgecolor ='black')
            plt.title('Histogram of Gabor Filter Response', fontsize=16)
            plt.xlabel('Gabor Response', fontsize=14)
            plt.ylabel('Frequency', fontsize=14)
            plt.tick_params(axis='both', which='major', labelsize=12)  # Increase tick label size
            plt.grid(True)
            plt.savefig(analysis_path + "/" + image_file.split('.')[0] + "_gabor_hist.png")
            
            # Close plots
            plt.close('all')

cv2.destroyAllWindows()

