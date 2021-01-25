
class Entity():
    def __init__(self, name):
        self.__components = {}
        self.__tags = []
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
            print("Error: class <Entity> function (remove) -> The component "+component+" was not added to the entity "+self.name+".")

    def has(self, component):
        if component in self.__components:
            return True
        return False

    def get(self, component):
        if component in self.__components:
            return self.__components[component]
        else:
            print("Error: class <Entity> function (get) -> The component "+component+" was not added to the entity "+self.name+".")

    def addTag(self, name):
        if not name in self.__tags:
            self.__tags.append(name)
        else:
            print("Error: class <Entity> function (addTag) -> The "+name+" tag has already been added to entity "+self.name+".")

    def removeTag(self, name):
        if name in self.__tags:
            self.__tags.remove(name)
        else:
            print("Error: class <Entity> function (removeTag) -> The "+name+" tag was not added to entity "+self.name+".")

    def hasTag(self, name):
        if name in self.__tags:
            return True
        return False

    def getChildrens(self):
        return self.childrens

    def parent(self, entity):
        if not self in entity.getChildrens():
            entity.childrens.append(self)

    def getScene(self):
        return self.scene

    def update(self):
        for component in self.__components:
            if not self.__components[component].started:
                self.__components[component].start()
                self.__components[component].started = True
            else:
                self.__components[component].update()