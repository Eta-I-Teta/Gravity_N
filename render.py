from engine.classes import *
from engine.utilities import *
from engine.GUI import *
import json
import pygame

pygame.init()

with open("data/config/display.json", "r", encoding="utf-8") as f:
    config_display = json.load(f)
with open("data/config/help_info.json", "r", encoding="utf-8") as f:
    config_help_info = json.load(f)

# Screen settings

screen_width = config_display["render"]["size"]["width"]
screen_height = config_display["render"]["size"]["height"]

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Модель космической системы")
pygame.display.set_icon(pygame.image.load('data/images/render_icon.png'))

# Configurate and other settings

space = OuterSpace()
space.set_planet_system_configuration("data/config/standart_planet_system.json")

total_time = 0
time_speed = 1
min_time_speed = config_display["render"]["min_time_speed"]
max_time_speed = config_display["render"]["max_time_speed"]
time_multiplicity = config_display["render"]["time_multiplicity"]

coordinates_frame_reference = [0, 0]
camera_anchor = -2

camera_shift = [0, 0]
camera_movement_speed = config_display["render"]["camera_movement_speed"]
camera_scale = space.get_normalized_scale(coordinates_frame_reference)
camera_scale_multiplier = config_display["render"]["scale_multiplier"]

font = pygame.font.SysFont(config_GUI["font_family"], config_GUI["font_size"])

paused = False
show_info = False
show_help = False
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
                paused = not paused

            if (event.key == pygame.K_i):
                show_info = not show_info
            
            if (event.key == pygame.K_ESCAPE):
                show_help = not show_help

            if (event.key == pygame.K_UP) and (time_speed < max_time_speed):
                time_speed *= time_multiplicity
            if (event.key == pygame.K_DOWN) and (time_speed > min_time_speed):
                time_speed /= time_multiplicity

            if (event.key == pygame.K_RIGHT):
                if camera_anchor == len(space.planets) - 1:
                    camera_anchor = -2
                else:
                    camera_anchor += 1
            if (event.key == pygame.K_LEFT):
                if camera_anchor == -2:
                    camera_anchor = len(space.planets) - 1
                else:
                    camera_anchor -= 1

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

        space.planets_move_calculation_Euler(time_speed = time_speed)
        if trace_rendering:
            space.trace_calculation()
        total_time += time_speed * config_display["render"]["frequency_updating"]
        
    # Drawing

    screen.fill((0, 0, 0))

    if camera_anchor == -2:
        coordinates_frame_reference = [0, 0]
        anchor_name = "начало координат"
    elif camera_anchor == -1:
        coordinates_frame_reference = space.get_coordinates_center_mass()
        anchor_name = "центр масс"
    else:
        coordinates_frame_reference = space.planets[camera_anchor].coordinates
        anchor_name = space.planets[camera_anchor].name

    for planet in space.planets:
        draw_planet(planet, screen, center_coordinates = coordinates_frame_reference, camera_shift = camera_shift, scale = camera_scale)
        if trace_rendering:
            draw_trace(planet.trace, screen, center_coordinates = coordinates_frame_reference, camera_shift = camera_shift, scale = camera_scale)
        if show_info:
            draw_planet_info(planet, screen, font, scale=camera_scale, camera_shift=camera_shift, center_coordinates = coordinates_frame_reference)

    MultilineText(
        f"Времени прошло: {time_converter(total_time)} \n" \
        f"Скорость времени: {get_beautiful_number(time_speed)}x \n" \
        f"Отслеживаемый объект: {anchor_name}",
        font
        ).draw(screen, 0, 0, 475)

    if show_help:
        MultilineText(
            "\n".join(config_help_info["text"]), 
            font
        ).draw(
            screen, 
            (config_display["render"]["size"]["width"] - config_help_info["width"]) / 2, 
            50, 
            config_help_info["width"]
        )
        

    #time.sleep(config_display["render"]["frequency_updating"])
    pygame.time.Clock().tick(config_display["render"]["FPS"])
    
    pygame.display.flip()

pygame.quit()