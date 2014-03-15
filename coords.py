"""Coordinates Module, made by Jacob Kodner."""

__author__ = "Jacob Kodner"

def generate(num, quad=1):
    """Creates a Coordinate plane.

    The plane that is generated has the x & y values less than the inputed 'num' paramater.
    
    You can also input which quadrant your points can come from. If you input 'all', the function
    returns a list of all points from all quadrants. The quadrant parameter is labeled 'quad'."""
    if not isinstance(num, int) or num < 0:
        raise ValueError("Inputted 'num' Value is not an integer or greater than 0.")
    elif quad not in [1, 2, 3, 4, "all"]:
        raise ValueError("Inputed 'quad' value not 1-4/'all'")
    def negate(q):
        x_range, y_range = range(num), range(num)
        neg = range(-num + 1, 1)
        if q == 2:
            x_range = neg
        if q == 3:
            x_range, y_range = neg, neg
        if q == 4:
            y_range = neg
        return {"x_range": x_range, "y_range": y_range}
    plane = []
    if quad != "all":
        x_range = negate(quad)["x_range"]
        y_range = negate(quad)["y_range"]
        for x in x_range:
            for y in y_range:
                plane.append((x, y))
    else:
        for i in range(1, 5):
            x_range = negate(i)["x_range"]
            y_range = negate(i)["y_range"]
            for x in x_range:
                for y in y_range:
                    point = (x, y)
                    if point not in plane:
                        plane.append((point))
    return plane

def slope(p1, p2, fract=True):
    """Returns the Slope of points p1 and p2. p1 and p2 must be tuples with 2 integers.

    There is an optional 'fract' parameter. If 'fract' equals True (default), the function
    returns the slope as a Fraction object from the fractions module. If False, the function
    returns a string.

    If the slope is an undefined slope (#/0), the 'fract' value is overriden to False, and a
    string is returned."""

    if isinstance(p1, tuple) and isinstance(p2, tuple):
        token = False
        if len(p1) != 2 or len(p2) != 2:
            token = True
        for i in [p1, p2]:
            for x in i:
                if not isinstance(x, int):
                    token = True
        if token:
            raise ValueError("Tuple Values are not capable for slope calculation.")
    else:
        raise ValueError("Values are not capable for slope calculation.")
    if fract not in [True, False]:
        raise ValueError("'fract' value is not True/False")
    from fractions import Fraction
    xDif = p2[0] - p1[0]
    yDif = p2[1] - p1[1]
    if xDif == 0:
        fract = False
    if fract:
        obj = Fraction(yDif, xDif)
    else:
        obj = "%s/%s" % (yDif, xDif)
    return obj
