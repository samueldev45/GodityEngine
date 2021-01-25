class Component():
    def __init__(self, name, args):
        self.name = name
        self.args = args
        self.entity = None

        self.started = False

    def start(self):
        pass

    def update(self):
        pass