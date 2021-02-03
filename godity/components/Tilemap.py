from godity.core.Component import Component
from godity.core.Entity import Entity
from godity.components.Transform import Transform
from godity.components.BoxCollider import BoxCollider
from godity.math.Vector2 import Vector2
import pytmx, pygame

class Tilemap(Component):
    def __init__(self, file_path, object_offset_x=0, object_offset_y=0):
        self.tmx_data = pytmx.load_pygame(file_path)
        self.width = self.tmx_data.width * self.tmx_data.tilewidth
        self.height = self.tmx_data.height * self.tmx_data.tileheight

        args = {
           "object offset x" : object_offset_x,
           "object offset y" : object_offset_y
        }

        super().__init__("Tilemap", args)

    def start(self):
        self.object_offset_x = self.args["object offset x"]
        self.object_offset_y = self.args["object offset y"]

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32).convert_alpha()
        ti = self.tmx_data.get_tile_image_by_gid

        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        self.image.blit(tile, (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))

        collider_id = 0
 
        for tile_object in self.tmx_data.objects:
            if tile_object.name == "box_collider" or tile_object.name == "platform":
                collider_id += 1
                collider = Entity("Collider_{}".format(collider_id))
                collider.addTag(tile_object.name)
                collider.add(Transform(Vector2(tile_object.x + self.object_offset_x, tile_object.y + self.object_offset_y), Vector2(tile_object.width, tile_object.height), 0))

                if tile_object.name == "box_collider":
                    collider.add(BoxCollider(tile_object.width, tile_object.height))
                elif tile_object.name == "platform":
                    collider.add(BoxCollider(tile_object.width, tile_object.height, False, True))
            
                collider.update()
                self.entity.getScene().add(collider, self.entity.getLayer().name)

    def getDrawImage(self):
        transform = self.entity.get("Transform")
        image = self.image
        rect = image.get_rect(x=transform.position.x, y=transform.position.y)
        return [image, rect]

    def update(self):
        pass