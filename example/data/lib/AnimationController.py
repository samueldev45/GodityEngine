from godity.core.Component import Component

class AnimationController(Component):
	def __init__(self):
		args = {

		}
		super().__init__("Animation Controller", args)

	def start(self):
		self.last_air_time = 0

	def update(self):
		rigidbody = self.entity.get("Rigidbody")
		# animations
		idle_anim = self.entity.get("Animation Idle")
		jump_anim = self.entity.get("Animation Jump")
		falling_anim = self.entity.get("Animation Falling")
		run_anim = self.entity.get("Animation Run")

		if not rigidbody.is_jumping:
			if rigidbody.air_time > 0:
				if falling_anim.getState() == "paused":
					idle_anim.pause()
					jump_anim.pause()
					run_anim.pause()

					falling_anim.restart()
					falling_anim.run()
			
			elif rigidbody.direction.x == 0:
				if idle_anim.getState() == "paused":
					falling_anim.pause()
					jump_anim.pause()
					run_anim.pause()

					idle_anim.restart()
					idle_anim.run()

			elif rigidbody.direction.x != 0:
				if run_anim.getState() == "paused":
					falling_anim.pause()
					jump_anim.pause()
					idle_anim.pause()

					run_anim.restart()
					run_anim.run()
		else:
			if jump_anim.getState() == "paused":
				falling_anim.pause()
				idle_anim.pause()
				run_anim.pause()

				jump_anim.restart()
				jump_anim.run()