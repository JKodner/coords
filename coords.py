"""Coordinates Module, made by Jacob Kodner."""

"""To Do: Abs. Value, Perpendicular/Parallel, Exponents, Inequalities, Geometry"""

__author__ = "Jacob Kodner"

class point(object):
    """Coordinate Point Object. The following parameters could be inputted:
    x-coordinate, y-coordinate, and data values."""
    def __init__(self, x, y, *data):
        test = (int, float) 
        if isinstance(x, test) and isinstance(y, test):
            self.x = x
            self.y = y
            self.data = data
        else:
            raise ValueError("x/y values are not compatible.")
    def __repr__(self):
        x, y = self.x, self.y
        data = map(str, self.data)
        rep = "(%s, %s, " % (x, y)
        rep += "[" + ", ".join(data) + "]" + ")"
        return rep
    def add(self, *info):
        """Adds inputted data to list of point's data values"""
        data = list(self.data)
        for i in info:
            data.append(i)
        self.data = tuple(data)
    def delete(self, *info):
        data = list(self.data)
        for i in info:
            if i in data:
                data.remove(i)
        self.data = tuple(data)
    def translate(self, x, y=0):
        test = (int, float)
        if isinstance(x, test) and isinstance(y, test):
            self.x += x
            self.y += y
        else:
            raise ValueError("x/y values are not compatible.")

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
    string is returned.

    Note: As though this program can calculate slopes in the form of decimals, the fractions
    module will not be able to convert the slope into a Fraction. Therefore, the 'fract' parameter
    would be overriden to False.

    Note: Non-Fraction-Object slopes are not simplified, whereas Fraction-Object slopes are
    simplified."""

    if isinstance(p1, tuple) and isinstance(p2, tuple):
        token = False
        if len(p1) != 2 or len(p2) != 2:
            token = True
        for i in [p1, p2]:
            for x in i:
                if not isinstance(x, (int, float)):
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
    elif isinstance(xDif, float) or isinstance(yDif, float):
        fract = False
    if fract:
        obj = Fraction(yDif, xDif)
    else:
        obj = "%s/%s" % (yDif, xDif)
    return obj

def on_slope(p, slope, intercept=0):
    """Determines if the given 'p' point is on a line with a slope of the 'slope' parameter.

    Note: The slope parameter must be in string form.

    There is also an optional 'intercept' parameter, which defaults to 0."""
    from re import match
    if isinstance(p, tuple) and len(p) == 2:
        token = False
        for i in p:
            if not isinstance(i, (int, float)):
                token = True
        if token:
            raise ValueError("Tuple Values are not capable to work with.")
    else:
        raise ValueError("'p' Value is not capable to work with.")
    if not isinstance(intercept, (int, float)):
        raise ValueError("'intercept' value is not int or float.")
    x, y = p[0], p[1]
    patt = r'-?\d+(.\d+)? */ *-?\d+(.\d+)?'
    if not match(patt, slope):
        raise ValueError("Input is not Fraction")
    else:
        new_val = slope.split('/')
        new_val = map(lambda x: x.strip(), new_val)
        new_val = map(float, new_val)
    slope = new_val[0] / new_val[1]
    return bool(y == (slope * x) + intercept)

def on_inequality(p, sign, slope, intercept=0):
    """Determines if the given 'p' point that is either greater, less,
    greater or equal, lesser or equal, to the slope.

    The 'sign' parameter can be any of the following: '<', '<=', '>', or '>='.

    Note: The slope parameter must be in string form.

    There is also an optional 'intercept' parameter, which defaults to 0."""
    from re import match
    if isinstance(p, tuple) and len(p) == 2:
        token = False
        for i in p:
            if not isinstance(i, (int, float)):
                token = True
        if token:
            raise ValueError("Tuple Values are not capable to work with.")
    else:
        raise ValueError("'p' Value is not capable to work with.")
    if sign not in ["<", "<=", ">", ">="]:
        raise ValueError("'sign' Value is invalid.")
    if not isinstance(intercept, (int, float)):
        raise ValueError("'intercept' value is not int or float.")
    x, y = p[0], p[1]
    patt = r'-?\d+(.\d+)? */ *-?\d+(.\d+)?'
    if not match(patt, slope):
        raise ValueError("Input is not Fraction")
    else:
        new_val = slope.split('/')
        new_val = map(lambda x: x.strip(), new_val)
        new_val = map(float, new_val)
    slope = new_val[0] / new_val[1]
    result = eval("y %s (slope * x) + intercept" % sign)
    return bool(result)

def distance(p1, p2):
    """Calculates the distance between 'p1' and 'p2'.

    'p1' and 'p2' can be either a tuple or integer, but both must be the same type."""
    if isinstance(p1, tuple) and isinstance(p2, tuple):
        token = False
        reg = True
        if len(p1) != 2 or len(p2) != 2:
            token = True
        for i in [p1, p2]:
            for x in i:
                if not isinstance(x, (int, float)):
                    token = True
        if token:
            raise ValueError("Tuple Values are not capable for distance calculation.")
    elif isinstance(p1, (int, float)) and isinstance(p2, (int, float)):
        reg = False
    else:
        raise ValueError("Values are not capable for distance calculation.")
    if reg:
        from math import sqrt
        x1, y1, x2, y2 = p1 + p2
        add1 = (x2 - x1) ** 2
        add2 = (y2 - y1) ** 2
        dist = sqrt(add1 + add2)
    else:
        from math import fabs
        dist = fabs(p1) + fabs(p2)
    return dist

def midpoint(p1, p2):
    """Calculates the midpoint between 'p1' and 'p2'.

    'p1' and 'p2' can be either a tuple or integer, but both must be the same type."""
    if isinstance(p1, tuple) and isinstance(p2, tuple):
        token = False
        reg = True
        if len(p1) != 2 or len(p2) != 2:
            token = True
        for i in [p1, p2]:
            for x in i:
                if not isinstance(x, (int, float)):
                    token = True
        if token:
            raise ValueError("Tuple Values are not capable for distance calculation.")
    elif isinstance(p1, (int, float)) and isinstance(p2, (int, float)):
        reg = False
    else:
        raise ValueError("Values are not capable for distance calculation.")
    if reg:
        x1, y1, x2, y2 = p1 + p2
        x = (x1 + x2) / 2.0
        y = (y1 + y2) / 2.0
        mid = (x, y)
    else:
        mid = (p1 + p2) / 2.0
    return mid

def vertex(a, b, c):
    """Returns a vertex point of the given parabola equation.

    Note: the 'x' value of the returned point is the line of symmetry."""
    for i in [a, b, c]:
        if not isinstance(i, (int, float)):
            raise ValueError("Inputted value(s) are not integers.")
    line = float(b) / (2 * a)
    line = -line
    a *= line ** 2
    b *= line
    return (line, a + b + c)