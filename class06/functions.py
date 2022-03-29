def u(x1:float, x2:float, alpha:float) -> float:
    """ Calculates utility of chosen (x1, x2) bundle.
    
    Args:
        x1 (float): quantity of x1.
        x2 (float): quantity of x2.

    Returns:
        (float): utility of bundle.
    """
    utility = x1**alpha * x2**(1-alpha)
    return utility