import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		self.import_character_assets()
		self.frame_index = 0
		self.animation_speed = 0.6
		self.image = self.animations['idle'][self.frame_index]
		self.image = pygame.Surface((32,56))
		self.image.fill('red')
		self.rect = self.image.get_rect(midbottom = pos)

		#player movement
		self.direction = pygame.math.Vector2(0,0)
		self.speed = 8
		self.gravity = 1.6
		self.jump_speed = -16
		self.standing_count = True
		self.standing = 0

		#player status
		self.status = 'idle'
		self.facing_right = True
		self.on_ground = False
		self.on_ceiling = False
		self.on_left = False
		self.on_right = False

	def import_character_assets(self):
		character_path = '../Sprites/Character/Wisam/'
		self.animations = {'idle':[],'walk':[],'jump':[],'fall':[]}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def animate(self):
		animation = self.animations[self.status]

		# loop over frame index
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		image = animation[int(self.frame_index)]
		if self.facing_right:
			self.image = image
		else:
			flipped_image = pygame.transform.flip(image,True,False)
			self.image = flipped_image

		# set the rect
		if self.on_ground and self.on_right:
			self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
		elif self.on_ground and self.on_left:
			self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
		elif self.on_ground:
			self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
		elif self.on_ceiling and self.on_right:
			self.rect = self.image.get_rect(topright = self.rect.topright)
		elif self.on_ceiling and self.on_left:
			self.rect = self.image.get_rect(topleft = self.rect.topleft)
		elif self.on_ceiling:
			self.rect = self.image.get_rect(midtop = self.rect.midtop)


	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_d]:
			self.direction.x = 1
			self.facing_right = True
			self.standing_count = False
			self.standing = 0
		elif keys[pygame.K_a]:
			self.direction.x = -1
			self.facing_right = False
			self.standing_count = False
			self.standing = 0
		else:
			self.speed = 0
			self.direction.x = 0
			self.standing_count = True

		#horizontal movement
		if self.direction.x > 0:
			self.speed += 0.5
			if self.speed > 8:
				self.speed = 8
		if self.direction.x < 0:
			self.speed += 0.5
			if self.speed > 8:
				self.speed = 8

		#preventing left and right presses:
		if keys[pygame.K_a] and keys[pygame.K_d]:
			self.speed = 0
			self.direction.x = 0

		if keys[pygame.K_SPACE]:
			if self.on_ground:
				self.jump()

	def get_status(self):
		if self.direction.y < 0:
			self.status = 'jump'
		elif self.direction.y > 0:
			self.status = 'fall'
		else:
			if self.direction.x != 0:
				self.status = 'walk'
			else:
				self.status = 'idle'

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	def jump(self):
		self.direction.y = self.jump_speed

	def update(self):
		self.get_input()
		self.get_status()
		self.animate()
		print(self.rect.centerx)
