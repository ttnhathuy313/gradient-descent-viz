import numpy as np
from math_function import TwoVariableFunction
from function_plot import plot_changes_two_variables
from utils import clear_graph_folder, create_gifs
import matplotlib.pyplot as plt

def gradient_descent_fixed_step(f, x, y, starting_point, learning_rate, precision, max_iterations):
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
        plot_changes_two_variables(f, x, y, x_old, y_old, x_new, y_new, id=i, title="Iteration: " + str(i) + " value = " + str(f.value(x_new, y_new)))
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
    create_gifs('./fixed_step.gif')
    plt.show()

def gradient_descent_wolfe(f, x, y, starting_point, learning_rate, precision, max_iterations):
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
        gradient = -f.gradient(x_old, y_old)

        # Find the step size using extrapolation bisection line search
        # Initialize the step size
        step_size = 1
        # Initialize the counter: j
        j = 0
        U = 2
        L = 0
        while True:
            j+=1
            print(U, L, step_size)
            if (j == 30):
                break
            c_1 = 0.3
            new_x = x_old + (gradient[0] * step_size)
            new_y = y_old + (gradient[1] * step_size)
            if (f.value(new_x, new_y) > f.value(x_old, y_old) + c_1 * step_size * np.dot(-gradient, gradient)):
                U = step_size
                step_size = (U + L) / 2
            else:
                c_2 = 0.2
                next_gradient = -f.gradient(new_x, new_y)
                if (np.dot(next_gradient, gradient) < c_2 * np.dot(-gradient, gradient)):
                    L = step_size
                    if (U == 2):
                        step_size = 2 * L
                    else:
                        step_size = (U + L) / 2
                else:
                    break
        learning_rate = step_size
        

        # Print out the gradient
        print("gradient:", gradient)
        # Move x_old by the negative of the gradient times the learning rate
        x_new = x_old + (gradient[0] * learning_rate)
        # Move y_old by the negative of the gradient times the learning rate
        y_new = y_old + (gradient[1] * learning_rate)
        # Print out the new x value
        print("x_new:", x_new)
        # Print out the new y value
        print("y_new:", y_new)
        print("step_size", step_size)
        # Plot the function and new x value
        plot_changes_two_variables(f, x, y, x_old, y_old, x_new, y_new, id=i, title="Iteration: " + str(i) + " value = " + str(f.value(x_new, y_new)))
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
    create_gifs('./wolfe.gif')
    plt.show()

def gradient_descent_backtrack(f, x, y, starting_point, learning_rate, precision, max_iterations):
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
        gradient = -f.gradient(x_old, y_old)

        # Find the step size using extrapolation bisection line search
        # Initialize the step size
        step_size = 1
        p = 0.7
        j = 0
        while True:
            c_1 = 0.3
            j += 1
            new_x = x_old + (gradient[0] * step_size)
            new_y = y_old + (gradient[1] * step_size)
            if (f.value(new_x, new_y) <= f.value(x_old, y_old) + c_1 * step_size * np.dot(-gradient, gradient)):
                break
            step_size = p * step_size
        learning_rate = step_size
        

        # Print out the gradient
        print("gradient:", gradient)
        # Move x_old by the negative of the gradient times the learning rate
        x_new = x_old + (gradient[0] * learning_rate)
        # Move y_old by the negative of the gradient times the learning rate
        y_new = y_old + (gradient[1] * learning_rate)
        # Print out the new x value
        print("x_new:", x_new)
        # Print out the new y value
        print("y_new:", y_new)
        print("step_size", step_size)
        # Plot the function and new x value
        plot_changes_two_variables(f, x, y, x_old, y_old, x_new, y_new, id=i, title="Iteration: " + str(i) + " value = " + str(f.value(x_new, y_new)))
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
    create_gifs('./backtrack.gif')
    plt.show()

f = TwoVariableFunction()
x = np.linspace(-30, 30, 100)
y = np.linspace(-30, 30, 100)
gradient_descent_fixed_step(f, x, y, [0.5, 20], 0.1, 0.0001, 100)
gradient_descent_wolfe(f, x, y, [0.5, 20], 0.1, 0.0001, 100)
gradient_descent_backtrack(f, x, y, [0.5, 20], 0.1, 0.0001, 100)