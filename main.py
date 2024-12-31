import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    gameClock = pygame.time.Clock()
    playerShip = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        playerShip.draw(screen)
        playerShip.update(dt)
        pygame.display.flip()
        dt = gameClock.tick(60)/1000

    pygame.quit()

if __name__ == "__main__":
    main()