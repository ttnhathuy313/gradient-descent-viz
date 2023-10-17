from sympy.utilities.lambdify import lambdify
from sympy import Symbol, sin
import numpy as np


class TwoVariableFunction:
    def __init__(self):
        self.x = Symbol('x')
        self.y = Symbol('y')
        self.function = (10 * self.x ** 2 + self.y ** 2) / 2
        self.derivative_x = self.function.diff(self.x)
        self.derivative_y = self.function.diff(self.y)
    
    # Calculate f(point)
    def value(self, x, y):
        f = lambdify([self.x, self.y], self.function, 'numpy')
        return f(x, y)
    
    # Calculate the gradient of f at (x, y)
    def gradient(self, x, y):
        f_x = lambdify([self.x, self.y], self.derivative_x, 'numpy')
        f_y = lambdify([self.x, self.y], self.derivative_y, 'numpy')
        return np.array([f_x(x, y), f_y(x, y)])
