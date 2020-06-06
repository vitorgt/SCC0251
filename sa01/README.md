# [Short Assignment 1: Filtering in Fourier Domain](/sa01/README.md#description)

## [SCC0251](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=SCC0251).2020.1 - Image Processing

### Prof. Dr. Moacir Ponti

### Author

* 10284952 - Vitor Gratiere Torres

### Folders and files

* [Python code](/sa01/submission/sa01.py) submitted for evaluation
* [Jupyter Notebook demo](/sa01/sa01.ipynb) is a visual demo on the python code, where it was developed
* [Markdown](/sa01/README.md#description) file explaining the assignment
* [Images](/sa01/images) contains images used in demos and evaluation

### Description

In this short assignment you'll implement DFT 2D and Inverse DFT 2D using only numpy.

> Use vector/matrix processing whenever possible to decrease running time

The program takes as input an image filename (that must be loaded into memory) and a float number.

Implement a function that takes as input an image and a threshold value 0 < T <= 1 This function have to:

1. Compute the Fourier Transform, F, of the image;
2. Find the second peak of the Fourier Spectrum, p2, i.e. the maximum not counting the coefficient 0;
3. Set to zero (0) all coefficients for which the Fourier Spectrum is below (less than) T% of the second peak, that is, |F|< p2*T
4. Compute the Inverse Fourier Transform of the filtered version of F (after step 3 above)
5. Print on the screen the following information: p2*T, the number of coefficients below the threshold, the original mean of the image and the mean of the image after processing, using the following format:

```
Threshold=%.4f
Filtered Coefficients=%d
Original Mean=%.2f
New Mean=%.2f
```

Input example:

```
gradient_noise_small.png
0.05
```

Output example:

```
Threshold=28.3364
Filtered Coefficients=961
Original Mean=116.06
New Mean=116.06
```
