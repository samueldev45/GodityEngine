from godity.core.Component import Component
from godity.math.Vector2 import Vector2

class ResetPosition(Component):
	def __init__(self):
		args = {

		}
		super().__init__("Reset Position", args)

	def start(self):
		pass

	def update(self):
		transform = self.entity.get("Transform")
		rigidbody = self.entity.get("Rigidbody")

		if transform.position.y > 800:
			transform.setPosition(Vector2(50, 50))
			rigidbody.gravity = 0
			rigidbody.air_time = 0
