from godity.core.Component import Component
from godity.math.Vector2 import Vector2
from godity.inputs import *

class PlatformerController(Component):
	def __init__(self, app, velocity, jump_force):
		args = {
			"app"        : app,
			"velocity"   : velocity,
			"jump force" : jump_force
		}
		super().__init__("Platformer Controller", args)

	def start(self):
		self.__app = self.args["app"]
		self.velocity = self.args["velocity"]
		self.jump_force = self.args["jump force"]
		self.space_tap = False

	def releaseInputs(self):
		if not keyPressed("space") and self.space_tap == True:
			self.space_tap = False

	def getInputs(self):
		keyboard = pygame.key.get_pressed()
		sprite_renderer = self.entity.get("Sprite Renderer")

		# get components
		box_collider = self.entity.get("Box Collider")

		rigidbody = self.entity.get("Rigidbody")

		# set speed
		rigidbody.velocity = self.velocity * self.__app.getDeltaTime()

		# inputs
		if keyPressed("left"):
			rigidbody.direction.x = -1
			sprite_renderer.setFlip(True, False)

		elif keyPressed("right"):
			rigidbody.direction.x = 1
			sprite_renderer.setFlip(False, False)

		if keyPressed("space") and self.space_tap == False and rigidbody.air_time < 0.2:
			rigidbody.jump(self.jump_force)
			self.space_tap = True

	def update(self):
		self.releaseInputs()
		self.getInputs()