from godity.engine import *

# custom components
from playerController import PlayerController

class Game(App):
    def __init__(self, width, height, title, flags=0):
        super().__init__(width, height, title, flags)

    def start(self):
        self.gameScene = Scene("Game", True)
        # load images
        self.loadImage("cube", "cube.png")
        #---

        # entities
        self.platform = Entity("Platform")
        self.player = Entity("Player")
        self.camera = Entity("Camera")
        self.cube = Entity("Cube")
        #---

        # add components in entities
        self.platform.add(Transform(Vector2(-96, 300)))
        self.platform.add(BoxCollider(256, 16))

        self.player.add(Transform(Vector2(0, 0), Vector2(64, 64)))
        self.player.add(BoxCollider(64, 64))
        self.player.add(Rigidbody(self, 5, 1, False))
        self.player.add(PlayerController(5))
        self.player.add(SpriteRenderer(self, "cube"))

        self.cube.add(Transform(Vector2(-64, 0)))
        self.cube.add(BoxCollider(32, 32))
        self.cube.add(Rigidbody(self, 2, 10, True))

        self.camera.add(Transform(Vector2(0,0)))
        self.camera.add(Camera(800, 600, -32, -32))
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

game = Game(800, 600, "Godity Engine", 0)
game.run()
