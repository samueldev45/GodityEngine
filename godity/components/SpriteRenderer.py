from godity.core.Component import Component
from godity.math.Vector2 import Vector2
import pygame

class SpriteRenderer(Component):
    def __init__(self, app, image_name):
        args = {
            "app"        : app,
            "image name" : image_name
        }
        super().__init__("Sprite Renderer", args)

    def start(self):
        self.__app = self.args["app"]
        self.image_name = self.args["image name"]
        self.rect = pygame.Rect(0,0,0,0)

        # updating transform scale
        if self.entity.has("Transform"):
            transform = self.entity.get("Transform")
            if transform.scale.x == 0 and transform.scale.y == 0:
                sprite_rect = self.__app.getImage(self.image_name).get_rect()
                vec2 = Vector2(sprite_rect.width, sprite_rect.height)
                transform.setScale(vec2)

    def updateRect(self):
        transform = self.entity.get("Transform")
        self.rect.x = transform.position.x
        self.rect.y = transform.position.y

    def getDrawImage(self):
        transform = self.entity.get("Transform")
        image = self.__app.getImage(self.image_name)
        # set scale
        new_image = pygame.transform.smoothscale(image, (int(transform.scale.x), int(transform.scale.y)))
        # set rotate
        new_image = pygame.transform.rotozoom(new_image, transform.rotation * -1, 1)
        self.rect = new_image.get_rect(center = image.get_rect(center = (int(transform.position.x), int(transform.position.y))).center)
        return [new_image, self.rect]

    def update(self):
        pass