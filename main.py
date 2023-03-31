from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        b = key.get_pressed()
        if b[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if b[K_DOWN] and self.rect.y < 445:
            self.rect.y += self.speed
        if b[K_RIGHT] and self.rect.x < 645:
            self.rect.x += self.speed
        if b[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed