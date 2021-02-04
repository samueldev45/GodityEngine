from godity.core.Component import Component
from godity.math.Vector2 import Vector2
import pygame

class Rigidbody(Component):
    def __init__(self, app, velocity=2, mass=3, use_gravity=True, drop_platform_key=pygame.K_DOWN):
        args = {
            "app"               : app,
            "velocity"          : velocity,
            "mass"              : mass,
            "use gravity"       : use_gravity,
            "drop platform key" : drop_platform_key
        }
        super().__init__("Rigidbody", args)

    def start(self):
        self.air_time = 0.0
        self.__app = self.args["app"]
        self.velocity = self.args["velocity"]
        self.mass = self.args["mass"]
        self.use_gravity = self.args["use gravity"]
        self.drop_platform_key = self.args["drop platform key"]

        self.direction = Vector2(0, 0)
        self.gravity = 0
        self.on_ground = False
        self.is_jumping = False
        self.platform_drop = False

    def move(self):
        vec = self.direction.copy()
        vec = vec.normalize()
        transform = self.entity.get("Transform")
        box_collider = self.entity.get("Box Collider")

        vec = vec.multiply(self.velocity)

        self.air_time += 0.1
        self.direction.y = -1

        if self.air_time > 2:
            self.is_jumping = False

        if self.use_gravity:
            clock = self.__app.getClock()
            T = clock.get_time() / 1000
            G = self.__app.gravity
            F = (G * T) + (self.mass * 0.1)

            if not self.is_jumping:
                self.direction.y = 1
                self.gravity += F
            else:
                self.direction.y = -1
                self.gravity += 0.1

            vec.y = self.gravity

        if self.air_time > 0:
            self.on_ground = False

        box_collider.collide_objects.clear()

        transform.position.x += vec.x
        transform.updateChildrenPosition()
        box_collider.checkCollision("x")

        transform.position.y += vec.y
        transform.updateChildrenPosition()
        box_collider.checkCollision("y")

        self.direction.x = 0
        if not self.use_gravity:
            self.direction.y = 0

    def jump(self, force):
        self.on_ground = False
        self.direction.y = -1
        self.gravity = -force
        self.is_jumping = True

    def update(self):
        self.move()