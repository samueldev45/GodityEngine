from godity.core.Component import Component

class Entity():
    def __init__(self, name):
        self.__components = {}
        self.__tags = []
        
        self.layer = None
        self.scene = None
        self.childrens = []
        self.name = name

    def add(self, component):
        if not component.name in self.__components:
            component.entity = self
            self.__components[component.name] = component

    def remove(self, component):
        if component in self.__components:
            del self.__components[component]
        else:
            print("Error: class <Entity> function (remove) -> The component {} was not added to the entity {}.".format(component, self.name))

    def has(self, component):
        if component in self.__components:
            return True
        return False

    def get(self, component):
        if component in self.__components:
            return self.__components[component]
        else:
            print("Error: class <Entity> function (get) -> The component {} was not added to the entity {}.".format(component, self.name))

    def addTag(self, name):
        if not name in self.__tags:
            self.__tags.append(name)
        else:
            print("Error: class <Entity> function (addTag) -> The {} tag has already been added to entity {}.".format(name, self.name))

    def removeTag(self, name):
        if name in self.__tags:
            self.__tags.remove(name)
        else:
            print("Error: class <Entity> function (removeTag) -> The {} tag was not added to entity {}.".format(name, self.name))

    def hasTag(self, name):
        if name in self.__tags:
            return True
        return False

    def getChildrens(self):
        return self.childrens

    def parent(self, entity, offset_x=0, offset_y=0):
        if not self in entity.getChildrens():
            entity.childrens.append([self, offset_x, offset_y])
        else:
            print("Error: class <Entity> function (parent) -> The entity {} is already parented to the entity {}.".format(self.name, entity.name))

    def clearParent(self):
        self.childrens.clear()

    def getScene(self):
        if self.scene != None:
            return self.scene
        else: 
            print("Error: class <Entity> function (getScene) -> The entity {} is not in any scene.".format(self.name))

    def getLayer(self):
        if self.layer != None:
            return self.layer
        else:
            print("Error: class <Entity> function (getLayer) -> The entity {} is not in any layer.".format(self.name))

    def end(self):
        if self.scene != None:
            self.scene.remove(self.name, self.layer.name)

    def update(self):
        for component in self.__components:
            if not self.__components[component].started:
                self.__components[component].start()
                self.__components[component].started = True
            else:
                self.__components[component].update()