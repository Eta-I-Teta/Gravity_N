from engine.classes import *
from engine.utilities import *
import json

with open("data/config/standart_planet_system.json", "r", encoding="utf-8") as f:
    standart_planet_system = json.load(f)

planet_configuration =[]
for i in standart_planet_system:
    print(standart_planet_system[i])
    planet_configuration.append(standart_planet_system[i])

print()
print(standart_planet_system)
print(planet_configuration)
print(list_to_json(planet_configuration))
print(list_to_json(planet_configuration) == standart_planet_system)