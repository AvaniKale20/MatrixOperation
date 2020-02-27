from numpy import *
import numpy as numpy

# How to access element from matrix
# here Two diamentional matrix are given
print("----Two diamentional Matrix----")
matrixOne = numpy.matrix('10 34 ; 18 23')
print("Matrix one ---", matrixOne)
print()
# --------------------------
# Accessing element from matrix
# We have to put in matrixOne[0] 0 , it will give whole 1st row."
print("Access 1st two element / means 1st row  from the matrix---")
AccessFirstRow = matrixOne[0]
print("1st row in the matrix ---", AccessFirstRow)
print()
# ---------------------------------------
# We have to put in matrixOne[1] 1 , it will give whole 2nd row."
print("Access 2nd two element / means 2nd row  from the matrix---")
AccessSecondRow = matrixOne[1]
print("2nd row in the matrix ---", AccessSecondRow)
print()
# ----------------------------------
# We have to put in matrixOne[0,0] "0,0" : 1st 0 for 1st row and 2nd 0 for 1st column ."
print("Access 1st one element / means 1st element from 1st row from the matrix---")
AccessFirstElementFromFirstRow = matrixOne[0,0]
print("1st element from matrix ---", AccessFirstElementFromFirstRow)
print()
# ------------------
# We have to put in matrixOne[1,1] "1,1" : 1st 1 for 2nd row and 2nd 1 for 2nd column ."
print("Access last 4th element / means 4th element from 2nd row from the matrix---")
AccessFourthElementFromFirstRow = matrixOne[1,1]
print("4th element from matrix ---", AccessFourthElementFromFirstRow)
print()
