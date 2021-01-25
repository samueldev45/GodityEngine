from godity.core.Component import Component
from godity.math.Vector2 import Vector2

class BoxCollider(Component):
    def __init__(self, width, height):
        args = {
            "width"  : width,
            "height" : height
        }
        super().__init__("Box Collider", args)

    def start(self):
        self.width = self.args["width"]
        self.height = self.args["height"]

    def checkCollision(self, axis):
        scene = self.entity.getScene()
        collider_entities = scene.getEntitiesWithComponent("Box Collider")
    
        for entity in collider_entities:
            if entity.name == self.entity.name: continue
            if not entity.has("Transform"): continue

            collider = entity.get("Box Collider")
            transform = entity.get("Transform")
            this_transform = self.entity.get("Transform")

            if(this_transform.position.x < transform.position.x + collider.width and 
                this_transform.position.x + self.width > transform.position.x and
                this_transform.position.y < transform.position.y + collider.height and
                this_transform.position.y + self.height > transform.position.y  
            ):
                vec = this_transform.position.copy()
                rb = self.entity.get("Rigidbody")

                if axis == "y":
                    # vertical collision
                    if rb.direction.y < 0: # top
                        vec.y = transform.position.y + collider.height
                    elif rb.direction.y > 0: # bottom
                        vec.y = transform.position.y - self.height
                        rb.gravity = 0

                    this_transform.setPositionY(vec.y)

                if axis == "x":
                    # horizontal collision
                    if rb.direction.x < 0:
                        vec.x = transform.position.x + collider.width
                    elif rb.direction.x > 0:
                        vec.x = transform.position.x - self.width

                    this_transform.setPositionX(vec.x)

    def update(self):
        pass