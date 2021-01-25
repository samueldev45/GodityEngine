import pygame
from godity.engine import *

class Scene():
    def __init__(self, name, render_physics=False):
        self.name = name
        self.render_physics = render_physics

        self.__entities = {}
        self.__camera = None
        self.__add_queue = []
        self.__remove_queue = []
        self.__updating = False
        self.__rendering = False

    def add(self, entity):
        self.__add_queue.append(entity)
    
    def __add(self, entity):
        if not entity.name in self.__entities:
            entity.scene = self
            self.__entities[entity.name] = entity
        else:
            print("Error: class <Scene> function (add) -> The "+entity.name+" entity has already been added to the "+self.name+" scene.")

    def remove(self, entity):
        self.__remove_queue.append(entity)

    def __remove(self, entity):
        if entity in self.__entities:
            entity.scene = None
            del self.__entities[entity]
        else:
            print("Error: class <Scene> function (remove) -> The "+entity+" entity was not added to the "+self.name+" scene.")

    def get(self, entity):
        if entity in self.__entities:
            return self.__entities[entity]
        else:
            print("Error: class <Scene> function (get) -> The "+entity+" entity was not added to the "+self.name+" scene.")

    def getEntities(self):
        entities = []
        for entity in self.__entities:
            entities.append(self.__entities[entity])
        return entities

    def getEntitiesWithComponent(self, component):
        entities = []
        for entity in self.__entities:
            if self.__entities[entity].has(component):
                entities.append(self.__entities[entity])
        return entities

    def setCamera(self, entity):
        if entity.has("Camera"):
            self.__camera = entity

    def getCamera(self):
        return self.__camera

    def isRendering(self):
        return self.__rendering
    
    def isUpdating(self):
        return self.__updating

    def render(self, surface):
        self.__rendering = True
        entities = self.getEntitiesWithComponent("Sprite Renderer")
        if len(entities) > 0:
            for entity in entities:
                if not entity.has("Transform"): continue
                transform = entity.get("Transform")
                sprite_renderer = entity.get("Sprite Renderer")
                image, rect = sprite_renderer.getDrawImage()

                # draw with top left
                rect.x = rect.x + (rect.width / 2)
                rect.y = rect.y + (rect.height / 2)

                if self.__camera == None:
                    surface.blit(image, rect)
                else:
                    surface.blit(image, self.__camera.get("Camera").apply(rect))

        # render physics
        if self.render_physics:
            entities = self.getEntitiesWithComponent("Box Collider")
            for entity in entities:
                if not entity.has("Transform"): continue
                collider = entity.get("Box Collider")
                transform = entity.get("Transform")
                
                # draw with top left
                rect = pygame.Rect(transform.position.x, transform.position.y, collider.width, collider.height)

                if self.__camera != None:
                    rect = self.__camera.get("Camera").apply(rect)

                pygame.draw.rect(surface, (255,255,255), rect, width=1)
        self.__rendering = False

    def update(self):
        if not self.__rendering:
            # add entities in queue
            for entity in self.__add_queue:
                self.__add(entity)
            self.__add_queue.clear()

            # remove entities in queue
            for entity in self.__remove_queue:
                self.__remove(entity)
            self.__remove_queue.clear()

        self.__updating = True
        for entity in self.__entities:
            if self.__camera != None:
                if self.__entities[entity].has("Camera") and self.__entities[entity].name == self.__camera.name:    continue
            self.__entities[entity].update()
        if self.__camera != None:
            self.__camera.update()
        self.__updating = False