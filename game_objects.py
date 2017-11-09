import pygame

from settings import HEIGHT, WIDTH


class Player(pygame.sprite.Sprite):
    speed = 10
    jump_height = 100
    jump_speed = -13

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

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.current_jump_speed == 0:
                self.current_image = self.current_image + 1 if self.current_image < 7 else 0
            self.current_speed = -self.speed
            self.image = self.manback_images[self.current_image]
            Background.change_direction(Background, "left")
        elif keys[pygame.K_RIGHT]:
            if self.current_jump_speed == 0:
                self.current_image = self.current_image + 1 if self.current_image < 7 else 0
            self.current_speed = self.speed
            self.image = self.man_images[self.current_image]
            Background.change_direction(Background, "right")
        else:
            self.current_speed = 0

        if keys[pygame.K_UP] and self.rect.bottom == HEIGHT - 20:
            if self.rect.bottom > HEIGHT - self.jump_height:
                self.current_jump_speed = self.jump_speed
            else:
                self.current_jump_speed = 0
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


class Background(pygame.sprite.Sprite):
    speed = 10
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
