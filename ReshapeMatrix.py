from numpy import *
import numpy as numpy
matrixOne=numpy.array([[1,3,4],[2,3,4]])
print(matrixOne)
# Shape of the matrix
print("Shape Of the matrix")
print (matrixOne.shape)
print ("size of an array")
print (matrixOne.size)
print ("how to create in single diamentional from multi diamentional")
inSingledia = matrixOne.flatten()
print (inSingledia)

# how to convert matrix in 2 diamentional array

print("how to print matrix in  3 row and 2col")
threeRowAndTwoColumn=inSingledia.reshape(3,2)
print (threeRowAndTwoColumn)
print("how to print matrix in  2row and 3col")
twoRowAndThreecol=inSingledia.reshape(2,3)
print (twoRowAndThreecol)