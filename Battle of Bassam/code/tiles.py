import pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,size):
		super().__init__()
		self.image = pygame.Surface((32,32))
		self.image.fill('grey')
		self.rect = self.image.get_rect(midbottom = pos)

	def update(self,x_shift):
		self.rect.x += x_shift