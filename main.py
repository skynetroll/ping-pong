from pygame import *

from random import *

mixer.init()
mixer.music.load("")

win = display.set_mode((700,500))
display.set_caption('catch_up')

win.fill((0, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, width, height, col1, col2, col3, x, y, sp):
        super().__init__()
        self.width = width
        self.height = height
        self.col1 = col1
        self.col2 = col2
        self.col2 = col3
        self.image = Surface((self.width,self.height))
        self.image.fill((col1, col2, col3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = sp
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        b = key.get_pressed()
        if b[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if b[K_DOWN] and self.rect.y < 445:
            self.rect.y += self.speed

    def update_l(self):
        c = key.get_pressed()
        if c[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if c[K_s] and self.rect.y < 445:
            self.rect.y += self.speed

lp = Player(34, 5, 255, 255, 255, 99, 77, 10)

rp = Player(34, 5, 255, 255, 255, 645, 77, 10)

mich = 

mixer.music.play()
clock = time.Clock()
FPS = 60
game = True
finish = False
otskok = mixer.Sound('')
louse = mixer.Sound('')
while game:

    for a in event.get():
        if a.type == QUIT:
            game = False

    if finish != True:
        win.blit(background , (0,0))
        stena.draw()
        enemy.update()
        enemy.reset()
        enemy1.update()
        enemy1.reset()
        if sprite.collide_rect(rp or lp , mich):
            otskok.play()
            
        if x = 5 or 695:
            louse.play()
            finish = True

    i += 1
    display.update()
    clock.tick(FPS)
