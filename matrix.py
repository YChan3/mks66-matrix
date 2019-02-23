"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for col in range(len(matrix[0])):
        line = ""
        for row in range(len(matrix)):
            line += "{} ".format(matrix[row][col])
        print(line + "\n")


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    cpy = matrix
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if col == row:
                cpy[row][col] = 1
            else:
                cpy[row][col] = 0
    matrix = cpy

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m = []
    for c in range( len(m2) ):
        m.append( [] )
        for r in range( len(m1[0]) ):
            m[c].append( 0 )

    for col in range(len(m1[0])):
        vals_m1 = []
        for row in range(len(m1)):
            vals_m1.append(m1[row][col])
        # print(vals_m1)

        for row in range(len(m2)):
            sum = 0
            for i in range(len(m2[row])):
                sum += vals_m1[i] * m2[row][i]
            m[row][col] = sum
            # print_matrix(m)
            # print("---------------")

    for row in range(len(m)):
        m2[row] = m[row]



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
