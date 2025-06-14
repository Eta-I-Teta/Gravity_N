import pygame
import json
import subprocess
from engine.classes import *

pygame.init()

with open("data/config/display.json", "r", encoding="utf-8") as f:
    config_display = json.load(f)

# Screen settings

screen_width = config_display["main"]["size"]["width"]
screen_height = config_display["main"]["size"]["height"]

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Задача начальной концигурации")
pygame.display.set_icon(pygame.image.load('data/images/main_icon.png'))

font = pygame.font.SysFont(config_display["main"]["font_family"], config_display["main"]["font_size"])

planet_system_config = OuterSpace().set_planet_system_configuration("data/config/standart_planet_system.json")



while True:

    # Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    #subprocess.run(["python", "render.py"])

    # Drawing

    screen.fill((0, 0, 0))
    

    pygame.display.flip()

    pygame.time.Clock().tick(config_display["main"]["FPS"])

pygame.quit()