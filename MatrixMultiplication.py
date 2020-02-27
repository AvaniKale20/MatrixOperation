from numpy import *
import numpy as numpy

# Multiplication of two 2* 2 matrix
matrixOne = numpy.matrix('1 2 ; 1 2')
matrixTwo = numpy.matrix('1 2 ; 1 2')
multiplication_of_matrix = matrixOne * matrixTwo
print("Multiplication of two 2* 2 matrix", multiplication_of_matrix)
print()

# Multiplication of two 3*3 matrix
matrixOneWithThreeDiamentionalArray = numpy.matrix('2 1 2 ; 1 2 1 ; 2 3 2')
print("matrix One With Three Diamentional Array==", matrixOneWithThreeDiamentionalArray)

matrixTwoWithThreeDiamentionalArray = numpy.matrix('1 2 1 ; 2 1 2 ; 2 3 2')
print("matrix two With Three Diamentional Array==", matrixTwoWithThreeDiamentionalArray)

multiplication_of_three_by_three_matrix = matrixOneWithThreeDiamentionalArray * matrixTwoWithThreeDiamentionalArray
print("Multiplication of two 2* 2 matrix", multiplication_of_three_by_three_matrix)
