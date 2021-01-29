from godity.engine import *
from data.lib import *

class Game(App):
	def __init__(self, width, height, title):
		super().__init__(width, height, title)

	def start(self):

		# load images
		self.loadImage("character", "data/images/character.png")
		#---

		self.physics_color = (255,255,255)

		# scenes
		self.game_scene = Scene(self, "Game", SCREEN_WIDTH, SCREEN_HEIGHT, True, False)
		self.game_scene.background_color = (50,155,255)
		#---

		# entities
		self.player = Player(self, 50, 50, 10, 22)
		self.camera = Entity("Camera")
		self.world = Entity("World")
		#---

		# creating a camera
		self.camera.add(Transform())
		self.camera.add(Camera(SCREEN_WIDTH, SCREEN_HEIGHT, -4, -8))
		#---

		# creating a tilemap
		self.world.add(Transform())
		self.world.add(Tilemap("data/maps/world.tmx", True))
		#---

		# adding entities in game scene
		
		self.game_scene.add(self.world)
		self.game_scene.add(self.player)
		#---

		# parent camera to player
		self.camera.parent(self.player)
		
		# set camera in game scene
		self.game_scene.setCamera(self.camera)

		# set game scene in app
		self.setScene(self.game_scene)


	def update(self):
		self.window.update()
		self.getScene().update()

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