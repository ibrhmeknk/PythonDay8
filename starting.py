import math

coverage = 5
height = int(input('What is the height of the wall? \n'))
width = int(input('What is the width of the wall? \n'))


def calculator(x, y):
    b = math.ceil((x * y) / coverage)
    return b


calculator(height, width)
a = calculator(height, width)
print(a)
