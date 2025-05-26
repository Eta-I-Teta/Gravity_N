import json
import pygame
from engine.utilities import *
from collections import deque

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

def distance(obj_1: SpaceObject, obj_2: SpaceObject) -> float:
    """
    Args:
        obj_1 (SpaceObject): first object, between which the distance will be calculated
        obj_2 (SpaceObject): second object, between which the distance will be calculated

    Returns:
        distance between objects
    """
    if ( not (type(obj_1) is SpaceObject) ) or ( not (type(obj_2) is SpaceObject) ):
        raise TypeError("Arguments of the SpaceObject type are expected")
    
    if ( not hasattr(obj_1, "coordinates") ) or ( not hasattr(obj_2, "coordinates") ):
        raise KeyError("The coordinates attribute was not found for the objects")
    
    if (
        ( ( len(obj_1.coordinates) != 2 ) or ( len(obj_2.coordinates) != 2 ) ) or
        ( (not (type(obj_1.coordinates[0]) is float)) and (not (type(obj_1.coordinates[0]) is int)) ) or
        ( (not (type(obj_1.coordinates[1]) is float)) and (not (type(obj_1.coordinates[1]) is int)) ) or
        ( (not (type(obj_2.coordinates[0]) is float)) and (not (type(obj_2.coordinates[0]) is int)) ) or
        ( (not (type(obj_2.coordinates[1]) is float)) and (not (type(obj_2.coordinates[1]) is int)) )
    ):
        raise ValueError("Incorrect coordinate value")



    return ((obj_1.coordinates[0] - obj_2.coordinates[0]) ** 2 + (obj_1.coordinates[1] - obj_2.coordinates[1]) ** 2) ** 0.5

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

    x_coordinates_for_screen = ( ( obj.coordinates[0] - center_coordinates[0] ) / scale ) + ( config["size"]["width"] / 2 ) + camera_shift[0]
    y_coordinates_for_screen = ( ( obj.coordinates[1] - center_coordinates[1] ) / scale ) + ( config["size"]["height"] / 2 ) + camera_shift[1]

    radius_for_screen = obj.radius / scale * config["planet_radius_multiplier"]

    pygame.draw.circle(screen, obj.color, [x_coordinates_for_screen, y_coordinates_for_screen], radius_for_screen)

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
        x_coordinates_for_screen = ( ( dots_coordinates[0] - center_coordinates[0] ) / scale ) + ( config["size"]["width"] / 2 ) + camera_shift[0]
        y_coordinates_for_screen = ( ( dots_coordinates[1] - center_coordinates[1] ) / scale ) + ( config["size"]["height"] / 2 ) + camera_shift[1]

        pygame.draw.circle(screen, config["trace_color"], [x_coordinates_for_screen, y_coordinates_for_screen], config["trace_size"])

class OuterSpace:
    def __init__(self, planets: list = None):
        self.planets = [] if ( planets == None ) else planets
    
    def acceleration_calculation(self, config: json = config_consts):
        G = config["G"]

        for modified_object in self.planets:
            acceleration_data = []

            for cursor_object in self.planets:
                if modified_object != cursor_object:
                    
                    direction = [cursor_object.coordinates[0] - modified_object.coordinates[0], cursor_object.coordinates[1] - modified_object.coordinates[1]]
                    direction = normalize_vector(direction)

                    value = G * cursor_object.mass / ( distance(modified_object, cursor_object) ** 2 )

                    acceleration_data.append(product_vector_scalar(value, direction))
            
            modified_object.acceleration = averaging_vector(acceleration_data)
    
    def speed_calculation(self, time_speed: float = 1, config: json = config_display["render"]):
        for modified_object in self.planets:

            modified_object.speed[0] += modified_object.acceleration[0] * config["frequency_updating"] * time_speed
            modified_object.speed[1] += modified_object.acceleration[1] * config["frequency_updating"] * time_speed
    
    def coordinates_calculation(self, time_speed: float = 1, config: json = config_display["render"]):
        for modified_object in self.planets:

            modified_object.coordinates[0] += modified_object.speed[0] * config["frequency_updating"] * time_speed
            modified_object.coordinates[1] += modified_object.speed[1] * config["frequency_updating"] * time_speed
    
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
        
        coordinates_center_mass[0] /= total_mass
        coordinates_center_mass[1] /= total_mass

        return coordinates_center_mass

    def set_planet_system_configuration(self, file_name: str, config_attributes: list = config_backend_settings["SpaceObject_attributes"]):

        with open("data/config/" + file_name, "r", encoding="utf-8") as f:
            config = json.load(f)
        
        planet_system = []

        for index in range(len(config)):
            planet_system.append( SpaceObject() )
            for attribute in config_attributes:
                if hasattr(planet_system[index], attribute):
                    setattr(planet_system[index], attribute, config[str(index)][attribute])
                else:
                    raise AttributeError("The config file contains unsupported attributes")
        
        self.planets = planet_system