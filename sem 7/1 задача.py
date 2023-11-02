class Vector:
    def __init__(self, x, y, z):
        assert isinstance(x, (int, float))
        assert isinstance(y, (int, float))
        assert isinstance(z, (int, float))
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z

    def __rmul__(self, other):
        return self.__mul__(other)
a = Vector(7, 12, 17)
b = Vector(9, 19, 22)

c = a + b
print(c.x, c.y, c.z)

d = a - b
print(d.x, d.y, d.z)

e = a * b
print(e)

f = a * 2
print(f.x, f.y, f.z)
