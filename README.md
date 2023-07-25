# ISOsphere
ISOsphere is a Python tool that analyzes film photography. It evaluates image quality based on light, color contrast, and more, providing insights for improvement and optimal shooting conditions.

## Installation
Before running ISOsphere, make sure you have Python installed on your machine along with the necessary libraries.

```bash
# Clone the repository
git clone https://github.com/username/ISOsphere.git

# Navigate to the project directory
cd ISOsphere

# Install the required libraries
pip install -r requirements.txt
```

## Example: Take an Image as an example to see how the image and graphs relate. 

![Example Image](https://github.com/hdparmar/ISOsphere/blob/main/images/000042.JPG)

## Color Histograms
Color histograms represent the distribution of colors in an image. They can provide insights into the color balance of the image, for example, whether an image is predominantly red, or if it has a good balance of colors. 

[How can reading the Histogram can give idea about Exposures](https://photographylife.com/understanding-histograms-in-photography) <br />
[From Capture the Atlas](https://capturetheatlas.com/how-to-read-a-histogram-in-photography/) <br />

Here is an example of a color histogram produced by ISOsphere:

![Color Histogram](https://github.com/hdparmar/ISOsphere/blob/main/images/000042_histogram.png)


## Local Binary Patterns (LBP)
Local Binary Patterns (LBP) are a type of visual descriptor used for texture classification in images. They provide a measure of local spatial structure and can help identify areas of an image with particular textures.

Here is an example of a LBP histogram produced by ISOsphere:

![LBP Histogram](https://github.com/hdparmar/ISOsphere/blob/main/images/000042_lbp.png)

What can you learn by looking at LBP Histogram
The histogram of the LBP image (LBP histogram) represents the distribution of local structures or textures in the image. Each bin in the histogram corresponds to a specific local binary pattern (local structure), and the height of the bin indicates the frequency of that pattern in the image.

Understanding the LBP Histogram:

- A histogram with most values in the low range (near 0) indicates a lot of smooth regions.
- A histogram with values distributed across the range suggests the presence of various textures.
- A histogram with values concentrated in the high range (near 255) implies lots of edges or transitions from dark to light areas.

## Gabor Filter, Why Gabor Fitler
Widely used in texture analysis and feature extraction

They show a high response at the edges and at points where texture changes. Moreover, Gabor filters are believed to closely model the human visual system's response to features in an image, making them particularly useful in human-centric image processing tasks.

![Example Gabor Filter Response]()

## Usage
To use ISOsphere, simply run the main Python script (make sure the path to your image directory is correct):
```bash
python3 image_histogram_and_lbp.py
```

After the program has finished execution, the histogram and lbp will be saved in the same image directory with name x_histogram.png and x_lbp.png where x is the file name.