import cv2
import os
import matplotlib.pyplot as plt

# Path to the directory with the images
directory_path = 'path_to_your_folder'

# Get a list of all the file names in the directory
image_files = os.listdir(directory_path)

for image_file in image_files:
    # Full path to the image file
    image_path = os.path.join(directory_path, image_file)

    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read image as grayscale

    # Check if image is not None (this means imread successfully read the image)
    if image is not None:
        # Display the image
        cv2.imshow('Image', image)

        # Compute histogram
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])

        # Plot histogram
        plt.figure()
        plt.title("Grayscale Histogram")
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")
        plt.plot(hist)
        plt.xlim([0, 256])
        plt.show()

        # Wait for a key press and then close the image window
        cv2.waitKey(0)

cv2.destroyAllWindows()
