from pygame import *
from random import choice

WIN_W = 900
WIN_H = 700
FPS = 60
step = 10
YELLOW = (255,255,0)
back = (200,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN = (0,255,0)
BLACK=(0,0,0)
WHITE = (255, 255, 255)

class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,w,h):
        self.image = transform.scale(
            image.load(img),
            (w,h)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self,window):
        window.blit(self.image,(self.rect.x,self.rect.y))


class sprite1(GameSprite):
    def __init__ (self,img,x,y,w,h,step=step):
        super().__init__(img,x,y,w,h)
        self.step = step
    
    def update(self, up, down):
        keys_pressed = key.get_pressed()
        if keys_pressed[up] and self.rect.y > 5:
            self.rect.y -= self.step
        if keys_pressed[down] and self.rect.y < WIN_H - 150:
            self.rect.y += self.step


class Ball(GameSprite):
    def __init__(self,img, x,y,w,h, step = 5):
        super().__init__(img,x,y,w,h)
        self.step_x = step * choice([-1, 1])
        self.step_y = step * choice([-1, 1])
    def update(self):
        if self.rect.x <= 0 or  self.rect.x >= WIN_W - self.rect.width:
            self.step_x = self.step_x * -1
        self.rect.x += self.step_x
        if self.rect.y <= 0 or  self.rect.y >= WIN_H - self.rect.height:
            self.step_y = self.step_y * -1
        self.rect.y += self.step_y

        

window = display.set_mode((WIN_W, WIN_H))
clock = time.Clock()

font.init()
title_font = font.SysFont('Times New Roman', 70)    
left_win = title_font.render('ЛЕВЫЙ ПОБЕДИЛ', True, WHITE)
right_win = title_font.render('ПРАВЫЙ ПОБЕДИЛ', True, WHITE)

display.set_caption("пинг понг")

background = transform.scale(
    image.load("background.jpg"),
    (WIN_W, WIN_H)
)

player_1 = sprite1('wall.png',0,350,50,150)
player_2 = sprite1('wall.png',850,350,50,150)

ball = Ball('ball.png', 400, 300, 100, 100)

game = True
Finish = False

while game:
    if not Finish:
        window.blit(background,(0, 0))

        player_1.draw(window) 
        player_2.draw(window)
        ball.draw(window)

        player_1.update(K_w,K_s,)
        player_2.update(K_UP,K_DOWN,)
        ball.update()

        if sprite.collide_rect(ball, player_1):
            ball.rect.x *= -1

        if sprite.collide_rect(ball, player_2):
            ball.rect.x *= -1

        if ball.rect.x <= 0:
            window.blit(right_win, (100,300))
            display.update()
            Finish = True

        if ball.rect.x >= 800:
            window.blit(left_win, (100,300))
            display.update()
            Finish = True       

    else:
        time.delay(3000)

        player_1 = sprite1('wall.png',0,350,50,150)
        player_2 = sprite1('wall.png',850,350,50,150)

        ball = Ball('ball.png', 400, 300, 100, 100)

        Finish = False

    for e in event.get():
        if e.type == QUIT:
            game = False
            
    display.update()
    clock.tick(FPS)