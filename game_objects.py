import pygame
import random

from settings import HEIGHT, WIDTH, SPEED_PLAYER, SPEED_MAX_MOB


class Player(pygame.sprite.Sprite):
    speed = SPEED_PLAYER
    jump_height = 100
    jump_speed = -13
    direction = "left"

    def __init__(self):
        super(Player, self).__init__()
        self.man_images = []
        for i in range(1, 3):
            for j in range(1, 5):
                self.man_images.append(pygame.image.load("images/man{}{}.png".format(i, j)))
        self.manback_images = []
        for i in range(1, 3):
            for j in range(1, 5):
                self.manback_images.append(pygame.image.load("images/manback{}{}.png".format(i, j)))

        self.current_image = 0

        self.image = self.manback_images[self.current_image]
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 20

        self.current_speed = 0
        self.current_jump_speed = 0

    def shoot(self):
        if self.direction == "right":
            bullet = Bullet(self.speed + 2, self.rect.right + 2, self.rect.centery)
        else:
            bullet = Bullet(-self.speed - 2, self.rect.left - 2, self.rect.centery)
        return bullet

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.current_jump_speed == 0:
                self.current_image = self.current_image + 1 if self.current_image < 7 else 0
            self.current_speed = -self.speed
            self.image = self.manback_images[self.current_image]
            self.direction = "left"
            Background.change_direction(Background, self.direction)
        elif keys[pygame.K_RIGHT]:
            if self.current_jump_speed == 0:
                self.current_image = self.current_image + 1 if self.current_image < 7 else 0
            self.current_speed = self.speed
            self.image = self.man_images[self.current_image]
            self.direction = "right"
            Background.change_direction(Background, self.direction)
        else:
            self.current_speed = 0

        if keys[pygame.K_UP] and self.rect.bottom == HEIGHT - 20:
            self.current_jump_speed = self.jump_speed
            # if self.rect.bottom > HEIGHT - self.jump_height:
            #     self.current_jump_speed = self.jump_speed
            # else:
            #     self.current_jump_speed = 0
        elif self.rect.bottom <= HEIGHT - self.jump_height:
            self.current_jump_speed = - self.jump_speed
        elif self.rect.bottom == HEIGHT - 20:
            self.current_jump_speed = 0

        if (self.rect.left < 10 and self.current_speed < 0) or \
                        (self.rect.right + 10 > WIDTH and self.current_speed > 0):
            self.current_speed = 0
            Background.change_go(Background, True)
        else:
            Background.change_go(Background, False)

        self.rect.move_ip(self.current_speed, self.current_jump_speed)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, x, y):
        super(Bullet, self).__init__()

        self.image = pygame.image.load("images/bullet.png") if speed > 0 else pygame.image.load("images/bullet2.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        # kill if moves off the screen
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()
            

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super(Mob, self).__init__()
        self.image = pygame.Surface((5, 40))
        self.rect = self.image.get_rect()
        self.image.fill((255, 0, 0))
        side = random.randint(0, 1)
        if side == 0:
            self.rect.left = 0
            self.speed = random.randint(SPEED_MAX_MOB - 3, SPEED_MAX_MOB)
        else:
            self.rect.right = WIDTH
            self.speed = random.randint(-SPEED_MAX_MOB, -SPEED_MAX_MOB + 3)
        self.rect.bottom = random.randint(HEIGHT - 90, HEIGHT - 20)

    def update(self):
        self.rect.x += self.speed
        # kill if moves off the screen
        if self.rect.right < 0 or self.rect.left > WIDTH:
            side = random.randint(0, 1)
            if side == 0:
                self.rect.left = 0
                self.speed = random.randint(SPEED_MAX_MOB - 3, SPEED_MAX_MOB)
            else:
                self.rect.right = WIDTH
                self.speed = random.randint(-SPEED_MAX_MOB, -SPEED_MAX_MOB + 3)
            self.rect.bottom = random.randint(HEIGHT - 90, HEIGHT - 20)


class Background(pygame.sprite.Sprite):
    speed = SPEED_PLAYER
    direction = "left"
    go = False

    def __init__(self):
        super(Background, self).__init__()

        self.image = pygame.image.load("images/countryfield.png")
        self.rect = self.image.get_rect()

        self.rect.bottom = HEIGHT + 67
        self.rect.centerx = WIDTH / 2

    def update(self):
        if self.go:
            if self.direction == "left":
                if self.rect.right < self.rect.width - 10:
                    self.rect.right += self.speed
            else:
                if self.rect.left > (WIDTH - self.rect.width + 10):
                    self.rect.left -= self.speed


    def change_direction(self, direction):
        self.direction = direction

    def change_go(self, go):
        self.go = go
