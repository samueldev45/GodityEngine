import pygame
from godity.engine import *

class Scene():
    def __init__(self, app, name, surface_width, surface_height, adjust_surface=True, render_physics=False, environment_light=(255,255,255), max_surface_width=None, max_surface_height=None):
        self.name = name
        self.render_physics = render_physics
        self.environment_light = environment_light
        self.background_color = (0,0,0)

        self.__app = app
        self.__surface_width = surface_width
        self.__surface_height = surface_height
        self.__adjust_surface = adjust_surface
        self.__max_surface_width = max_surface_width
        self.__max_surface_height = max_surface_height
        self.__surface = pygame.Surface((self.__surface_width, self.__surface_height))
        self.__environment_surface = pygame.Surface((self.__surface_width, self.__surface_height))

        self.__entities = {}
        self.__camera = None
        self.__add_queue = []
        self.__remove_queue = []
        self.__updating = False
        self.__rendering = False
        self.__cameraFirstUpdate = False
        self.__layers = {}

    def addLayer(self, layer):
        if not layer.name in self.__layers:
            self.__layers[layer.name] = layer

    def removeLayer(self, layer):
        if layer in self.__layers:
            del self.__layers[layer]

    def add(self, entity, layer):
        self.__add_queue.append([entity, layer])
    
    def __add(self, entity, layer):
        if not entity.name in self.__entities:
            entity.scene = self
            entity.layer = self.__layers[layer]
            self.__layers[layer].add(entity)
            self.__entities[entity.name] = entity
        else:
            print("Error: class <Scene> function (add) -> The {} entity has already been added to the {} scene.".format(entity.name, self.name))

    def remove(self, entity, layer):
        self.__remove_queue.append([entity, layer])

    def __remove(self, entity, layer):
        if entity in self.__entities:
            self.__entities[entity].scene = None
            self.__entities[entity].layer = None
            del self.__entities[entity]
            self.__layers[layer].remove(entity)
        else:
            print("Error: class <Scene> function (remove) -> The {} entity was not added to the {} scene.".format(entity, self.name))

    def get(self, entity):
        if entity in self.__entities:
            return self.__entities[entity]
        else:
            print("Error: class <Scene> function (get) -> The {} entity was not added to the {} scene.".format(entity, self.name))

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

    def getSurface(self):
        return self.__surface

    def setCamera(self, entity):
        if entity.has("Camera"):
            self.__camera = entity
        else:
            print("Error: class <Scene> function (setCamera) -> The {} entity does not have a Camera component.".format(entity.name))

    def getCamera(self):
        return self.__camera

    def isRendering(self):
        return self.__rendering
    
    def isUpdating(self):
        return self.__updating

    def render(self):
        self.__rendering = True
        
        # clear surface
        self.__surface.fill(self.background_color)

        for layer in self.__layers:
            # render tilemaps
            entities = self.__layers[layer].getEntitiesWithComponent("Tilemap")
            if len(entities) > 0:
                for entity in entities:
                    tilemap = entity.get("Tilemap")
                    image, rect = tilemap.getDrawImage()

                    if self.__camera == None:
                        self.__surface.blit(image, rect)
                    else:
                        self.__surface.blit(image, self.__camera.get("Camera").apply(rect))

            # render sprites
            entities = self.__layers[layer].getEntitiesWithComponent("Sprite Renderer")
            if len(entities) > 0:
                for entity in entities:
                    if not entity.has("Transform"): continue
                    transform = entity.get("Transform")
                    sprite_renderer = entity.get("Sprite Renderer")
                    image, rect = sprite_renderer.getDrawImage()

                    if self.__camera == None:
                        self.__surface.blit(image, rect)
                    else:
                        if sprite_renderer.follow_camera:
                            self.__surface.blit(image, self.__camera.get("Camera").apply(rect))
                        else:
                            self.__surface.blit(image, rect)

        # environment light
        self.__environment_surface.fill(self.environment_light)
        
        # lights
        for layer in self.__layers:
            # render lights
            entities = self.__layers[layer].getEntitiesWithComponent("Light")
            if len(entities) > 0:
                for entity in entities:
                    light = entity.get("Light")
                    image, rect = light.getDrawImage()

                    if self.__camera == None:
                         self.__environment_surface.blit(image, rect)

                    else:
                        if light.follow_camera:
                            self.__environment_surface.blit(image, self.__camera.get("Camera").apply(rect))
                        else:
                            self.__environment_surface.blit(image, rect)

        self.__surface.blit(self.__environment_surface, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

        # render physics
        if self.render_physics:
            entities = self.getEntitiesWithComponent("Box Collider")
            for entity in entities:
                if not entity.has("Transform"): continue
                collider = entity.get("Box Collider")
                transform = entity.get("Transform")
                
                rect = pygame.Rect(transform.position.x, transform.position.y, collider.width, collider.height)

                if self.__camera != None:
                    rect = self.__camera.get("Camera").apply(rect)

                pygame.draw.rect(self.__surface, self.__app.physics_color, rect, 1)


        if self.__adjust_surface:
            display_width = self.__app.window.getDisplay().get_width()
            display_height = self.__app.window.getDisplay().get_height()

            w, h, = display_width, display_height
            x, y = 0, 0

            if self.__max_surface_width != None:
                if w > self.__max_surface_width:
                    w = int(self.__max_surface_width)

            if self.__max_surface_height != None:
                if h > self.__max_surface_height:
                    h = int(self.__max_surface_height)

            if w != display_width:
                x = int((display_width / 2) - (w / 2))

            if h != display_height:
                y = int((display_height / 2) - (h / 2))


            self.__app.window.getDisplay().blit(pygame.transform.scale(self.__surface, (w, h)), (x, y))
        else:
            self.__app.window.getDisplay().blit(self.__surface, (x, y))

        self.__rendering = False

    def update(self):
        if not self.__rendering:
            self.__updating = True

            # add entities in queue
            for entity, layer in self.__add_queue:
                self.__add(entity, layer)
            self.__add_queue.clear()

            # remove entities in queue
            for entity, layer in self.__remove_queue:
                 self.__remove(entity, layer)
            self.__remove_queue.clear()

            # camera first update
            if self.__camera != None and not self.__cameraFirstUpdate:
                self.__camera.update()
                self.__cameraFirstUpdate = True

            # update entities
            for layer in self.__layers:
                for entity in self.__layers[layer].getEntities():
                    if self.__camera != None:
                        if entity.has("Camera") and entity.name == self.__camera.name:  continue
                    entity.update()

            # update camera
            if self.__camera != None:
                self.__camera.update()

        self.__updating = False