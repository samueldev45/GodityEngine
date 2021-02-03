from godity.core.Component import Component
from godity.math.Vector2 import Vector2
import pygame

class Camera(Component):
    def __init__(self, screen_width, screen_height, offset_x=0, offset_y=0, max_width=0, max_height=0):
        args = {
            "screen width"  : screen_width,
            "screen height" : screen_height,
            "offset x"      : offset_x,
            "offset y"      : offset_y,
            "max width"     : max_width,
            "max height"    : max_height
        }
        super().__init__("Camera", args)

    def start(self):
        self.screen_width = self.args["screen width"]
        self.screen_height = self.args["screen height"]
        self.offset_x = self.args["offset x"]
        self.offset_y = self.args["offset y"]
        self.max_width = self.args["max width"]
        self.max_height = self.args["max height"]
        
        self.__scroll = Vector2(0, 0)

    def apply(self, rect):
        return rect.move(self.__scroll.x, self.__scroll.y)

    def update(self):
        transform = self.entity.get("Transform")

        x = -transform.position.x + ((self.screen_width / 2) + self.offset_x)
        y = -transform.position.y + ((self.screen_height / 2) + self.offset_y)

        # limit camera
        if self.max_width != 0:
            x = min(0, x)
            x = max(-(self.max_width - self.screen_width), x)
        if self.max_height != 0:
            y = min(0, y)
            y = max(-(self.max_height - self.screen_height), y)

        self.__scroll.x = x
        self.__scroll.y = y