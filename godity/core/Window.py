import pygame

class Window():
    def __init__(self, width, height, title, flags=0):
        self.width = width
        self.height = height
        self.title = title
        self.flags = flags

        # create display and set title
        self.__display = pygame.display.set_mode((self.width, self.height), flags=flags)
        pygame.display.set_caption(self.title)

    def getDisplay(self):
        return self.__display

    def clearColor(self, color):
        self.__display.fill(color)
    
    def update(self):
        pygame.display.update()