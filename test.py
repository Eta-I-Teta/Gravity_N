from engine.classes import *
from engine.utilities import *
import json
import pygame
import time

pygame.init()

# Screen settings

screen_width = config_display["render"]["size"]["width"]
screen_height = config_display["render"]["size"]["height"]

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(" системы")
pygame.display.set_icon(pygame.image.load('data/images/render_icon.png'))

font = pygame.font.SysFont(config_display["render"]["font_family"], config_display["render"]["font_size"])

# Program processes

while True:

    # Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    # Drawing

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, [255, 255, 255], (0, 0, 3, 3))
    text = font.render("abc", True, (0, 0, 0))
    screen.blit(text, (100, 100))
    
    pygame.display.flip()

pygame.quit()