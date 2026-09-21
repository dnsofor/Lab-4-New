def wears_jacket(temp, raining):
    """Return True if Belle wears a jacket.
    >>> wears_jacket(50, False)
    True
    >>> wears_jacket(70, True)
    True
    >>> wears_jacket(70, False)
    False
    """
    return temp < 60 or raining
