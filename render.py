from engine.classes import SpaceObject
from engine.utilities import *
import json
import pygame
import time

pygame.init()

with open("data/config/display.json", "r", encoding="utf-8") as f:
    config_display = json.load(f)

# Screen settings

screen_width = config_display["render"]["size"]["width"]
screen_height = config_display["render"]["size"]["height"]

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Модель космической системы")

# Configurate and other settings

space = set_space_configuration("planet_system.json")
time_speed = 5e8

camera_shift = [0, 0]
camera_movement_speed = config_display["render"]["camera_movement_speed"]

# Program processes

while True:

    # Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Handling single keystrokes

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_r):
                camera_shift = [0, 0]
        
    # Handling key retention

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_w]:
        camera_shift[1] += camera_movement_speed
    if pressed_keys[pygame.K_a]:
        camera_shift[0] += camera_movement_speed
    if pressed_keys[pygame.K_s]:
        camera_shift[1] -= camera_movement_speed
    if pressed_keys[pygame.K_d]:
        camera_shift[0] -= camera_movement_speed
    
    # Coordinates calculation

    acceleration_calculation(space)
    speed_calculation(space, time_speed = time_speed)
    coordinates_calculation(space, time_speed = time_speed)

    coordinates_frame_reference = get_coordinates_center_mass(space)
    
    # Drawing

    screen.fill((0, 0, 0))

    for i in space:
        draw(i, screen, center_coordinates = coordinates_frame_reference, camera_shift = camera_shift)
    
    pygame.display.flip()

    time.sleep(config_display["render"]["frequency_updating"])

pygame.quit()