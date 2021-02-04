from godity.engine import *
from data.lib import *

class Game(App):
	def __init__(self, width, height, title):
		super().__init__(width, height, title)

	def start(self):
		# load images
		self.loadImage("character", "data/images/character.png")
		self.loadImage("blob", "data/images/blob.png")
		self.loadImage("sky", "data/images/sky_static.png")
		self.loadImage("sky with sun", "data/images/sky_static_withsun.png")
		self.loadImage("clouds", "data/images/clouds.png")
		self.loadImage("mountains", "data/images/mountains.png")
		self.loadImage("light 350 hard", "data/images/light_350_hard.png")
		self.loadImage("light2", "data/images/light2.png")
		#---

		self.physics_color = (255,255,255)

		# layers
		self.bg_layer = Layer("Background")
		self.tilemap_layer = Layer("Tilemaps")
		self.game_layer = Layer("Game")
		self.light_layer = Layer("Light")
		#---

		# scenes
		self.game_scene = Scene(self, "Game", SCREEN_WIDTH, SCREEN_HEIGHT, True, False, (5,20,20))
		self.game_scene.background_color = (50,155,255)
		#---

		# entities
		self.player = Player(self, 50, 50, 10, 22)
		self.camera = Entity("Camera")
		self.world = Entity("World")

		self.light = Entity("Light")
		self.light.add(Transform(Vector2(0,0)))
		self.light.add(Light(self, 128, (100,255,255), "light 350 hard"))

		self.light2 = Entity("Light 2")
		self.light2.add(Transform(Vector2(100,300)))
		self.light2.add(Light(self, (318,216), (255,255,150), "light2"))

		# background
		self.sky = Entity("Sky")
		self.sky.add(Transform(Vector2(0,0), Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)))
		self.sky.add(SpriteRenderer(self, "sky", follow_camera=False))

		self.clouds = Entity("Clouds")
		self.clouds.add(Transform(Vector2(0,0), Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)))
		self.clouds.add(SpriteRenderer(self, "clouds", follow_camera=False))

		self.mountains = Entity("Mountains")
		self.mountains.add(Transform(Vector2(0,0), Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)))
		self.mountains.add(SpriteRenderer(self, "mountains", follow_camera=False))
		#---

		# creating a tilemap
		self.world.add(Transform())
		self.world.add(Tilemap("data/maps/world.tmx", 0, 2))

		# creating a camera
		self.camera.add(Transform())
		self.camera.add(Camera(SCREEN_WIDTH, SCREEN_HEIGHT, -4, -8, self.world.get("Tilemap").width, self.world.get("Tilemap").height))
		#---

		self.spawnEnemies = Entity("Spawn Enemies")
		self.spawnEnemies.add(SpawnEnemies(self, self.world, "Game"))
		#---

		# adding layers in game scene
		self.game_scene.addLayer(self.bg_layer)
		self.game_scene.addLayer(self.tilemap_layer)
		self.game_scene.addLayer(self.game_layer)
		self.game_scene.addLayer(self.light_layer)
		
		# set camera in game scene
		self.game_scene.setCamera(self.camera)

		# parent entities
		self.camera.parent(self.player)
		self.light.parent(self.player, 4, 8)

		# adding entities in game scene
		self.game_scene.add(self.sky, "Background")
		self.game_scene.add(self.clouds, "Background")
		self.game_scene.add(self.mountains, "Background")

		self.game_scene.add(self.world, "Tilemaps")

		self.game_scene.add(self.player, "Game")
		self.game_scene.add(self.spawnEnemies, "Game")
		#self.game_scene.add(self.light2, "Light")
		self.game_scene.add(self.light, "Light")
		#---

		# set game scene in app
		self.setScene(self.game_scene)


	def update(self):
		self.window.update()
		self.getScene().update()
		#print(self.player.get("Box Collider").collide_objects)

	def render(self):
		#self.window.clearColor((0,0,0))
		self.getScene().render()

	def end(self):
		print("end app")

if __name__ == "__main__":
	monitor_size = getMonitorSize()
	#game = Game(1024, 720, "Godity - Platform Game")
	# FULLSCREEN
	game = Game(monitor_size[0], monitor_size[1], "Godity - Platform Game")
	game.run()