[![](https://img.realpython.net/8899c4a6d15334a6b9f769e9f8bc0cf7)](https://srv.realpython.net/click/41686012779/?c=7309556696&p=29182759436&r=25556)

Image Manipulation[¶](#image-manipulation "Permalink to this headline")
=======================================================================

![https://d33wubrfki0l68.cloudfront.net/7a499e799f356a6fe2e695eed7a7d663f7c23c9e/e316e/_images/34575689432_3de8e9a348_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/7a499e799f356a6fe2e695eed7a7d663f7c23c9e/e316e/_images/34575689432_3de8e9a348_k_d.jpg)

Most image processing and manipulation techniques can be carried out effectively using two libraries: Python Imaging Library (PIL) and Open Source Computer Vision (OpenCV).

A brief description of both is given below.

Python Imaging Library[¶](#python-imaging-library "Permalink to this headline")
-------------------------------------------------------------------------------

The [Python Imaging Library](http://www.pythonware.com/products/pil/), or PIL for short, is one of the core libraries for image manipulation in Python. Unfortunately, its development has stagnated, with its last release in 2009.

Luckily for you, there’s an actively-developed fork of PIL called [Pillow](http://python-pillow.github.io/) – it’s easier to install, runs on all major operating systems, and supports Python 3.

### Installation[¶](#installation "Permalink to this headline")

Before installing Pillow, you’ll have to install Pillow’s prerequisites. Find the instructions for your platform in the [Pillow installation instructions](https://pillow.readthedocs.io/en/3.0.0/installation.html).

After that, it’s straightforward:

$ pip install Pillow

### Example[¶](#example "Permalink to this headline")

from PIL import Image, ImageFilter
#Read image
im \= Image.open( 'image.jpg' )
#Display image
im.show()

#Applying a filter to the image
im\_sharp \= im.filter( ImageFilter.SHARPEN )
#Saving the filtered image to a new file
im\_sharp.save( 'image\_sharpened.jpg', 'JPEG' )

#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
r,g,b \= im\_sharp.split()

#Viewing EXIF data embedded in image
exif\_data \= im.\_getexif()
exif\_data

There are more examples of the Pillow library in the [Pillow tutorial](https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html).

Open Source Computer Vision[¶](#open-source-computer-vision "Permalink to this headline")
-----------------------------------------------------------------------------------------

Open Source Computer Vision, more commonly known as OpenCV, is a more advanced image manipulation and processing software than PIL. It has been implemented in several languages and is widely used.

### Installation[¶](#id2 "Permalink to this headline")

In Python, image processing using OpenCV is implemented using the `cv2` and `NumPy` modules. The [installation instructions for OpenCV](http://docs.opencv.org/2.4/doc/tutorials/introduction/table_of_content_introduction/table_of_content_introduction.html#table-of-content-introduction) should guide you through configuring the project for yourself.

NumPy can be downloaded from the Python Package Index(PyPI):

$ pip install numpy

### Example[¶](#id3 "Permalink to this headline")

import cv2
#Read Image
img \= cv2.imread('testimg.jpg')
#Display Image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Applying Grayscale filter to image
gray \= cv2.cvtColor(img, cv2.COLOR\_BGR2GRAY)

#Saving filtered image to new file
cv2.imwrite('graytest.jpg',gray)

There are more Python-implemented examples of OpenCV in this [collection of tutorials](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html).