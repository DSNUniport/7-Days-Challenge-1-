# A basic linear regression function with sklearn module
import numpy as np
from sklearn.linear_model import LinearRegression

def perform_linear_regression(X, y):
    model = LinearRegression()
    model.fit(X, y)
    
    return model

# A basic linear regression function with sklearn module and creating a slope and intercept plot with matplotlib

def linear_regression(x, y):
    # Create a linear regression object
    model = LinearRegression()

    # Fit the model to the data
    model.fit(x.reshape(-1, 1), y) # .reshape(-1, 1)

    # Get the coefficients
    slope = model.coef_[0]
    intercept = model.intercept_

    # Print the equation of the line
    print('Equation: y = {:.2f}x + {:.2f}'.format(slope, intercept))

    # Return the slope and intercept
    return slope, intercept