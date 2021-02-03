from godity.core.Component import Component
from godity.math.Vector2 import Vector2

class Transform(Component):
    def __init__(self, position=None, scale=None, rotation=0):
        args = {
            "position" : position,
            "scale"    : scale,
            "rotation" : rotation
        }
        super().__init__("Transform", args)

    def start(self):
        if self.args["position"] != None:   self.position = self.args["position"]
        else:   self.position = Vector2(0,0)
        if self.args["scale"] != None:   self.scale = self.args["scale"]
        else:   self.scale = Vector2(0,0)
        self.rotation = self.args["rotation"]

    def move(self, vector2):
        self.position.x += vector2.x
        self.position.y += vector2.y
        childrens = self.entity.getChildrens()
        if len(childrens) > 0:
            for children in childrens:
                if not children.has("Transform"):   continue
                children.get("Transform").move(vector2)

    def rotate(self, angle):
        self.rotation += angle
        childrens = self.entity.getChildrens()
        if len(childrens) > 0:
            for children in childrens:
                if not children.has("Transform"):   continue
                children.get("Transform").rotate(angle)

    def setRotation(self, angle):
        self.rotation = angle

    def setPosition(self, vector2):
        self.position = vector2
        self.updateChildrenPosition()

    def setPositionX(self, value):
        self.position.x = value
        self.updateChildrenPosition()

    def setPositionY(self, value):
        self.position.y = value
        self.updateChildrenPosition()

    def setScale(self, vector2):
        self.scale = vector2

    def setScaleX(self, value):
        self.scale.x = value

    def setScaleY(self, value):
        self.scale.y = value

    def updateChildrenPosition(self):
        childrens = self.entity.getChildrens()
        if len(childrens) > 0:
            for children in childrens:
                if not children[0].has("Transform"): continue
                pos = self.position.copy()
                pos.x += children[1]
                pos.y += children[2]
                children[0].get("Transform").setPosition(pos)

    def update(self):
        pass