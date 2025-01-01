import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet

def main():
    #Initialise Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    gameClock = pygame.time.Clock()

    #Sprite Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    #Containers for the sprite classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Bullet.containers = (bullets, updatable, drawable)

    playerShip = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()


    #Game Loop
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(playerShip):
                print("Collision Detected: Game Over")
                return
            for bullet in bullets:
                if  bullet.collision(asteroid):
                    asteroid.split()
                    bullet.kill()
        
        screen.fill(BLACK)
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #Limit the frame rate to 60 fps
        dt = gameClock.tick(60)/1000


if __name__ == "__main__":
    main()