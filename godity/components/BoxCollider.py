from godity.core.Component import Component
from godity.math.Vector2 import Vector2
import pygame

class BoxCollider(Component):
    def __init__(self, width, height, ghost=False, is_platform=False):
        args = {
            "width"       : width,
            "height"      : height,
            "ghost"       : ghost,
            "is platform" : is_platform
        }
        super().__init__("Box Collider", args)

    def start(self):
        self.width = self.args["width"]
        self.height = self.args["height"]
        self.ghost = self.args["ghost"]
        self.is_platform = self.args["is platform"]
        self.collide_objects = {}

    def checkCollision(self, axis):
        scene = self.entity.getScene()
        collider_entities = scene.getEntitiesWithComponent("Box Collider")

        for entity in collider_entities:
            if entity.name == self.entity.name: continue
            if not entity.has("Transform") and not entity.has("Box Collider"): continue

            collider = entity.get("Box Collider")
            transform = entity.get("Transform")
            this_transform = self.entity.get("Transform")
            this_rigidbody = self.entity.get("Rigidbody")

            if(this_transform.position.x < transform.position.x + collider.width and 
                this_transform.position.x + self.width > transform.position.x and
                this_transform.position.y < transform.position.y + collider.height and
                this_transform.position.y + self.height > transform.position.y  
            ):
                self.collide_objects[entity.name] = {"entity" : entity, "collision types" : {"top": False, "bottom" : False, "left" : False, "right" : False}}
                if collider.ghost:  continue
                vec = this_transform.position.copy()

                if collider.is_platform:
                    if this_rigidbody.is_jumping: continue
                    keyboard = pygame.key.get_pressed()
                    if keyboard[this_rigidbody.drop_platform_key] and not this_rigidbody.platform_drop:
                        this_rigidbody.platform_drop = True
                        this_rigidbody.direction.y = 1
                    if this_rigidbody.platform_drop: continue

                if axis == "y":
                    # vertical collision
                    if this_rigidbody.direction.y < 0: # top
                        self.collide_objects[entity.name]["collision types"]["top"] = True
                        if this_rigidbody.use_gravity:
                            this_rigidbody.gravity = 0.1
                            this_rigidbody.is_jumping = False
                        vec.y = transform.position.y + collider.height
                        
                    elif this_rigidbody.direction.y > 0: # bottom
                        self.collide_objects[entity.name]["collision types"]["bottom"] = True
                        if this_rigidbody.use_gravity:
                            this_rigidbody.gravity = 0
                            this_rigidbody.air_time = 0.0
                            this_rigidbody.on_ground = True
                            this_rigidbody.platform_drop = False
                        vec.y = transform.position.y - self.height

                    this_transform.setPositionY(vec.y)

                if axis == "x":
                    # horizontal collision
                    if this_rigidbody.direction.x < 0: # left
                        self.collide_objects[entity.name]["collision types"]["left"] = True
                        vec.x = transform.position.x + collider.width
                    elif this_rigidbody.direction.x > 0: # right
                        self.collide_objects[entity.name]["collision types"]["right"] = True
                        vec.x = transform.position.x - self.width

                    this_transform.setPositionX(vec.x)
    def update(self):
        pass