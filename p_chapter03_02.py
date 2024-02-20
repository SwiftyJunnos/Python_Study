# Chapter03-02
# Special Method (Magic Method)
import typing

class Vector():
    """
    Vector is a couple of numbers which represents point at 2-dimensional plane.
    """

    def __init__(self, *args):
        """
        Create a new vector
        Example : v = Vector(5, 10)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self) -> str:
        """Return the vector information."""
        return "Vector(%r, %r)" % (self._x, self._y)

    def __add__(self, other: 'Vector') -> 'Vector':
        """Add another vector."""
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other: int) -> 'Vector':
        """Multiply integer to vector."""
        return Vector(self._x * other, self._y * other)

    def __bool__(self):
        """Check if given vector is (0, 0) or not."""
        return bool(max(self._x, self._y))

# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(bool(v1), bool(v3))
