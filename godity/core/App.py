import pygame
import sys

from godity.core.Window import Window

class App():
    def __init__(self, width, height, title, flags=0, fps=60):
        # initialize pygame
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        # variables
        self.__images = {}
        self.__audios = {}
        self.__scene = None
        self.__FPS = fps
        self.__clock = pygame.time.Clock()

        self.gameLoop = True

        # create window
        self.window = Window(width, height, title, flags)

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

    def getScene(self):
        return self.__scene

    def setScene(self, scene):
        self.__scene = scene

    def getImage(self, name):
        if name in self.__images:
            return self.__images[name]
        else:
            print("Error: class <App> function (getImage) -> No image was found with the identifier "+name+".")

    def loadImage(self, name, path):
        if not name in self.__images:
            self.__images[name] = pygame.image.load(path)
        else:
            print("Error: class <App> function (loadImage) -> The identifier "+name+" has already been used.")

    def deleteImage(self, name):
        if name in self.__images:
            del self.__images[name]
        else:
            print("Error: class <App> function (deleteImage) -> No image was found with the identifier "+name+".")

    def getAudio(self, name):
        if name in self.__audios:
            return self.__audios[name]
        else:
            print("Error: class <App> function (getAudio) -> No audio was found with the identifier "+name+".")

    def deleteAudio(self, name):
        if name in self.__audios:
            del self.__audios[name]
        else:
            print("Error: class <App> function (deleteAudio) -> No audio was found with the identifier "+name+".")

    def playAudio(self, name):
        if name in self.__audios:
            self.__audios[name].play()
        else:
            print("Error: class <App> function (playAudio) -> No audio was found with the identifier "+name+".")

    def stopAudio(self, name):
        if name in self.__audios:
            self.__audios[name].stop()
        else:
            print("Error: class <App> function (stopAudio) -> No audio was found with the identifier "+name+".")

    def loadAudio(self, name, path):
        if not name in self.__audios:
            self.__audios[name] = pygame.mixer.Sound(path)
        else:
            print("Error: class <App> function (loadAudio) -> The identifier "+name+" has already been used.")

    def close(self):
        self.gameLoop = False

    def setFPS(self, value):
        self.__FPS = value

    def __checkCloseWindow(self):
        for event in self.getEvents():
            if event.type == pygame.QUIT:
                self.close()

    def run(self):
        self.start()
        while self.gameLoop:
            self.__clock.tick(self.__FPS)
            self.__checkCloseWindow()
            self.update()
            self.render()
        self.end()
        sys.exit(0)