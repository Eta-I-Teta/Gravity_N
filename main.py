import pygame
import time
import json
import subprocess

pygame.init()

with open("data/config/display.json", "r", encoding="utf-8") as f:
    config_display = json.load(f)

# Screen settings

screen_width = config_display["main"]["size"]["width"]
screen_height = config_display["main"]["size"]["height"]

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("main")

while True:

    # Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # Drawing

    screen.fill((0, 0, 0))

    
    pygame.display.flip()

    pygame.time.Clock().tick(config_display["main"]["FPS"])

    
    print("DO IT")
    subprocess.run(["python", "render.py"])

pygame.quit()