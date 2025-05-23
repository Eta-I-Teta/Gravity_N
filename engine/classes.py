import pygame
import json

with open("data/config/display.json", "r", encoding="utf-8") as f:
    config_display = json.load(f)

class SpaceObject:
    def __init__(self, name: any = None, mass: float = None, coordinates: list = None, radius: float = None, speed: list = None, acceleration: list = None, color = None):
        self.name = name
        self.mass = 1e3 if ( mass == None ) else mass
        self.coordinates = [0, 0] if ( coordinates == None ) else coordinates
        self.radius = 1 if ( radius == None ) else radius
        self.speed = [0, 0] if ( speed == None ) else speed
        self.acceleration = [0, 0] if ( acceleration == None ) else acceleration
        self.color = (255, 255, 255) if ( color == None ) else color
        
        pass
    
    def draw(self, screen, center_coordinates: list = None ,config: json = config_display):
        """
        Args:
        screen - the screen where the SpaceObject will be drawn
        center_coordinates - a pair of coordinates that should be in the center of the screen
        config - configuration file

        Do:
        renders the SpaceObject according to the arguments
        """
        center_coordinates = [0, 0] if ( center_coordinates == None ) else center_coordinates

        x_coordinates_for_screen = ( ( self.coordinates[0] - center_coordinates[0] ) / config["scale"] ) + ( config["size"]["width"] / 2 )
        y_coordinates_for_screen = ( ( self.coordinates[1] - center_coordinates[1] ) / config["scale"] ) + ( config["size"]["height"] / 2 )

        radius = self.radius / config["scale"]

        pygame.draw.circle(screen, self.color, [x_coordinates_for_screen, y_coordinates_for_screen], radius)