import cv2
import os
import matplotlib.pyplot as plt

# Path to the directory with the images
directory_path = '../Film_01_CLC'

# Get a list of all the file names in the directory
image_files = os.listdir(directory_path)

for image_file in image_files:
    # Full path to the image file
    image_path = os.path.join(directory_path, image_file)

    # Read the image
    image = cv2.imread(image_path)  # Read image as color

    # Check if image is not None (this means imread successfully read the image)
    if image is not None:
        # Display the image
        cv2.imshow('Image', image)

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
        plt.show()

        # Wait for a key press and then close the image window
        cv2.waitKey(0)

cv2.destroyAllWindows()
