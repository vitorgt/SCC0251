# [Short Assignment 3: Mathematical Morphology for Color Image](/sa03/README.md#description)

## [SCC0251](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=SCC0251).2020.1 - Image Processing

### Prof. Dr. Moacir Ponti

### Author

* 10284952 - Vitor Gratiere Torres

### Folders and files

* [Python code](/sa03/submission/sa03.py) submitted for evaluation
* [Jupyter Notebook demo](/sa03/sa03.ipynb) is a visual demo on the python code, where it was developed
* [Markdown](/sa03/README.md#description) file explaining the assignment
* [Images](/sa03/images) contains images used in demos and evaluation

### Description

In this assignment you are going to perform morphology with color images

There are two procedures to be implemented: 1) RGB opening 2) Composition of operations in RGB channels: gradient, opening, closing 3) procedure 1 followed by procedure 2

The input must be in this order:

* image filename
* k (size of the structuring element)
* option = 1 for RGB opening, 2 = for composition of operations

For all options you must use the disk structuring element from scikit-image's morphology package

Below the details for each option

#### 1. RGB opening

Implement a function that gets as input an RGB image and the size of the structuring element (as implemented in scikit-image). Perform opening on each RGB channel separately.

#### 2. Composition of operations in RGB channels: gradient, opening, closing

1. convert the input image to HSV
2. get the H channel and normalize it to the interval 0 - 255
3. with the structuring element disk, perform the morphological gradient
4. normalize the resulting morphological gradient to the interval 0 - 255
5. compose a new RGB image having

* the normalized gradient in the R channel
* the opening of the normalized H (obtained in step 2) in G channel
* the closing of the normalized H (obtained in step 2) in B channel

#### 3. Using the two above procedures

1. Perform the RGB opening using the size of the structuring element = 2*k
2. Use the opened image as input to the composition method using the size of the structuring element = k

In all cases, compute the RMSE comparing the input image and the image after processing and show it with 4 decimal places
