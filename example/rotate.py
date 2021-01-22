from godity.core.Component import Component

class RotateComponent(Component):
    def __init__(self, force):
        args = {
            "force": force
        }
        super().__init__("Rotate Component", args)

    def start(self):
        self.force = self.args["force"]

    def update(self):
        transform = self.entity.get("Transform")
        transform.rotate(self.force)