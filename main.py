import pygame
import sys

from settings import SIZE
from game_objects import Player, Background


pygame.init()
pygame.display.set_caption("Surprise, mutherfucker!")

screen = pygame.display.set_mode(SIZE)
running = True

#Game objects
player = Player()
background = Background()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background.image, background.rect)
    screen.blit(player.image, player.rect)

    player.update()
    background.update()

    pygame.display.flip()

    pygame.time.delay(60)

pygame.quit()
sys.exit(0)
