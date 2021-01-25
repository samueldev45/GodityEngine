from godity.engine import *

# custom components
from playerController import PlayerController

class Game(App):
    def __init__(self, width, height, title, flags=0):
        super().__init__(width, height, title, flags)

    def start(self):
        self.gameScene = Scene(name=Game, render_physics=True)
        # load images
        self.loadImage("cube", "cube.png")
        #---

        # entities
        self.platform = Entity(name="Platform")
        self.player = Entity(name="Player")
        self.camera = Entity(name="Camera")
        self.cube = Entity(name="Cube")
        #---

        # add components in entities
        self.platform.add(Transform(position=Vector2(-96, 300)))
        self.platform.add(BoxCollider(width=256, height=16))

        self.player.add(Transform(position=Vector2(0, 0), scale=Vector2(64, 64)))
        self.player.add(BoxCollider(width=64, height=64))
        self.player.add(Rigidbody(app=self, use_gravity=False))
        self.player.add(PlayerController(speed=5))
        self.player.add(SpriteRenderer(app=self, image_name="cube"))

        self.cube.add(Transform(position=Vector2(-64, 0)))
        self.cube.add(BoxCollider(width=32, height=32))
        self.cube.add(Rigidbody(app=self, mass=10))

        self.camera.add(Transform(position=Vector2(0,0)))
        self.camera.add(Camera(screen_width=800, screen_height=600, offset_x=-32, offset_y=-32))
        #---

        self.camera.parent(self.player)

        self.gameScene.add(self.platform)
        self.gameScene.add(self.player)
        self.gameScene.add(self.cube)
        self.gameScene.add(self.camera)

        self.gameScene.setCamera(self.camera)
        self.setScene(self.gameScene)

        print("started app")

    def update(self):
        self.window.update()
        self.getScene().update()

    def render(self):
        self.window.clearColor((0,0,0))
        self.getScene().render(self.window.getDisplay())

    def end(self):
        print("end app")

game = Game(width=800, height=600, title="Godity Engine", flags=0)
game.run()