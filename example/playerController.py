from godity.core.Component import Component
import pygame

class PlayerController(Component):
    def __init__(self, speed=4):
        args = {
            "speed" : speed
        }
        super().__init__("Player Controller", args)

    def start(self):
        self.entity.get("Rigidbody").velocity = self.args["speed"]

    def getInputs(self):
        keyboard = pygame.key.get_pressed()
        rigidbody = self.entity.get("Rigidbody")

        if keyboard[pygame.K_w]:    rigidbody.direction.y = -1
        elif keyboard[pygame.K_s]:  rigidbody.direction.y = 1
        if keyboard[pygame.K_a]:    rigidbody.direction.x = -1
        elif keyboard[pygame.K_d]:  rigidbody.direction.x = 1

    def update(self):
        self.getInputs()