from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 255]
scalex = new_matrix()
scaley = new_matrix()
matrix = []

scalex[0] = [1,0,0,0]
scalex[1] = [0,1,0,0]
scalex[2] = [0,0,1,0]
scalex[3] = [80,0,0,1]

scaley[0] = [1,0,0,0]
scaley[1] = [0,1,0,0]
scaley[2] = [0,0,1,0]
scaley[3] = [0,80,0,1]

x = 0
while x < 80:
    add_edge(matrix, x, 0, 0, x, 80, 0)
    x += 1

orig = []
for item in matrix:
    orig.append(item)

base = []
for item in matrix:
    base.append(item)

for t in range(2):
    for r in range(4):
        for c in range(4):
            draw_lines( matrix, screen, color )
            if c != 3:
                matrix_mult(scalex, matrix)
                matrix_mult(scalex, matrix)
        matrix_mult(scaley, base)
        matrix_mult(scaley, base)
        matrix = []
        for item in base:
            matrix.append(item)
    if t == 0:
        base = orig
        matrix_mult(scaley, base)
        matrix_mult(scalex, base)
        # print_matrix(base)
        matrix = []
        for item in base:
            matrix.append(item)

A = {[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]}
B = {[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]}
ident = new_matrix()
ident(ident)
matrix_mult(A,B)
print_matrix(A)
print_matrix(B)
matrix_mult(B,A)
print_matrix(A)
print_matrix(B)
matrix_mult(ident,A)
print_matrix(A)

display(screen)
