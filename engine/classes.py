import json
import pygame
from engine.utilities import *
from collections import deque
from engine.GUI import *

with open("data/config/display.json", "r", encoding="utf-8") as f:
    config_display = json.load(f)
with open("data/config/consts.json", "r", encoding="utf-8") as f:
    config_consts = json.load(f)
with open("data/config/backend_settings.json", "r", encoding="utf-8") as f:
    config_backend_settings = json.load(f)

class SpaceObject:
    def __init__(self, name: any = None, mass: float = None, coordinates: list = None, radius: float = None, speed: list = None, acceleration: list = None, color = None, config = config_display["render"]):
        self.name = name
        self.mass = 1e3 if ( mass == None ) else mass
        self.coordinates = [0, 0] if ( coordinates == None ) else coordinates
        self.radius = 1 if ( radius == None ) else radius
        self.speed = [0, 0] if ( speed == None ) else speed
        self.acceleration = [0, 0] if ( acceleration == None ) else acceleration
        self.color = (255, 255, 255) if ( color == None ) else color
        self.trace = deque(maxlen = config["trace_lenght"])
        
        pass

def get_coordinates_for_screen(coordinates: list, scale, camera_shift, center_coordinates, config = config_display["render"]):
    screen_x = ( ( coordinates[0] - center_coordinates[0] ) / scale ) + ( config["size"]["width"] / 2 ) + camera_shift[0]
    screen_y = ( ( coordinates[1] - center_coordinates[1] ) / scale ) + ( config["size"]["height"] / 2 ) + camera_shift[1]

    return [screen_x, screen_y]

def draw_planet(obj: SpaceObject, screen, center_coordinates: list, camera_shift: list, scale: float, config = config_display["render"]):
    """
    Args:
        obj (SpaceObject): the object to be drawn
        screen: the screen where the SpaceObject will be drawn
        center_coordinates (list): a pair of coordinates that should be in the center of the screen
        camera_shift (list): offset of the camera relative to the center
        config (json): configuration file

    Do:
        renders the object according to the arguments
    """
    center_coordinates = [0, 0] if ( center_coordinates == None ) else center_coordinates

    coordinates_for_screen = get_coordinates_for_screen(obj.coordinates, scale, camera_shift, center_coordinates)

    radius_for_screen = obj.radius / scale

    pygame.draw.circle(screen, obj.color, coordinates_for_screen, radius_for_screen)

def draw_trace(obj: list, screen, center_coordinates: list, camera_shift: list, scale: float, config = config_display["render"]):
    """
    Args:
        obj (list): list of coordinate pairs of trace to be drawn
        screen: the screen where the SpaceObject will be drawn
        center_coordinates (list): a pair of coordinates that should be in the center of the screen
        camera_shift (list): offset of the camera relative to the center
        config (json): configuration file

    Do:
        renders the object according to the arguments
    """
    center_coordinates = [0, 0] if ( center_coordinates == None ) else center_coordinates

    for dots_coordinates in obj:
        coordinates_for_screen = get_coordinates_for_screen(dots_coordinates, scale, camera_shift, center_coordinates)

        pygame.draw.circle(screen, config["trace_color"], coordinates_for_screen, config["trace_size"])

def draw_planet_info(obj: SpaceObject, screen, font, scale, camera_shift, center_coordinates, config = config_display["render"]):
    MultilineText(
        f"Name: {obj.name} \n" \
        f"Position: {get_beautiful_number(obj.coordinates[0])}, {get_beautiful_number(obj.coordinates[1])} \n" \
        f"Speed: {get_beautiful_number(obj.speed[0])}, {get_beautiful_number(obj.speed[1])}",
        font
    ).draw(screen, get_coordinates_for_screen(obj.coordinates, scale, camera_shift, center_coordinates)[0], get_coordinates_for_screen(obj.coordinates, scale, camera_shift, center_coordinates)[1], 300)

class OuterSpace:
    def __init__(self, planets: deque = None, center_mass: list = None):
        self.planets = deque() if ( planets == None ) else planets
    
    # Метод Эйлера

    def acceleration_calculation_Euler(self, config: json = config_consts):
        G = config["G"]

        for modified_object in self.planets:
            acceleration_data = []

            for cursor_object in self.planets:
                if modified_object != cursor_object:
                    
                    direction = [cursor_object.coordinates[0] - modified_object.coordinates[0], cursor_object.coordinates[1] - modified_object.coordinates[1]]
                    direction = normalize_vector(direction)

                    value = G * cursor_object.mass / not_zero( distance(modified_object.coordinates, cursor_object.coordinates) ** 2 )

                    acceleration_data.append(product_vector_scalar(value, direction))
            
            modified_object.acceleration = averaging_vector(acceleration_data)
    
    def speed_calculation_Euler(self, time_speed: float = 1, config: json = config_display["render"]):
        for modified_object in self.planets:

            modified_object.speed[0] += modified_object.acceleration[0] * config["frequency_updating"] * time_speed
            modified_object.speed[1] += modified_object.acceleration[1] * config["frequency_updating"] * time_speed
    
    def coordinates_calculation_Euler(self, time_speed: float = 1, config: json = config_display["render"]):
        for modified_object in self.planets:

            modified_object.coordinates[0] += modified_object.speed[0] * config["frequency_updating"] * time_speed
            modified_object.coordinates[1] += modified_object.speed[1] * config["frequency_updating"] * time_speed

    def planets_move_calculation_Euler(self, time_speed: float, config: json = config_display["render"]):
        self.acceleration_calculation_Euler()
        self.speed_calculation_Euler(time_speed = time_speed)
        self.coordinates_calculation_Euler(time_speed = time_speed)


    def trace_calculation(self):
        for planet in self.planets:
            planet.trace.append(list(planet.coordinates))

    def get_coordinates_center_mass(self) -> list:
        coordinates_center_mass = [0, 0]
        total_mass = 0

        for i in self.planets:
            coordinates_center_mass[0] += i.coordinates[0] * i.mass
            coordinates_center_mass[1] += i.coordinates[1] * i.mass
            total_mass += i.mass
        
        coordinates_center_mass[0] /= not_zero(total_mass)
        coordinates_center_mass[1] /= not_zero(total_mass)

        return coordinates_center_mass

    def set_planet_system_configuration(self, file_name: str, config_attributes: list = config_backend_settings["SpaceObject_attributes"]):

        with open(file_name, "r", encoding="utf-8") as f:
            config = json.load(f)
        
        planet_system = deque()

        for index in range(len(config)):
            planet_system.append( SpaceObject() )
            for attribute in config_attributes:
                if hasattr(planet_system[index], attribute):
                    setattr(planet_system[index], attribute, config[str(index)][attribute])
                else:
                    raise AttributeError("The config file contains unsupported attributes")
        
        self.planets = planet_system
    
    def get_normalized_scale(self, center_coordinates: list, config: json = config_display["render"]):

        most_remote_planet = self.get_most_remote_planet(center_coordinates)

        return max(abs(center_coordinates[0] - most_remote_planet.coordinates[0]) * 2 / (config["size"]["width"] * config_display["render"]["normal_scale_multiplier"]), 
                   abs(center_coordinates[1] - most_remote_planet.coordinates[1]) * 2 / (config["size"]["height"] * config_display["render"]["normal_scale_multiplier"]))

    def get_most_remote_planet(self, center_coordinates) -> SpaceObject:
        max_distance = 0
        most_remote_planet = self.planets[0]

        for planet in self.planets:
            if distance(center_coordinates, planet.coordinates) > max_distance:
                max_distance = distance(center_coordinates, planet.coordinates)
                most_remote_planet = planet
        
        return most_remote_planet