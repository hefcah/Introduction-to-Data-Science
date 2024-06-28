#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image
import numpy as np
from IPython.display import display
# img = Image.open('PATH')
img = Image.open('img.jpg')
display(img)
img_array = np.array(img)
img_array.shape
""" The RGB Values of the first Pixel """
img_array[0][0]
""" You can use the height and width variables in your code to get the rows and columns of pixels in the image """
height = img_array.shape[0]
width = img_array.shape[1]
height,width

#I refered youtube videos and chatgpt to understand the concepts involve in the given code
# Define the colors for light and dark squares
color1= (255, 0, 225)       #Green color
color2 = (0, 225, 225)     #Pink Color

# Specify the dimensions of the chessboard (12x12)
square_size = height // 12

# Create a pattern of alternating light and dark squares
#loops were taken with the help of chagpt
for i in range(0, height, square_size):
    for j in range(0, width, square_size):
        if (i // square_size + j // square_size) % 2 == 0:
            color = color1
        else:
            color = color2
    img_array[i:i+square_size, j:j+square_size] = color

# Convert the modified NumPy array back to an image
newcolor = Image.fromarray(img_array)

# Display the modified image (optional)
display(newcolor)

# Save the modified image
newcolor.save('newcolor.jpg')
from PIL import Image

# Assuming you have 'height', 'width', and 'img_array' defined

# Define the colors for light and dark squares
green = (255, 0, 225)  # Green color
pink = (0, 225, 0)  # Pink Color

# Specify the dimensions of the chessboard (12x12)
square_size = height // 12

# Create a pattern of alternating light and dark squares
for i in range(0, height, square_size):
    for j in range(0, width, square_size):
        if (i // square_size + j // square_size) % 2 == 0:
            color = green
        else:
            color = pink
        img_array[i:i + square_size, j:j + square_size] = color
#Took help for this step from chat gpt 
# Convert the modified NumPy array back to an image
newcolor = Image.fromarray(img_array.astype('uint8'), 'RGB')

# Display the modified image
display(newcolor)

# Save the modified image
newcolor.save('newcolor.jpg')

