# # Assignment 1: Intensity Transformations
# ## SCC0251.2020.1 - Image Processing
# ### Prof. Dr. Moacir Ponti
# ### 10284952 - Vitor Gratiere Torres
# https://github.com/vitorgt/SCC0251

# Imports
import numpy as np
import imageio
# import matplotlib.pyplot as plt


# Transformation functions
# Formulae described on assignment's pdf only translated to python
def t1(image):
    return (255 - image)


def t2(image):
    a = np.min(r)
    b = np.max(r)
    c = int(input())
    d = int(input())
    return (image-a)*((d-c)/(b-a))+c


def t3(image):
    image = image.astype(np.int32)
    return 255*(np.log2(1+image)/np.log2(1+np.max(image)))


def t4(image):
    W = int(input())
    l = float(input())
    return W*(image**l)


# Root Squared Error function
def rse(r, m):
    return np.sqrt(np.sum((m.astype(np.float)-r.astype(np.float))**2))


# Inputs, following assignment's pdf requested sequence
r = imageio.imread(str(input()).rstrip()).astype(np.uint8)
m = int(input())
s = (False, True)[int(input())]
# Note on 's': that is an if. If it's inputted a '0', 's' receives the 0th position of tuple (False, True), as so for '1'.

# Dictionary for functions based on method input
t = {1: t1, 2: t2, 3: t3, 4: t4}

# Appling 'm' transformation to original image 'r'
# Storing back on 'm'
m = t[m](r)

# Calculating RSE and printing
print("{:.4f}".format(rse(r, m)))

# Saving
if s:
    imageio.imwrite("output_img.png", m)

# Plotting
# plt.figure(figsize=(20,20))

# plt.subplot(121)
# plt.imshow(r, cmap="gray")
# plt.axis('off')

# plt.subplot(122)
# plt.imshow(m.astype(np.uint8), cmap="gray")
# plt.axis('off')
