from godity.core.Component import Component
from godity.math.Vector2 import Vector2
import pygame

class SpriteRenderer(Component):
    def __init__(self, app, image_name, area=None, tile_width=0, tile_height=0, offset_x=0, offset_y=0, flip_x=False, flip_y=False, smooth_scale=True):
        args = {
            "app"          : app,
            "image name"   : image_name,
            "area"         : area,
            "tile width"   : tile_width,
            "tile height"  : tile_height,
            "offset x"     : offset_x,
            "offset y"     : offset_y,
            "flip x"       : flip_x,
            "flip y"       : flip_y,
            "smooth scale" : smooth_scale
        }
        super().__init__("Sprite Renderer", args)

    def start(self):
        self.__app = self.args["app"]
        self.image_name = self.args["image name"]
        self.area = self.args["area"]
        self.tile_width = self.args["tile width"]
        self.tile_height = self.args["tile height"]
        self.offset_x = self.args["offset x"]
        self.offset_y = self.args["offset y"]
        self.flip_x = self.args["flip x"]
        self.flip_y = self.args["flip y"]
        self.smooth_scale = self.args["smooth scale"]
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

    def setArea(self, area):
        self.area = area

    def setFlip(self, x, y):
        self.flip_x = x
        self.flip_y = y

    def setImage(self, image_path, convert_alpha=False):
        self.__app.updateImage(self.image_name, image_path, convert_alpha)

    def getDrawImage(self):
        transform = self.entity.get("Transform")
        image = self.__app.getImage(self.image_name)

        if self.area == None:
            if self.smooth_scale:
                new_image = pygame.transform.smoothscale(image, (int(transform.scale.x), int(transform.scale.y)))
            else:
                new_image = pygame.transform.scale(image, (int(transform.scale.x), int(transform.scale.y)))
            new_image = pygame.transform.rotozoom(new_image, transform.rotation * -1, 1)
            
        else:
            area = (self.area[0] * self.tile_width, self.area[1] * self.tile_height, self.tile_width, self.tile_height)
            surface = pygame.Surface((self.tile_width, self.tile_height))
            surface.set_colorkey((0,0,0))
            surface.blit(image, (0,0), area)

            if self.smooth_scale:
                new_image = pygame.transform.smoothscale(surface, (int(transform.scale.x), int(transform.scale.y)))
            else:
                new_image = pygame.transform.scale(surface, (int(transform.scale.x), int(transform.scale.y)))

        new_image = pygame.transform.flip(new_image, self.flip_x, self.flip_y)
        self.rect = image.get_rect(center = image.get_rect(center = (int(transform.position.x), int(transform.position.y))).center)
        
        self.rect.x += self.offset_x
        self.rect.y += self.offset_y
        return [new_image, self.rect]

    def update(self):
        pass