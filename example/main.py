from godity.engine import *

# componentes customizados
from rotate import RotateComponent
from clickPlayAudio import ClickPlayAudio

class Game(App):
    def __init__(self, width, height, title, flags=0):
        super().__init__(width, height, title, flags)

    def start(self):
        # load images
        self.loadImage("image", "image.png")
        #---

        # load audios
        self.loadAudio("audio", "audio.ogg")
        #---

        # scenes
        self.gameScene = Scene(name="Game")
        #---

        # entities
        self.entity = Entity("Entity")
        #---

        # adding components to entities
        self.entity.add(Transform(position=Vector2(400,300)))
        self.entity.add(SpriteRenderer(app=self, image_name="image"))
        self.entity.add(RotateComponent(force=1))
        self.entity.add(ClickPlayAudio(app=self))

        # adding entities in game scene
        self.gameScene.add(self.entity)

        # set game scene
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