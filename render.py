from engine.classes import SpaceObject
from engine.defs import *
import json
import pygame
import time
import random

with open("data/config/display.json", "r", encoding="utf-8") as f:
    config_display = json.load(f)

pygame.init()

screen = pygame.display.set_mode((config_display["size"]["width"], config_display["size"]["height"]))

earth = SpaceObject(name="EARTH", radius=5e6, color=(100, 255, 100), coordinates=[300e6, 300e6], mass=6e24)
moon = SpaceObject(name="MOON", radius=5e6, color=(255, 255, 255), coordinates=[300e6 +200e6, 300e6], mass=7e22, speed=[0, 1.2])
space = [earth,moon]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))
    
    acceleration_calculation(space)
    speed_calculation(space)
    coordinates_calculation(space)

    for i in space:
        i.draw(screen)
    
    
    pygame.display.flip()
    time.sleep(config_display["frequency_updating"])

pygame.quit()