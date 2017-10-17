import numpy as np
import matplotlib.pyplot as plt


class Point:
    '''
    Add docstring
    '''

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "Point(%.6F, %.6f) " % (self.x, self.y)

    def __add__(self, P):
        return Point(self.x + P.x, self.y + P.y)

    def __mul__(self, S):
        return Point(self.x * S, self.y * S)

    def __rmul__(self, S):
        return Point(self.x * S, self.y * S)


class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        # ensure the direction is normalized to unity, i.e., cos^2 + sin^2 = 1
        norm = np.sqrt(direction.x**2 + direction.y**2)
        self.direction = Point(direction.x/norm, direction.y/norm)

    def __str__(self):
        return "Ray: r_0(%10.6f, %10.6f), d(%.6f %.6f) " % \
               (self.origin.x, self.origin.y, self.direction.x, self.direction.y)


class Node:

    def contains(self, p):
        """Does the node contain the point?"""
        raise NotImplementedError

    def intersections(self, r):
        """Where does the node intersect the ray?"""
        raise NotImplementedError


class Primitive:

    def __init__(self, surface, sense):
        self.surface, self.sense = surface, sense

    def contains(self, p):
        return (self.surface.f(p) < 0) == self.sense

    def intersections(self, r):
        return self.surface.intersections(r)


class Operator:

    def __init__(self, L, R):
        self.L, self.R = L, R
        # some super checking algorithm

    def contains(self, p):
        raise NotImplementedError

    def intersections(self, r):
        # get intersections with left and right nodes
        pointsL = self.L.intersections(r)
        pointsR = self.R.intersections(r)
        # return the concatenated result
        return pointsL + pointsR


class Union(Operator):

    def __init__(self, L, R):
        super(Union, self).__init__(L, R)

    def contains(self, p):
        inL = self.L.contains(p)
        inR = self.R.contains(p)
        return inL or inR


class Intersection(Operator):

    def __init__(self, L, R):
        super(Intersection, self).__init__(L, R)

    def contains(self, p):
        inL = self.L.contains(p)
        inR = self.R.contains(p)
        return inL and inR


class Surface(object):

    def f(self, p):
        raise NotImplementedError

    def intersections(self, r):
        raise NotImplementedError


class QuadraticSurface(Surface):

    def __init__(self, A=0.0, B=0.0, C=0.0, D=0.0, E=0.0, F=0.0):
        self.A, self.B, self.C, self.D, self.E, self.F = A, B, C, D, E, F
        self.M = np.array([[2 * A, C, D],
                           [C, 2 * B, E],
                           [D, E, 2 * F]])

    def intersections(self, r):
        d = np.array([r.direction.x, r.direction.y, 0]).T
        ro = np.array([r.origin.x, r.origin.y, 1]).T
        a = np.inner(d.T, np.inner(self.M, d))
        b = 2 * np.inner(ro.T, np.inner(self.M, d))
        c = np.inner(ro.T, np.inner(self.M, ro))
        if a != 0:
            coeffs = (a, b, c)
        else:
            coeffs = (b, c)
        roots = np.roots(coeffs)
        ints = []
        for root in roots:
            if not isinstance(root, complex):
                xy = ro + (d * root)
                ints.append(Point(xy[0], xy[1]))
        return ints

    def f(self, p):
        r = np.array([p.x, p.y, 1]).T
        return 0.5 * np.inner(r.T, np.inner(self.M, r))


class PlaneV(QuadraticSurface):

    def __init__(self, a):
        QuadraticSurface.__init__(self, D=1, F=-a)


class PlaneH(QuadraticSurface):

    def __init__(self, b):
        QuadraticSurface.__init__(self, E=1, F=-b)


class Plane(QuadraticSurface):

    def __init__(self, m, b):
        QuadraticSurface.__init__(self, D=-m, E=1, F=-b)


class Circle(QuadraticSurface):

    def __init__(self, r, a=0, b=0):
        QuadraticSurface.__init__(self, A=1, B=1, D=-2*a, E=-2*b, F=(a**2 + b**2 - r**2))


class Region(object) :
    
    def __init__(self) :
        self.node = None
    
    def append(self, node=None, surface=None, operation="U", sense=False) :
        assert((node and not surface) or (surface and not node))
        if isinstance(surface, Surface) :
            node = Primitive(surface, sense)
        if self.node is None :
            self.node = node
        else :
            O = Union if operation == "U" else Intersection
            self.node = O(self.node, node)
          
    def intersections(self, r) :
        pass
        
class Geometry(object) :
    
    # Attributes can be defined in the body of a class.  However, these
    # become "static" values that are the same for every object of the class.
    # Hence, they can be accessed either through object.attribute or 
    # classname.attribute.
    noregion = -1    
    
    def __init__(self,  xmin, xmax, ymin, ymax) :
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.regions = []
        
    def add_region(self, r) :
        self.regions.append(r)

    def find_region(self, p) :
        region = Geometry.noregion
        # look for the region containing p.
        return region
        
    def plot(self, nx, ny) :
        pass
        

if __name__ == '__main__':
    pass
    