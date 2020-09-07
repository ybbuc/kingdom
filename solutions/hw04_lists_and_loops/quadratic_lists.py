# Prompt the user to enter terms of quadratic
def get_quadratic():
    print('For a quadratic of the form ax^2+bx+c:')
    a = int(input('a=? '))  # Quadratic coefficient
    b = int(input('b=? '))  # Linear coefficient
    c = int(input('c=? '))  # Constant
    return [a, b, c]


# Find  roots of quadratic if they exist and return the result as string
def solve_quadratic(func):
    # You can assign values to more than one variable using just a single
    # line. This can help shorten your programs and make them easier to read;
    # you’ll use this technique most often when initializing a set of numbers.
    a, b, c = func[0], func[1], func[2]
    determinant = b**2-4*a*c
    if a == 0:  # Avoid division by zero when not quadratic
        return 'Not a quadratic'
    elif determinant < 0:  # Complex roots
        return 'Imaginary solutions'
    elif determinant == 0:  # One root
        root = -b/(2*a)
        return 'x = %.2f' % root
    else:  # Two roots
        root_1 = (-b+determinant**0.5)/(2*a)
        root_2 = (-b-determinant**0.5)/(2*a)
        return 'x = %.2f or %.2f' % (root_1, root_2)


# Get the terms of quadratic
func = get_quadratic()

# Display results
print(solve_quadratic(func))

# Uncomment these lines to run some 'standard' equations for testing
# print(solve_quadratic([0, 1, 1]))
# print(solve_quadratic([1, 2, 3]))
# print(solve_quadratic([1, 0, -4]))
