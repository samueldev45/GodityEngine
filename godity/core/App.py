import pygame
import sys, time

from godity.core.Window import Window
from godity.core.Scene import Scene

class App():
    def __init__(self, width, height, title, flags=0, fps=60, exit_key=pygame.K_ESCAPE):
        # initialize pygame
        if not pygame.get_init():
            pygame.init()
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        if not pygame.font.get_init():
            pygame.font.init()
        if not pygame.joystick.get_init():
            pygame.joystick.init()

        # variables
        self.__images = {}
        self.__audios = {}
        self.__scene = None
        self.__fps = fps
        self.__clock = pygame.time.Clock()
        self.__game_loop = True
        self.__last_time = 0
        self.__delta_time = 0.0
        self.__flags = flags

        self.gravity = 9.807
        self.physics_color = (255,255,255)
        self.exit_key = exit_key

        # create window
        self.window = Window(width, height, title, self.__flags)

    # Overwrite functions
    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def end(self):
        pass
    #--------------------

    def getEvents(self):
        return pygame.event.get()

    def getClock(self):
        return self.__clock

    def getFlags(self):
        return self.__flags

    def getDeltaTime(self):
        return self.__delta_time

    def getScene(self):
        if self.__scene != None:
            return self.__scene
        else:
            print("Error: class <App> function (getScene) -> No scene have been defined for the App.")

    def setScene(self, scene):
        if type(scene) is Scene:
            self.__scene = scene
        else:
            print("Error: class <App> function (setScene) -> A valid godity.core.Scene was not passed for the scene parameter.")

    def getImage(self, name):
        if name in self.__images:
            return self.__images[name]
        else:
            print("Error: class <App> function (getImage) -> No image was found with the identifier {}.".format(name))

    def loadImage(self, name, path, convert_alpha=False):
        if not name in self.__images:
            if convert_alpha:   self.__images[name] = pygame.image.load(path).convert_alpha()
            else:   self.__images[name] = pygame.image.load(path)
        else:
            print("Error: class <App> function (loadImage) -> The identifier {} has already been used.".format(name))

    def updateImage(self, name, path, convert_alpha=False):
        if convert_alpha:   self.__images[name] = pygame.image.load(path).convert_alpha()
        else:   self.__images[name] = pygame.image.load(path)

    def deleteImage(self, name):
        if name in self.__images:
            del self.__images[name]
        else:
            print("Error: class <App> function (deleteImage) -> No image was found with the identifier {}.".format(name))

    def getAudio(self, name):
        if name in self.__audios:
            return self.__audios[name]
        else:
            print("Error: class <App> function (getAudio) -> No audio was found with the identifier {}.".format(name))

    def deleteAudio(self, name):
        if name in self.__audios:
            del self.__audios[name]
        else:
            print("Error: class <App> function (deleteAudio) -> No audio was found with the identifier {}.".format(name))

    def playAudio(self, name):
        if name in self.__audios:
            self.__audios[name].play()
        else:
            print("Error: class <App> function (playAudio) -> No audio was found with the identifier {}.".format(name))

    def stopAudio(self, name):
        if name in self.__audios:
            self.__audios[name].stop()
        else:
            print("Error: class <App> function (stopAudio) -> No audio was found with the identifier {}.".format(name))

    def loadAudio(self, name, path):
        if not name in self.__audios:
            self.__audios[name] = pygame.mixer.Sound(path)
        else:
            print("Error: class <App> function (loadAudio) -> The identifier {} has already been used.".format(name))

    def close(self):
        self.__game_loop = False

    def setFPS(self, value):
        self.__fps = value

    def __events(self):
        for event in self.getEvents():
            if event.type == pygame.QUIT:
                self.close()
            if event.type == pygame.KEYDOWN:
                if event.key == self.exit_key:
                    self.close()
            break

    def run(self):
        self.start()
        self.__last_time = time.time()
        while self.__game_loop:
            self.__delta_time = time.time() - self.__last_time
            self.__delta_time *= self.__fps
            self.__last_time = time.time()
            
            self.__events()
            self.update()
            self.render()
            self.__clock.tick(self.__fps)
        self.end()
        sys.exit(0)