import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	print('Starting asteroids!')
	pygame.init() 
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
	asteroids = pygame.sprite.Group()
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	
	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable)
	Shot.containers = (shots, updateable, drawable)
	asteroid_field = AsteroidField()
 
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	
	clock = pygame.time.Clock()
	dt = 0  
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
  
		for obj in updateable:
			obj.update(dt)

			for asteroid in asteroids:
				if asteroid.collision(player):
					print(f'Game over!')
					return
				for shot in shots:
					if asteroid.collision(shot):
						shot.kill()
						asteroid.split()
		
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
