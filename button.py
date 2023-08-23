import pygame


# button class creates a button that changes image when the mouse is over it and returns true when the player clicks on it
class Button():
	def __init__(self, x, y, image, image_hover, scale):
		width = image.get_width()
		height = image.get_height()
		self.original_image = image
		self.original_image_hover = image_hover
		self.original_x = x / scale
		self.original_y = y / scale
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.image_hover = pygame.transform.scale(image_hover, (int(width * scale), int(height * scale)))
		self.image_in_use = self.image
		self.rect = self.image_in_use.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		mouse_pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(mouse_pos):
			self.image_in_use = self.image_hover
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
		else:
			self.image_in_use = self.image

		if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image_in_use, (self.rect.x, self.rect.y))

		return action