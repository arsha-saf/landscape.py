

import pygame
import math


pygame.init()


window_size = (800, 600)
screen = pygame.display.set_mode(window_size)


sky_blue = (135, 206, 235)
sky_black = (0, 0, 0)
grass_green = (34, 170, 34)
sun_yellow = (255, 255, 0)
sun_white = (255, 255, 255)


sun_x = -100
sun_y = 50
sun_size = 100


time_of_day = 0.0


clock = pygame.time.Clock()


while True:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

   
    time_of_day += 0.01
    if time_of_day > 2.0:
        time_of_day = 0.0

    
    if time_of_day < 1.0:
        screen.fill(sky_blue)
    else:
        screen.fill(sky_black)

    angle = time_of_day * math.pi * 2
    sun_x = math.cos(angle) * 375 + 400
    sun_y = math.sin(angle) * 300 + 250
    sun_color = sun_yellow if time_of_day < 1.0 else sun_white
    pygame.draw.circle(screen, sun_color, (int(sun_x), int(sun_y)), sun_size // 2)

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    points = [(400, 100), (300, 250), (500, 250)]
    pygame.draw.polygon(screen, RED, points)


    knob_pos = (380, 335)
    knob_size = (17, 17)
    knob_color = (255, 255, 0)
    door_pos = (375, 300)
    door_size = (50, 100)
    door_color = (100, 40, 0)
    leaf_pos = (75, 200)
    leaf_size = (100, 100)
    leaf_color =(34, 139, 34)
    tree_pos = (100,300)
    tree_size = (50, 100)
    tree_color = (0, 100, 0)
    house_pos = (300, 250)
    house_size = (200, 200)
    house_color = (255, 0, 0)
    tree1_pos = (650,300)
    tree1_size = (50, 100)
    tree1_color = (0, 100, 0)
    leaf1_pos = (622, 200)
    leaf1_size = (100, 100)
    leaf1_color =(34, 139, 34)
    pygame.draw.rect(screen, house_color, pygame.Rect(house_pos, house_size))
    pygame.draw.polygon(screen, grass_green, [(0, 400), (800, 400), (800, 600), (0, 600)])
    pygame.draw.rect(screen, tree_color, pygame.Rect(tree_pos, tree_size))
    pygame.draw.rect(screen, leaf_color, pygame.Rect(leaf_pos, leaf_size))
    pygame.draw.rect(screen, door_color, pygame.Rect(door_pos, door_size))
    pygame.draw.rect(screen, knob_color, pygame.Rect(knob_pos, knob_size))
    pygame.draw.rect(screen, tree1_color, pygame.Rect(tree1_pos, tree1_size))
    pygame.draw.rect(screen, leaf1_color, pygame.Rect(leaf1_pos, leaf1_size))
    # pygame.draw.rect(screen, window_color, pygame.Rect(window_pos, window_size))
    pygame.display.flip()


    clock.tick(60)