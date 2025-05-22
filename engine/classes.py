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
    
    def draw(self, screen, config_display = config_display):
        pygame.draw.circle(screen, self.color, [self.coordinates[0] / config_display["scale"], self.coordinates[1] / config_display["scale"]], self.radius  / config_display["scale"])