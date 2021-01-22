from godity.core.Component import Component
import pygame

class ClickPlayAudio(Component):
    def __init__(self, app):
        args = {
            "app": app
        }
        super().__init__("Click Play", args)

    def start(self):
        self.__app = self.args["app"]

    def update(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            self.__app.stopAudio("audio")
            self.__app.playAudio("audio")