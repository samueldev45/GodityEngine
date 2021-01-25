class Scene():
    def __init__(self, name):
        self.name = name
        self.__entities = {}

    def add(self, entity):
        if not entity.name in self.__entities:
            entity.scene = self
            self.__entities[entity.name] = entity
        else:
            print("Error: class <Scene> function (add) -> The "+entity.name+" entity has already been added to the "+self.name+" scene.")

    def remove(self, entity):
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

    def update(self):
        for entity in self.__entities:
            self.__entities[entity].update()

    def getEntitiesWithComponent(self, component):
        entities = []
        for entity in self.__entities:
            if self.__entities[entity].has(component):
                entities.append(self.__entities[entity])
        return entities

    def render(self, surface):
        entities = self.getEntitiesWithComponent("Sprite Renderer")
        if len(entities) > 0:
            for entity in entities:
                if not entity.has("Transform"): continue
                transform = entity.get("Transform")
                sprite_renderer = entity.get("Sprite Renderer")
                image, rect = sprite_renderer.getDrawImage()
                surface.blit(image, rect)