class Layer():
	def __init__(self, name):
		self.__entities = {}

		self.name = name

	def add(self, entity):
		if not entity.name in self.__entities:
			self.__entities[entity.name] = entity
		else:
			print("Error: class <Layer> function (add) -> The {} entity has already been added to the {} layer.".format(entity.name, self.name))

	def remove(self, entity):
		if entity in self.__entities:
			del self.__entities[entity]
		else:
			print("Error: class <Layer> function (remove) -> The {} entity was not added to the {} layer.".format(entity, self.name))

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