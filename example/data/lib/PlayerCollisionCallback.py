from godity.core.Component import Component

class PlayerCollisionCallback(Component):
	def __init__(self):
		args = {

		}
		super().__init__("Player Collision Callback", args)

	def start(self):
		pass

	def collisionCallback(self):
		box_collider = self.entity.get("Box Collider")

		if len(box_collider.collide_objects) > 0:
			for entity_name in box_collider.collide_objects:
				collide_list = box_collider.collide_objects[entity_name]

				if collide_list["entity"].hasTag("enemy"):
					if collide_list["collision types"]["bottom"]:
						collide_list["entity"].end()

	def update(self):
		self.collisionCallback()