from godity.core.Component import Component
from data.lib.enemies import *

class SpawnEnemies(Component):
	def __init__(self, app, tilemap_entity, layer):
		args = {
			"app"			 : app,
			"tilemap entity" : tilemap_entity,
			"layer"			 : layer
		}
		super().__init__("Spawn Enemies", args)

	def start(self):
		self.__app = self.args["app"]
		self.tilemap_entity = self.args["tilemap entity"]
		self.layer = self.args["layer"]

		tilemap = self.tilemap_entity.get("Tilemap")

		enemy_id = 0

		for tile_object in tilemap.tmx_data.objects:
			if tile_object.name == "enemy_blob":
				entity = Blob(self.__app, enemy_id, tile_object.x, tile_object.y, tile_object.width, tile_object.height, ["enemy"])
				entity.update()
				self.entity.getScene().add(entity, self.layer)
			enemy_id += 1


	def update(self):
		pass