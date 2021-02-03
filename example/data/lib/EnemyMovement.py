from godity.core.Component import Component
from godity.core.Timer import Timer

class EnemyMovement(Component):
	def __init__(self, app, initial_direction, speed, change_direction_seconds):
		args = {
			"app"					   : app,
			"initial direction"        : initial_direction,
			"speed"					   : speed,
			"change direction seconds" : change_direction_seconds
		}
		super().__init__("Enemy Movement", args)

	def start(self):
		self.__app = self.args["app"]
		self.direction = self.args["initial direction"]
		self.speed = self.args["speed"]
		self.change_direction_seconds = self.args["change direction seconds"]

		self.__timer = Timer()

	def collisionCallback(self):
		box_collider = self.entity.get("Box Collider")

	def changeDirection(self):
		rigidbody = self.entity.get("Rigidbody")
		if self.__timer.getTime() >= self.change_direction_seconds:
			self.direction *= -1
			self.__timer.resetTime()

	def move(self):
		rigidbody = self.entity.get("Rigidbody")
		sprite_renderer = self.entity.get("Sprite Renderer")

		# set speed
		rigidbody.velocity = self.speed * self.__app.getDeltaTime()

		# set direction
		rigidbody.direction.x = self.direction

		# set flip
		flip = True
		if self.direction == -1:	flip = False
		sprite_renderer.setFlip(flip, False)

		self.collisionCallback()
		self.changeDirection()

	def update(self):
		self.move()