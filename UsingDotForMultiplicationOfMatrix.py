from numpy import *
import numpy as numpy

# here Two diamentional matrix are given
print("----Two diamentional Matrix----")
matrixOne = numpy.matrix('10 34 ; 18 23')
print("Matrix one---",matrixOne)
matrixTwo = numpy.matrix('2 1 ; 1 2')
print("Matrix two---",matrixTwo)
print()

print("Multiplication using dot function----")
print(matrixOne.dot(matrixTwo))
