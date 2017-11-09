import pygame
import sys

from settings import SIZE
from game_objects import Player, Background, Mob


pygame.init()
pygame.display.set_caption("Surprise, mutherfucker!")

screen = pygame.display.set_mode(SIZE)
running = True

#Game objects
player = Player()
background = Background()

#Groups of sprites
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
mobs = pygame.sprite.Group()
for i in range(4):
    mob = Mob()
    mobs.add(mob)
    all_sprites.add(mob)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                bullet = player.shoot()
                bullets.add(bullet)
                all_sprites.add(bullet)

    screen.blit(background.image, background.rect)
    screen.blit(player.image, player.rect)

    player.update()
    background.update()
    all_sprites.update()

    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        mob = Mob()
        mobs.add(mob)
        all_sprites.add(mob)

    # check to see if a bullet hit a mob
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False

    all_sprites.draw(screen)
    pygame.display.flip()

    pygame.time.delay(15)

pygame.quit()
sys.exit(0)
