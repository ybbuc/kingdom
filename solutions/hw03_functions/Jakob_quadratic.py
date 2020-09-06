import math
# If you just want to do square roots, it's not necessary to import math.
# Instead of sqrt(x) you can do x ** 0.5 — the built-in exponentiation
# operator is efficient amd saves a function call.


# Find the roots of a quadratic if they exist and return the result as a string
def solve_quadratic(a, b, c):
    determinant = b**2-4*a*c
    # Avoid division by zero when not quadratic
    if a == 0:
        return 'Not a quadratic'
    # Complex roots
    elif determinant < 0:
        return 'Imaginary solutions'
    # One root
    elif determinant == 0:
        root = -b/(2*a)
        return 'x = %.2f' % root
    # Two roots
    else:
        root_1 = (-b+math.sqrt(determinant))/(2*a)
        root_2 = (-b-math.sqrt(determinant))/(2*a)
        return 'x = %.2f or %.2f' % (root_1, root_2)


# Get the terms of the quadratic
print('For a quadratic of the form ax^2+bx+c:')
a = int(input('a=? '))  # Quadratic coefficient
b = int(input('b=? '))  # Linear coefficient
c = int(input('c=? '))  # Constant

# Display the results
print(solve_quadratic(a, b, c))
