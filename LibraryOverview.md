1. NumPy for Python

2. NumPy is a library used for numerical computing and data analysis. It provides support for multi-dimensional arrays, along with a collection of mathematical functions to operate on these arrays efficiently [1].

After importing using "import numpy as np", you're able to use functions related to the library, such as creating arrays from lists and finding statistics about a given list (like mean, corelation coefficient, standard deviation etc.)

3. NumPy provides similar functionality to data analysis as Pandas does. Here are just a few functionalities of the library:

Creating an array:
arr = np.array([1, 2, 3, 4, 5])

Mathematical functions on the array:
result_sqrt = np.sqrt(arr)  - element-wise square root
sum_all = np.sum(arr)       - sum of all elements
mean_all = np.mean(arr)     - average of the array

Indexing and slicing (similar to Pandas):
print(arr[0])               - output: 1
print(arr[1:4])             - output: [2, 3, 4]

The program in this exploration activity uses the basic functionality of the library.

4. NumPy was created in 2005 by Travis Oliphant [2].

5. I chose this library because of my interest in data analysis. Having previously completed courses on MySQL, I thought that it'd be a seamless transition from MySQL to Python. Additionally, I wanted to choose a library that would work with my personal passion for (film), giving me a stronger reason to put effort into the exploration activity (other than it being seen as a must-do for a course). A stake in the game, so to speak.

6. 

References:
[1] https://numpy.org/devdocs/user/whatisnumpy.html
[2] https://www.w3schools.com/python/numpy/numpy_intro.asp
