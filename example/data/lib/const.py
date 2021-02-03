from godity.engine import getMonitorSize

MONITOR_SIZE = getMonitorSize()
PIXEL_SIZE = 5

SCREEN_WIDTH = int(MONITOR_SIZE[0] / PIXEL_SIZE)
SCREEN_HEIGHT = int(MONITOR_SIZE[1] / PIXEL_SIZE)