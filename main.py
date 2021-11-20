import pygame
import random
from pygame.rect import *
import mouse

pygame.mixer.init()
pygame.init()
gun_reload = pygame.mixer.Sound("Gun Reload sound effect.wav")
tick_tick = pygame.mixer.Sound("Gun Dry Fire Sound Effect.wav")
gun_shoot = pygame.mixer.Sound("Realistic Gunshot Sound Effect.wav")
gameDisplay = pygame.display.set_mode((800, 400))
farm = pygame.image.load("farm.jpg")
one = pygame.image.load("1.png")
two = pygame.image.load("2.png")
three = pygame.image.load("3.png")
four = pygame.image.load("4.png")
five = pygame.image.load("5.png")
zero = pygame.image.load("0.png")
# pos = [[675, 147], [331, 145], [4, 196], [506, 57]]
count = 0
reloading = pygame.image.load("reloading.png")
chicken = pygame.image.load("chicken.png")
chicken = pygame.transform.scale(chicken, [75, 67])
chicken_rect = Rect(4, 4, 75, 67)
bullet = 5
# pos1 = random.choice(pos)
a = 0
c_x = 0
c_y = 200
point = 0
image2 = five
level = 1
run = True
sound_count = 1
x, y = pygame.mouse.get_pos()
mouse_image = pygame.image.load("aim.png")
mouse_image = pygame.transform.scale(mouse_image, [30, 30])
pygame.mouse.set_visible(False)
b = 1
Left = 1
Right = 3
while run:
    if c_x <= 0:
        b = 1
    elif c_x >= 800:
        b = 0
    if b == 1:
        c_x += 1
    if b == 0:
        c_x -= 1
    if bullet == 5:
        image2 = five
    elif bullet == 4:
        image2 = four
    elif bullet == 3:
        image2 = three
    elif bullet == 2:
        image2 = two
    elif bullet == 1:
        image2 = one
    elif bullet == 0:
        image2 = zero
    x, y = pygame.mouse.get_pos()
    mouse_rect = Rect(x, y, 15, 15)
    a += 1
    gameDisplay.blit(farm, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == Left:
            if bullet <= 0:
                tick_tick.play()
            if bullet >= 1:
                mouse.move(0, -35, absolute=False, duration=0.1)
                bullet -= 1
                gun_shoot.play()
                if chicken_rect.colliderect(mouse_rect):
                    a = 0
                    point += 1
                    print("HIT!!!!!!!!!!!")
        if event.type == pygame.QUIT:
            pygame.quit()
    if a == 1000:
        a = 0
    if point > 4:
        level = 2
    chicken_rect = Rect(c_x, c_y, 75, 67)
    gameDisplay.blit(chicken, [c_x, c_y])
    image2 = pygame.transform.scale(image2, [58, 105])
    reloading = pygame.transform.scale(reloading, [137, 22])
    gameDisplay.blit(image2, [10, 22])
    if bullet <= 0:
        count += 1
        sound_count += 1
        if sound_count == 500:
            gun_reload.play()
        if sound_count == 1000:
            gun_reload.stop()
            sound_count = 0
        gameDisplay.blit(reloading, [10, 22])
        if count == 5000:
            count = 0
            bullet = 5
    gameDisplay.blit(mouse_image, [x - 15, y - 15])
    pygame.display.update()
