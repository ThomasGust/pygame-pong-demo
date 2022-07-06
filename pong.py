import sys
import random
import pygame
pygame.init()
clock = pygame.time.Clock()
sw = 1280
sh = 960
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Pong")
light_grey = (200, 200, 200)
bsx = 7
bsy = 7
ps = 0
so = 0
sp = 0
gf = pygame.font.Font(None, 25)
ball = pygame.rect.Rect(sw/2 - 15, sh/2 - 15, 30, 30)
opponent = pygame.rect.Rect(sw-20, sh/2 - 70, 20, 140)
player = pygame.rect.Rect(10, sh/2 - 70, 20, 140)
difficulty = 9
def restart_ball():
    global bsy, bsx
    ball.center = (sw/2, sh/2)
    bsy *= random.choice([1, -1])
    bsx *= random.choice([1, -1])
def animate_ball():
    global bsx, bsy, sp, so
    ball.x += bsx
    ball.y += bsy
    if ball.top <= 0 or ball.bottom >= sh:
        bsy *= -1
    if ball.left <= 0:
        so += 1
        restart_ball()
    if ball.right >= sw:
        sp += 1
        restart_ball()
    if ball.colliderect(player) or ball.colliderect(opponent):
        bsx *= -1
def animate_player():
    player.y += ps
    if player.top <= 0:
        player.top = 0
    if player.bottom >= sh:
        player.bottom= sh
def animate_opponent():
    if difficulty >= 10:
        opponent.centery = ball.centery
    else:
        if opponent.top < ball.y:
            opponent.top += difficulty
        if opponent.bottom > ball.y:
            opponent.bottom -= difficulty
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= sh:
        opponent.bottom = sh
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                ps -= 7
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                ps += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                ps -= 7
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                ps += 7
    animate_ball()
    animate_player()
    animate_opponent()
    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.aaline(screen, light_grey, (sw/2, 0), (sw/2, sh))
    pt = gf.render(f'{sp}', False, light_grey)
    ot = gf.render(f'{so}', False, light_grey)
    screen.blit(pt, ((sw//2)-20, (sh//2)))
    screen.blit(ot, ((sw//2)+20, (sh//2)))
    pygame.display.flip()
    clock.tick(60)
