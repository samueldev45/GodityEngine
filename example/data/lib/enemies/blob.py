from godity.core.Entity import Entity
from godity.math.Vector2 import Vector2

# default components
from godity.components.Transform import Transform
from godity.components.BoxCollider import BoxCollider
from godity.components.Rigidbody import Rigidbody
from godity.components.SpriteRenderer import SpriteRenderer
from godity.components.Animation import Animation

# custom components
from data.lib.EnemyMovement import EnemyMovement

import random

class Blob(Entity):
	def __init__(self, app, id, x, y, sx, sy, tags=[]):
		super().__init__("Blob_{}".format(id))
		# add tags
		if len(tags) > 0:
			for tag in tags:
				self.addTag(tag)

		# add components
		self.add(Transform(Vector2(x, y), Vector2(sx, sy)))
		self.add(BoxCollider(sx, sy))
		self.add(Rigidbody(app))
		self.add(SpriteRenderer(app, "blob", (0,0), 16, 16))
		self.add(EnemyMovement(app, random.choice([-1,1]), 0.5, 2))

		# animations
		self.add(Animation("walk", "blob", [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0)], 0.06, None, True))