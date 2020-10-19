
PI=3.14159

# calculate the circumference of the circle
def calculate_circ(radius):
    diameter=radius*2
    return PI*diameter

radius=3.2
print('Radius: %.1f cm.' %radius)
print('The circumference is %.4f cm.' %calculate_circ(radius))


