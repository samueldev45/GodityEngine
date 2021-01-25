from godity.core.Component import Component
from godity.math.Vector2 import Vector2

class Rigidbody(Component):
    def __init__(self, app, velocity=2, mass=3, use_gravity=True):
        args = {
            "app"         : app,
            "velocity"    : velocity,
            "mass"        : mass,
            "use gravity" : use_gravity
        }
        super().__init__("Rigidbody", args)

    def start(self):
        self.__app = self.args["app"]
        self.velocity = self.args["velocity"]
        self.mass = self.args["mass"]
        self.use_gravity = self.args["use gravity"]

        self.direction = Vector2(0, 0)
        self.gravity = 0

    def move(self):
        vec = self.direction.copy()
        vec = vec.normalize()

        vec = vec.multiply(self.velocity)

        if self.use_gravity:
            self.direction.y = 1
            clock = self.__app.getClock()
            T = clock.get_time() / 1000
            G = self.__app.gravity
            F = (G * T) + (self.mass * 0.1)
            self.gravity += F
            vec.y = self.gravity

        self.entity.get("Transform").position.x += vec.x
        self.entity.get("Transform").updateChildrenPosition()
        self.entity.get("Box Collider").checkCollision("x")
        self.entity.get("Transform").position.y += vec.y
        self.entity.get("Transform").updateChildrenPosition()
        self.entity.get("Box Collider").checkCollision("y")

        self.direction.x = 0
        if not self.use_gravity:
            self.direction.y = 0

    def update(self):
        self.move()