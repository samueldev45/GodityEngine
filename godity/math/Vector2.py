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

    def normalize(self):
        length = self.length()
        if length > 0:
            x = self.x / length
            y = self.y / length
            return Vector2(x, y)
        return Vector2(0, 0)

    def copy(self):
        return Vector2(self.x, self.y)

    def __str__(self):
        return "["+str(self.x)+", "+str(self.y)+"]"