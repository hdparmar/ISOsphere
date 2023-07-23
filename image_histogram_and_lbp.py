
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from skimage import feature

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

        # Compute histogram for each color channel and plot on same figure
        colors = ('b', 'g', 'r')
        plt.figure()
        plt.title('Color Histogram')
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")
        for i, color in enumerate(colors):
            hist = cv2.calcHist([image], [i], None, [256], [0, 256])
            plt.plot(hist, color = color)
        plt.xlim([0, 256])
        
        # Save color histogram
        plt.savefig(directory_path + "/" + image_file.split('.')[0] + "_histogram.png")

        # Convert image to grayscale for texture analysis
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Compute LBP
        radius = 3
        n_points = 8 * radius
        lbp = feature.local_binary_pattern(gray, n_points, radius, method="uniform")

        # Compute histogram of LBP
        n_bins = int(lbp.max() + 1)
        hist, _ = np.histogram(lbp, density=True, bins=n_bins, range=(0, n_bins))

        # Plot histogram
        plt.figure()
        plt.title('LBP Histogram')
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")
        plt.hist(hist, bins=n_bins)
        
        # Save LBP histogram
        plt.savefig(directory_path + "/" + image_file.split('.')[0] + "_lbp.png")
        
        # Close all plots
        plt.close('all')

cv2.destroyAllWindows()
