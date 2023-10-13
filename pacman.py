from pygame import *
from random import randint
from time import time as timer


class GameSprite(sprite.Sprite):
    def __init__(self, x, y, speed, img):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(img), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):    
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 0:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.y > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.y < 0:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def update(self):
        self.direction = 'up'
        if self.rect.y >= 25:
            self.direction == 'down'
        if self.rect.y <= 925:
            self.direction == 'up'

        if self.direction == 'down':
            self.rect.y += self.speed
        if self.direction == 'up':
            self.rect.y -= self.speed

        
    def update2(self):
        self.direction = 'right'
        if self.rect.x >= 25:
            self.direction == 'right'
        if self.rect.x <= 1375:
            self.direction == 'left'

        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, widht, height, wallx, wally, color1, color2, color3):
        super().__init__()
        self.width = widht
        self.height = height
        self.image = Surface([self.width, self.height])
        self.image.fill([color1, color2, color3])
        self.rect = self.image.get_rect()
        self.rect.x = wallx
        self.rect.y = wally

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Cherry(sprite.Sprite):
    def __init__(self, cherx, chery, img):
        super().__init__()
        self.rect = self.image.get_rect()
        self.image = transform.scale(image.load(img), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = cherx
        self.rect.y = chery
    
font.init()
font = font.SysFont('Arial', 35)

lose = font.render('Ты проиграл(((', True, (255, 0, 0))
pobeda = font.render('Ты победил!!!', True, (0, 255, 0))

running = True
finish = False

window_size = (1400, 1000)
FPS = 60
clock = time.Clock()

window = display.set_mode(window_size)
display.set_caption('POCMAN')

player = Player(700, 500, 3, '')

ghost1 = Enemy(500, 500, 5, '')
ghost2 = Enemy(500, 500, 5, '')
ghost3 = Enemy(500, 500, 5, '')
ghost4 = Enemy(500, 500, 5, '')

w1 = Wall(200, 50, 500, 500, 0, 0, 255)
w2 = Wall(200, 50, 500, 500, 0, 0, 255)
w3 = Wall(200, 50, 500, 500, 0, 0, 255)
w4 = Wall(200, 50, 500, 500, 0, 0, 255)
w5 = Wall(50, 200, 500, 500, 0, 0, 255)
w6 = Wall(50, 200, 500, 500, 0, 0, 255)
w7 = Wall(50, 200, 500, 500, 0, 0, 255)
w8 = Wall(50, 200, 500, 500, 0, 0, 255)

cher1 = Cherry(500, 500, '')
cher2 = Cherry(500, 500, '')
cher3 = Cherry(500, 500, '')
cher4 = Cherry(500, 500, '')

timerr = 30
schet = 0

cherrytimer = False

ghosts = sprite.Group()
ghosts.add(ghost1)
ghosts.add(ghost2)
ghosts.add(ghost3)
ghosts.add(ghost4)

while running:
    for e in event.get():
        if e.tipe == QUIT:
            running = False

    while finish != True:
        window.blit(background, (0, 0))
        player.update()

        ghost1.update()
        ghost2.update()
        ghost3.update2()
        ghost4.update2()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()


        if sprite.collide_rect(player, ghost1) or sprite.collide_rect(player, ghost2) or sprite.collide_rect(player, ghost3) or sprite.collide_rect(player, ghost4):
            finish = True
            window.blit(lose, (350, 250))

        if sprite.collide_rect(player, cher1) or sprite.collide_rect(player, cher2) or sprite.collide_rect(player, cher3) or sprite.collide_rect(player, cher4):
            cherrytimer = True
            time1 = timer()

        if cherrytimer == True:
            time2 = timer()
            if time2 - time1 < 30:
                if sprite.collide_rect(player, ghost1) or sprite.collide_rect(player, ghost2) or sprite.collide_rect(player, ghost3) or sprite.collide_rect(player, ghost4):
                    schet += 1

            else:
                cherrytimer = False

        player.reset()

        ghost1.reset()
        ghost2.reset()
        ghost3.reset()
        ghost4.reset()

        w1.reset()
        w2.reset()
        w3.reset()
        w4.reset()
        w5.reset()
        w6.reset()
        w7.reset()
        w8.reset()

        cher1.reset()
        cher2.reset()
        cher3.reset()
        cher4.reset()

    display.update()
    clock.tick(FPS)
