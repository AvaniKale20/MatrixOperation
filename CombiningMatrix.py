from numpy import *
import numpy as numpy

# here Two diamentional matrix are given
print("Concatenation using matrix method ,If we use  'axis = None' is not executed")
print("----Two diamentional Matrix----")
matrixOne = numpy.matrix('10 34 ; 18 23')
print("Matrix one---", matrixOne)
matrixTwo = numpy.matrix('2 1 ; 1 2')
print("Matrix two---", matrixTwo)
print()

print("Combining the two matrix row wise----")
combineBothMatrix = numpy.concatenate((matrixOne, matrixTwo), axis=0)
print(combineBothMatrix)
print()

print("Combining the two matrix column----")
combineBothMatrix2 = numpy.concatenate((matrixOne, matrixTwo), axis=1)
print(combineBothMatrix2)

# ------------------------------------------
# Another Three ways are there for concatenating . below program is without using matrix() method.---------

print("There are three way for concatenate --------")
print("1:: numpy.concatenate-----")

print("----Two diamentional Matrix----")
matrixOne = numpy.array([[10, 34], [18, 23]])
print("Matrix one---", matrixOne)

matrixTwo = numpy.array([[2, 1], [1, 2]])
print("Matrix two---", matrixTwo)

print("Combining the two matrix Row wise , axis =0 means concatenate row wise----")
combineRowWiseBothMatrix = numpy.concatenate((matrixOne, matrixTwo), axis=0)
print(combineRowWiseBothMatrix)
print()

print("Combining the two matrix Column wise , axis =1 means concatenate Column wise----")
combineColumnWiseBothMatrixF = numpy.concatenate((matrixOne, matrixTwo), axis=1)
print(combineColumnWiseBothMatrixF)
print()

print("Combining the two matrix in one row , axis =Nome ----")
combineColumnWiseBothMatrixF = numpy.concatenate((matrixOne, matrixTwo), axis=None)
print(combineColumnWiseBothMatrixF)
print()
# ------------------------------------------------------------------------------
print("2:: numpy.vstack and numpy.hstack-----")

print("----Two diamentional Matrix----")
matrixOne = numpy.array([[10, 34], [18, 23]])
print("Matrix one---", matrixOne)

matrixTwo = numpy.array([[2, 1], [1, 2]])
print("Matrix two---", matrixTwo)

print("Using vstack----")
combine_using_vstack_both_matrix = numpy.vstack((matrixOne, matrixTwo))
print(combine_using_vstack_both_matrix)
print()
print("Using hstack----")
combine_using_hstack_both_matrix = numpy.hstack((matrixOne, matrixTwo))
print(combine_using_hstack_both_matrix)
print()
# ------------------------------------------------------------
print("3:: numpy.r and numpy.c-----")

print("----Two diamentional Matrix----")
matrixOne = numpy.array([[10, 34], [18, 23]])
print("Matrix one---", matrixOne)

matrixTwo = numpy.array([[2, 1], [1, 2]])
print("Matrix two---", matrixTwo)

print("Using numpy.r----")
combine_using_r_both_matrix = numpy.r_[matrixOne, matrixTwo]
print(combine_using_r_both_matrix)
print()
print("Using numpy.c----")
combine_using_c_both_matrix = numpy.c_[matrixOne, matrixTwo]
print(combine_using_c_both_matrix)
print()