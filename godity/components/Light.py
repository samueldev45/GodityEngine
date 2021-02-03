from godity.core.Component import Component
import pygame

class Light(Component):
	def __init__(self, app, radius, color=(255,255,255), image_name=None, follow_camera=True, smooth_scale=False):
		args = {
			"app"           : app,
			"radius"        : radius,
			"color"         : color,
			"image name"    : image_name,
			"follow camera" : follow_camera,
			"smooth scale"  : smooth_scale
		}
		super().__init__("Light", args)

	def start(self):
		self.__app = self.args["app"]
		self.radius = self.args["radius"]
		self.color = self.args["color"]
		self.image_name = self.args["image name"]
		self.follow_camera = self.args["follow camera"]
		self.smooth_scale = self.args["smooth scale"]

	def getDrawImage(self):
		transform = self.entity.get("Transform")

		radius = []
		if type(self.radius) is int:
			radius = [self.radius, self.radius]
		if type(self.radius) is list or type(self.radius) is tuple:
			radius = self.radius

		if self.image_name != None:
			image = self.__app.getImage(self.image_name)
			if self.smooth_scale:
				image = pygame.transform.smoothscale(image, radius)
			else:
				image = pygame.transform.scale(image, radius)
		else:
			image = pygame.Surface(radius, pygame.SRCALPHA, 32).convert_alpha()
			pygame.draw.circle(image, (255,255,255), (radius[0] / 2, radius[0] / 2), radius[0] / 2)

		rect = image.get_rect()

		color_surface = pygame.Surface((rect.width, rect.height))
		color_surface.fill(self.color)

		image.blit(color_surface, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

		
		rect.x = transform.position.x - (rect.width / 2)
		rect.y = transform.position.y - (rect.height / 2)

		return [image, rect]

	def update(self):
		pass