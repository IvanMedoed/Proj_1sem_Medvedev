__all__ = ['circlePerimeter', 'circleArea']

from math import pi

defaulRadius = 5

def circlePerimeter(radius=defaulRadius):
    return radius*2 * pi

def circleArea(radius=defaulRadius):
    return radius**2 * pi