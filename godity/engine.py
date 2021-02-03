import pygame
pygame.init()
from pygame.locals import *

# core
from godity.core import *

# math
from godity.math import *

# components
from godity.components import *

# inputs
from godity.inputs import *

def getMonitorSize():
    info = pygame.display.Info()
    return (info.current_w, info.current_h)