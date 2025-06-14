from engine.classes import *
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

space = OuterSpace()
space.set_planet_system_configuration("standart_planet_system.json")

time_speed = 1
min_time_speed = config_display["render"]["min_time_speed"]
max_time_speed = config_display["render"]["max_time_speed"]
time_multiplicity = config_display["render"]["time_multiplicity"]

coordinates_frame_reference = space.get_coordinates_center_mass()

camera_shift = [0, 0]
camera_movement_speed = config_display["render"]["camera_movement_speed"]
camera_scale = space.get_normalized_scale(coordinates_frame_reference)
camera_scale_multiplier = config_display["render"]["scale_multiplier"]

font = pygame.font.Font(config_display["render"]["font_family"], config_display["render"]["font_size"])

paused = False
show_info = True
trace_rendering = True
trace_lenght = config_display["render"]["trace_lenght"]

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

            if (event.key == pygame.K_t):
                if trace_rendering:
                    trace_rendering = False
                    for planet in space.planets:
                        planet.trace.clear()
                else:
                    trace_rendering = True

            if (event.key == pygame.K_SPACE):
                if paused:
                    paused = False
                else:
                    paused = True

            if (event.key == pygame.K_i):
                if show_info:
                    show_info = False
                else:
                    show_info = True

            if (event.key == pygame.K_UP) and (time_speed < max_time_speed):
                time_speed *= time_multiplicity
            if (event.key == pygame.K_DOWN) and (time_speed > min_time_speed):
                time_speed /= time_multiplicity

        # Wheel scrolling processing

        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                camera_scale /= camera_scale_multiplier
            else:
                camera_scale *= camera_scale_multiplier
        
        # Processing mouse keystrokes

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:  # 1 - левая, 2 - средняя, 3 - правая
                camera_scale = space.get_normalized_scale(coordinates_frame_reference)
        
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
    
    if not paused:

        # Calculation

        space.acceleration_calculation()
        space.speed_calculation(time_speed = time_speed)
        space.coordinates_calculation(time_speed = time_speed)
        if trace_rendering:
            space.trace_calculation()
        
    # Drawing

    screen.fill((0, 0, 0))

    coordinates_frame_reference = space.get_coordinates_center_mass()

    for planet in space.planets:
        draw_planet(planet, screen, center_coordinates = coordinates_frame_reference, camera_shift = camera_shift, scale = camera_scale)
        if trace_rendering:
            draw_trace(planet.trace, screen, center_coordinates = coordinates_frame_reference, camera_shift = camera_shift, scale = camera_scale)
        if show_info:
            draw_info(planet, screen, font, scale=camera_scale, camera_shift=camera_shift, center_coordinates=coordinates_frame_reference)

    time.sleep(config_display["render"]["frequency_updating"])
    pygame.time.Clock().tick(config_display["render"]["FPS"])
    
    pygame.display.flip()

pygame.quit()