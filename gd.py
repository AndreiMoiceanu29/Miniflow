def gradient_descent_update(x, gradx, learning_rate):
    """
    Performs a gradient descent update.
    """
    # TODO: Implement gradient descent.
    
    # Return the new value for x
    x = x - gradx * learning_rate
    return x
import f