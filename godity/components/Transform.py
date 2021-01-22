from godity.core.Component import Component
from godity.math.Vector2 import *

class Transform(Component):
    def __init__(self, position=Vector2(0,0), scale=Vector2(0,0), rotation=0):
        args = {
            "position" : position,
            "scale"    : scale,
            "rotation" : rotation
        }
        super().__init__("Transform", args)

    def start(self):
        self.position = self.args["position"]
        self.scale = self.args["scale"]
        self.rotation = self.args["rotation"]

    def move(self, vector2):
        self.position.x += vector2.x
        self.position.y += vector2.y

    def rotate(self, angle):
        self.rotation += angle

    def setPosition(self, vector2):
        self.position = vector2

    def setPositionX(self, value):
        self.position.x = value

    def setPositionY(self, value):
        self.position.y = value

    def setRotation(self, angle):
        self.rotation = angle

    def setScale(self, vector2):
        self.scale = vector2

    def setScaleX(self, value):
        self.scale.x = value

    def setScaleY(self, value):
        self.scale.y = value

    def update(self):
        pass