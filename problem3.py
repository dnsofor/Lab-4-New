def pythagorean_triples(a,b,c):
    """Return True if a^2 + b^2 equals c^2, and False otherwise.
    >>> pythagorean_triples(3, 4, 5)
    True
    >>> pythagorean_triples(5, 12, 13)
    True
    >>> pythagorean_triples(2, 3, 4)
    False
    """
    return a ** 2 + b ** 2 == c ** 2
