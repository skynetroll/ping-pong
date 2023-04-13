from pygame import *

from random import *

#mixer.init()
#mixer.music.load("")

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
        self.sp = sp
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        b = key.get_pressed()
        if b[K_UP] and self.rect.y > 5:
            self.rect.y -= self.sp
        if b[K_DOWN] and self.rect.y < 445:
            self.rect.y += self.sp

    def update_l(self):
        c = key.get_pressed()
        if c[K_w] and self.rect.y > 5:
            self.rect.y -= self.sp
        if c[K_s] and self.rect.y < 445:
            self.rect.y += self.sp

class Ball(GameSprite):
    def __init__(self, width, height, col1, col2, col3, x, y, sp, sp2):
        super(). __init__(width, height, col1, col2, col3, x, y, sp)
        self.sp2 = sp2
    def update(self, lr, rp):
        self.rect.x += self.sp
        self.rect.y += self.sp2

        if sprite.collide_rect(rp , mich):
            self.sp *= -1
        if sprite.collide_rect(lp , mich):
            self.sp *= -1
        if self.rect.y <= 0 :
            self.sp2 *= -1 
        if self.rect.y >= 470 :
            self.sp2 *= -1


lp = Player(15, 100, 225, 255, 255, 99, 77, 10)

rp = Player(15, 100, 225, 255, 255, 645, 77, 10)

mich = Ball(20, 20, 255, 255, 255, 350, 250, 5, 5)


'''mixer.music.play()'''
clock = time.Clock()
FPS = 60
game = True
finish = False
'''otskok = mixer.Sound('')
louse = mixer.Sound('')'''

font = font.Font('Arial', 30)
starttext = font.render("press space to start", font,(0,0,0))
while game:

    if start = False :

    for a in event.get():
        if a.type == QUIT:
            game = False

    if finish != True:
        win.fill((0, 0, 0))
        lp.reset()
        lp.update_l()
        rp.reset()
        rp.update_r()
        mich.update(lp,rp)
        mich.reset()
 
    display.update()
    clock.tick(FPS)
