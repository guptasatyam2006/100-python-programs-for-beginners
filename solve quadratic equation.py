
# quadratic equation standard form: ax^2 + bx + c = 0
# where a, b, c are real numbers
# and a is not equal to 0

# solution of this quadratic equation is given by --

# (-b +- (b^2 - 4ac)^(1/2))/(2a)

import math

# input coefficient
a = float (input("Enter coefficient a: "))
b = float (input("Enter coefficient b: "))
c = float (input("Enter coefficient c: "))

# calculate discriminant
discriminant = b**2 - 4*a*c

# check if discriminant is positive, negative or zero

if discriminant > 0:
    # two real and distant roots 
    root1 = (-b + math.sqrt(discriminant))/(2*a)
    root2 = (-b - math.sqrt(discriminant))/(2*a)
    print(f"Root: {root1}")
    print(f"Root: {root2}")
elif discriminant == 0:
    # one real root (repeated)
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    # complex roots
    real_part = -b / (2*a)
    imaginary_root = math.sqrt(abs(discriminant))/(2*a)
    print(f"Root 1: {real_part} + {imaginary_root}i")
    print(f"Root 2: {real_part} - {imaginary_root}i")





