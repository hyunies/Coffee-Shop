import math

# Function for calculating the volume of a cube
def cube_calculator(side_length):
    cube_volume = side_length ** 3
    return cube_volume

# Function for calculating the volume of a pyramid
def pyramid_calculator(base_length, height):
    pyramid_volume = (1/3)*((base_length**2)*height)
    return pyramid_volume

# Function for calculating the volume of an ellipsoid
def ellipsoid_calculator(radius1, radius2, radius3):
    ellipsoid_volume = ((4/3)*math.pi)*(radius1)*(radius2)*(radius3)
    return ellipsoid_volume

