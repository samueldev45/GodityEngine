from godity.core.Component import Component
from godity.core.Entity import Entity
from godity.components.Transform import Transform
from godity.components.BoxCollider import BoxCollider
from godity.math.Vector2 import Vector2
import pytmx, pygame

class Tilemap(Component):
    def __init__(self, file_path, alpha_background=False):
        args = {
            "file path"        : file_path,
            "alpha background" : alpha_background
        }
        super().__init__("Tilemap", args)

    def start(self):
        self.__file_path = self.args["file path"]
        self.__alpha_background = self.args["alpha background"]

        self.tmx_data = pytmx.load_pygame(self.__file_path) # pixelalpha=True
        self.width = self.tmx_data.width * self.tmx_data.tilewidth
        self.height = self.tmx_data.height * self.tmx_data.tileheight

        self.image = pygame.Surface((self.width, self.height))
        ti = self.tmx_data.get_tile_image_by_gid

        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        self.image.blit(tile, (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))

        collider_id = 0

        # add 
        for tile_object in self.tmx_data.objects:
            if tile_object.name == "box_collider" or tile_object.name == "platform":
                collider_id += 1
                collider = Entity("Collider_"+str(collider_id))
                collider.add(Transform(Vector2(tile_object.x, tile_object.y), Vector2(tile_object.width, tile_object.height), 0))

                if tile_object.name == "box_collider":
                    collider.add(BoxCollider(tile_object.width, tile_object.height))
                elif tile_object.name == "platform":
                    collider.add(BoxCollider(tile_object.width, tile_object.height, False, True))
            
                collider.update()
                self.entity.getScene().add(collider)

    def getDrawImage(self):
        transform = self.entity.get("Transform")
        image = self.image
        if self.__alpha_background:
            image.set_colorkey((0,0,0))
        rect = image.get_rect(x=transform.position.x, y=transform.position.y)
        return [image, rect]

    def update(self):
        pass