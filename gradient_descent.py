import numpy as np
from math_function import Function, TwoVariableFunction
from function_plot import plot_changes, plot_function, plot_changes_two_variables, plot_function_two_variables
from utils import clear_graph_folder, create_gifs
import matplotlib.pyplot as plt

def gradient_descent_process(starting_point, learning_rate, precision, max_iterations):
    clear_graph_folder()

    x_old = starting_point
    # Initialize the counter: i
    i = 0
    # Create a Function object: f
    f = Function()
    # Use linspace to sample 100 x values between -10 and 10
    x = np.linspace(-10, 10, 100)
    # Plot the function
    # plot_function(f, x)


    # Iterate until the change in x is less than precision or we hit the maximum number of iterations
    while True:
        # Print out the number of the current iteration
        print("Iteration:", i)
        # Print out the old x value
        print("x_old:", x_old)
        # Get the gradient at our current position
        gradient = f.deriv(x_old)
        # Print out the gradient
        print("gradient:", gradient)
        # Move x_old by the negative of the gradient times the learning rate
        x_new = x_old - (gradient * learning_rate)
        # Print out the new x value
        print("x_new:", x_new)
        # Plot the function and new x value
        plot_changes(f, x, x_old, x_new, str(i))
        # Check if the difference between the old x and new x is less than precision
        if abs(x_new - x_old) < precision:
            print("Precision reached!")
            break
        # Check if we've exceeded the maximum number of iterations
        if i > max_iterations:
            print("Maximum iterations exceeded!")
            break
        # Set the old x to the new x
        x_old = x_new
        # Increment the iteration counter
        i += 1
    create_gifs()

def gradient_descent_two_variables_process(f, x, y, starting_point, learning_rate, precision, max_iterations):
    clear_graph_folder()

    x_old = starting_point[0]
    y_old = starting_point[1]
    # Initialize the counter: i
    i = 0
    # Plot the function
    # plot_function_two_variables(f, x, y)

    X, Y = np.meshgrid(x, y)
    Z = f.value(X, Y)
    plt.contourf(X, Y, Z, 100, cmap='RdGy')
    plt.colorbar()


    # Iterate until the change in x is less than precision or we hit the maximum number of iterations
    while True:
        # Print out the number of the current iteration
        print("Iteration:", i)

        # Print out the old x value
        print("x_old:", x_old)
        # Print out the old y value
        print("y_old:", y_old)
        # Get the gradient at our current position
        gradient = f.gradient(x_old, y_old)
        # Print out the gradient
        print("gradient:", gradient)
        # Move x_old by the negative of the gradient times the learning rate
        x_new = x_old - (gradient[0] * learning_rate)
        # Move y_old by the negative of the gradient times the learning rate
        y_new = y_old - (gradient[1] * learning_rate)
        # Print out the new x value
        print("x_new:", x_new)
        # Print out the new y value
        print("y_new:", y_new)
        # Plot the function and new x value
        plot_changes_two_variables(f, x, y, x_old, y_old, x_new, y_new, str(i))
        # Check if the difference between the old x and new x is less than precision
        if np.sqrt((x_new-x_old)**2 + (y_new-y_old)**2) < precision:
            print("Precision reached!")
            break
        # Check if we've exceeded the maximum number of iterations
        if i > max_iterations:
            print("Maximum iterations exceeded!")
            break
        # Set the old x to the new x
        x_old = x_new
        # Set the old y to the new y
        y_old = y_new
        # Increment the iteration counter
        i += 1
    create_gifs()

f = TwoVariableFunction()
x = np.linspace(-30, 30, 100)
y = np.linspace(-30, 30, 100)
gradient_descent_two_variables_process(f, x, y, [0.5, 20], 0.1, 0.00001, 100)