from engine.classes import *
from engine.defs import *
import json

if __name__ == "__main__":
    #argparse
    

    #demo
    pass

earth = SpaceObject(name="EARTH", radius=5e6, color=(100, 255, 100), coordinates=[0, 0], mass=6e24)
moon = SpaceObject(name="MOON", radius=5e6, color=(255, 255, 255), coordinates=[200e6, 0], mass=7e22, speed=[0, 1.2])
space = [earth,moon]

screen_coordinates = get_coordinates_center_mass(space)
print(screen_coordinates)