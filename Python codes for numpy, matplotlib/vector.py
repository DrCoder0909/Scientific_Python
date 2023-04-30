import math
import matplotlib.pyplot as plt

class Vector2D:
    """A two dimesnsional vector with cartesian coordinates"""

    def __init__(self, x, y):
        self.x, self.y =x,y

    def __str__(self):
        """Human-reaadable string representation of the vector"""
        return "{:g}i +{:g}j".format(self.x, self.y)

    def __repr__(self):
        """Unambiguous string representation of the vector."""
        return repr((self.x, self.y))

    def dot(self,other):
        """The scalar (dot) product of self and other. Both must be vectors"""

        if not isinstance(other, Vector2D):
            raise TypeError("Can only take dot product of two vector 2D objects")
        return self.x*other*x + self.y* other.y

    def __sub__(self,other):
        """Vector substraction"""
        return Vector2D(self.x -other.x , self.y-other.y)

    def __add__(self, other):
        """Vector addition"""
        return Vector2D(self.x+other.x , self.y+other.y)

    def __mul__(self, scalar):
        """Multiplication of a vector by a scalar"""

        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector2D(self.x*scalar, self.y*scalar)
        raise NotImplementedError("Can only multiply Vector2D by a scalar")

    def __rmul__(self, scalar):
        """Reflected multiplication"""
        return self.__mul__(scalar)

    def __neg__(self):
        """Negative of the vector"""
        return Vector2D(-self.x, -self.y)

    def __truediv__(self, scalar):
        """True division of a vector by a scalar"""
        return Vector2D(self.x/scalar , self.y/scalar)

    def __mod__(self, scalar):
        """Modulus operation for each  component"""
        return Vector2D(self.x%scalar , self.y % scalar)

    def __abs__(self):
        """ Absolute value (magnitude) of the vector"""
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, other):
        """distance between vector self and other"""
        return abs(self-other)

    def to_polar(self):
        """Return the vector's components in polar coordinates"""
        return self.__abs__(),math.atan2(self.y,self.x)

if  __name__ == "__main__":
    v1= Vector2D(2, 5/3)
    v2= Vector2D(3, -1.5)
    print("v1 =", v1)
    print("repr(v2)=", repr(v2))
    print("v1+v2=", v1+v2)
    print("v1 -v2= ", v1-v2)
    print("abs(v2-v1)= ", abs(v2-v1))
    print("-v2 =", -v2)
    print("v1*3= ", v1*3)
    print("7*v2= ", 7*v1)
