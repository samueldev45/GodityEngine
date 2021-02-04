import pygame

def keyPressed(key):
	pressed = pygame.key.get_pressed()
	try:
		if pressed[pygame.key.key_code(key)]:
			return True
	except:
		return False
	return False

def mousePressed(button):
	mouse = pygame.mouse.get_pressed()
	try:
		if mouse[button]:
			return True
	except:
		return False
	return False