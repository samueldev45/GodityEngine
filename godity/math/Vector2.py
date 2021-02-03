import math

class Vector2():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def add(self, vector2):
        return Vector2(self.x + vector2.x, self.y + vector2.y)

    def subtract(self, vector2):
        return Vector2(self.x - vector2.x, self.y - vector2.y)

    def multiply(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def divide(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def lengthSquared(self):
        return self.x * self.x + self.y * self.y

    def normalize(self):
        length = self.length()
        if length > 0:
            x = self.x / length
            y = self.y / length
            return Vector2(x, y)
        return Vector2(0, 0)

    def dot(self, vector2):
        return self.x * vector2.x + self.y * vector2.y

    def cross(self, vector2):
        return self.x * vector2.y - self.y * vector2.x

    def copy(self):
        return Vector2(self.x, self.y)

    def lerp(self, vector2, value):
        x = self.x * (1 - value) + vector2.x * value
        y = self.y * (1 - value) + vector2.y * value
        return Vector2(x, y)

    def rotate(self, degrees):
        sin = math.sin(degrees * math.pi / 180)
        cos = math.cos(degrees * math.pi / 180)

        x = (cos * self.x) - (sin * self.y)
        y = (sin * self.x) + (cos * self.y)

        return Vector2(x, y)

    def rotateRad(self, radians):
        x = self.x * math.cos(radians) - self.y * math.sin(radians)
        y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector2(x, y)

    def getDistanceTo(self, vector2):
        v = self.subtract(vector2)
        return v

    def isNormalized(self):
        if self.x >= -1 and self.x <= 1 and self.y >= -1 and self.y <= 1:
            return True
        return False

    def __str__(self):
        return "["+str(self.x)+", "+str(self.y)+"]"