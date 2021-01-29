from godity.core.Entity import Entity
from godity.math.Vector2 import Vector2

# import defaults components
from godity.components.Transform import Transform
from godity.components.BoxCollider import BoxCollider
from godity.components.Rigidbody import Rigidbody
from godity.components.SpriteRenderer import SpriteRenderer
from godity.components.Animation import Animation

# import custom components
from data.lib.PlatformerController import PlatformerController
from data.lib.AnimationController import AnimationController
from data.lib.ResetPosition import ResetPosition

class Player(Entity):
	def __init__(self, app, x, y, sx, sy):
		super().__init__("Player")
		self.add(Transform(Vector2(x, y), Vector2(22, 22)))
		self.add(BoxCollider(sx, sy))
		self.add(Rigidbody(app, 2, 5, True))
		self.add(PlatformerController(app, 5, 5))
		self.add(SpriteRenderer(app, "character", (0,2), 22, 22, -7, 0, False, False, False))

		# animations
		self.add(Animation("Idle", "character", [(0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2)], 0.08))
		self.add(Animation("Jump", "character", [(0,1), (1,1), (2,1), (3,1), (4,1), (5,1)], 0.1))
		self.add(Animation("Falling", "character", [(4,1)], 0.1))
		self.add(Animation("Run", "character", [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0)], 0.05))

		# animation controller
		self.add(AnimationController())

		self.add(ResetPosition())