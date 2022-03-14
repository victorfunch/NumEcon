def u(x1:float, x2:float, _dict:dict) -> float:
    """ Calculates utility of chosen (x1, x2) bundle.

    Args:

    x1 (float): quantity of x1.
    x2 (float): quantity of x2.
    _dict (dict): dictionary of model parameters. 

    Returns:

    (float): utility of bundle.
    """
    utility = _dict['beta'] + x1**_dict['alpha'] * x2**(1-_dict['alpha'])
    return utility
