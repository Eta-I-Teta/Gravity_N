from engine.classes import SpaceObject
import json

with open("data/config/consts.json", "r", encoding="utf-8") as f:
    config_consts = json.load(f)
with open("data/config/display.json", "r", encoding="utf-8") as f:
    config_display = json.load(f)
with open("data/config/backend_settings.json", "r", encoding="utf-8") as f:
    config_backend_settings = json.load(f)

def distance(obj_1: SpaceObject, obj_2: SpaceObject) -> float:
    return ((obj_1.coordinates[0] - obj_2.coordinates[0]) ** 2 + (obj_1.coordinates[1] - obj_2.coordinates[1]) ** 2) ** 0.5

def product_vector_scalar(scalar: float, vector: list) -> list:
    output_vector = []

    for x in vector:
        output_vector.append(x * scalar)
    
    return output_vector

def normalize_vector(vector: list) -> list:
    k = 0
    for i in vector:
        k += i ** 2
    if k != 0:
        k = 1 / (k ** 0.5)
    else:
        k = 1
    
    return product_vector_scalar(k, vector)

def averaging_vector(data: list) -> list:
    if ( len(data) == 0 ) or ( data == None ):
        return [0, 0]
    
    average_vector = []

    for coordinate in range(len(data[0])):
        tmp = 0

        for vector in range(len(data)):
            tmp += data[vector][coordinate]
        tmp /= len(data)

        average_vector.append(tmp)
    
    return average_vector

def acceleration_calculation(space: list, config: json = config_consts):
    G = config["G"]

    for modified_object in space:
        acceleration_data = []

        for cursor_object in space:
            if modified_object != cursor_object:
                
                direction = [cursor_object.coordinates[0] - modified_object.coordinates[0], cursor_object.coordinates[1] - modified_object.coordinates[1]]
                direction = normalize_vector(direction)

                value = G * cursor_object.mass / ( distance(modified_object, cursor_object) ** 2 )

                acceleration_data.append(product_vector_scalar(value, direction))
        
        modified_object.acceleration = averaging_vector(acceleration_data)

def speed_calculation(space: list, time_speed: float = 1, config: json = config_display):
    for modified_object in space:

        modified_object.speed[0] += modified_object.acceleration[0] * config["frequency_updating"] * time_speed
        modified_object.speed[1] += modified_object.acceleration[1] * config["frequency_updating"] * time_speed

def coordinates_calculation(space: list, time_speed: float = 1, config: json = config_display):
    for modified_object in space:

        modified_object.coordinates[0] += modified_object.speed[0] * config["frequency_updating"] * time_speed
        modified_object.coordinates[1] += modified_object.speed[1] * config["frequency_updating"] * time_speed

def get_coordinates_center_mass(space: list) -> list:
    coordinates_center_mass = [0, 0]
    total_mass = 0

    for i in space:
        coordinates_center_mass[0] += i.coordinates[0] * i.mass
        coordinates_center_mass[1] += i.coordinates[1] * i.mass
        total_mass += i.mass
    
    coordinates_center_mass[0] /= total_mass
    coordinates_center_mass[1] /= total_mass

    return coordinates_center_mass

def set_space_configuration(file_name: str, config_attributes: list = config_backend_settings["SpaceObject_attributes"]) -> list:

    with open("data/config/" + file_name, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    space = []

    for index in range(len(config)):
        space.append( SpaceObject() )
        for attribute in config_attributes:
            if hasattr(space[index], attribute):
                setattr(space[index], attribute, config[str(index)][attribute])
            else:
                print("ERROR")
    
    return space