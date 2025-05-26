from engine.classes import SpaceObject
import json
import pygame

with open("data/config/consts.json", "r", encoding="utf-8") as f:
    config_consts = json.load(f)
with open("data/config/display.json", "r", encoding="utf-8") as f:
    config_display = json.load(f)
with open("data/config/backend_settings.json", "r", encoding="utf-8") as f:
    config_backend_settings = json.load(f)

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

def product_vector_scalar(scalar: float, vector: list) -> list:
    """
    Args:
        scalar (float): the number by which the vector will be multiplied
        vector (list): the multiplying vector

    Returns:
        the result of the product of a vector by a scalar
    """
    if ( (not (type(scalar) is int) ) and (not (type(scalar) is float))) or ( not (type(vector) is list) ):
        raise TypeError("Uncorrected type of input data")
    
    for check_for_errors in vector:
        if ( (not (type(check_for_errors) is int) ) and (not (type(check_for_errors) is float))):
            raise TypeError("The vector contains invalid values")
    


    output_vector = []

    for x in vector:
        output_vector.append(x * scalar)
    
    return output_vector

def normalize_vector(vector: list) -> list:
    """
    Args:
        vector (list): the vector that will be normalized

    Returns:
        normalized vector: list
    """
    if ( not (type(vector) is list) ):
        raise TypeError("Uncorrected type of input data (vector)")
    error_number_zero_coordinates = 0

    for check_for_errors in vector:
        if check_for_errors == 0:
            error_number_zero_coordinates += 1
        if ( (not (type(check_for_errors) is int) ) and (not (type(check_for_errors) is float))):
            raise TypeError("The vector contains invalid values")
        
    if error_number_zero_coordinates == len(vector):
        raise ZeroDivisionError("The zero vector cannot be normalized")
    
    if len(vector) == 0:
        return [0, 0]



    k = 0
    for i in vector:
        k += i ** 2
    if k != 0:
        k = 1 / (k ** 0.5)
    else:
        k = 1
    
    return product_vector_scalar(k, vector)

def averaging_vector(data: list) -> list:
    """
    Args:
        data (list): a list with vectors of the same dimension that need to be averaged
    Returns:
        the average vector
    """
    if not(type(data) is list):
        raise TypeError("Uncorrected type of input data")
    
    if len(data) == 0:
        return [0, 0]

    for check_for_errors in data:
        if len(check_for_errors) != len(data[0]):
            raise ValueError("The input vectors have different dimensions")
        for component in check_for_errors:
            if ( not(type(component) is int) ) and ( not(type(component) is float) ):
                raise TypeError("Vectors contain an invalid data format")

    
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

def speed_calculation(space: list, time_speed: float = 1, config: json = config_display["render"]):
    for modified_object in space:

        modified_object.speed[0] += modified_object.acceleration[0] * config["frequency_updating"] * time_speed
        modified_object.speed[1] += modified_object.acceleration[1] * config["frequency_updating"] * time_speed

def coordinates_calculation(space: list, time_speed: float = 1, config: json = config_display["render"]):
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

def draw(obj: SpaceObject, screen, center_coordinates: list, camera_shift: list, config: json = config_display["render"]):
    """
    Args:
        obj: the object to be drawn (MUST HAVE A COORDINATES ATTRIBUTE)
        screen: the screen where the SpaceObject will be drawn
        center_coordinates (list): a pair of coordinates that should be in the center of the screen
        camera_shift (list): offset of the camera relative to the center
        config (json): configuration file

    Do:
        renders the object according to the arguments
    """
    center_coordinates = [0, 0] if ( center_coordinates == None ) else center_coordinates

    x_coordinates_for_screen = ( ( obj.coordinates[0] - center_coordinates[0] ) / config["scale"] ) + ( config["size"]["width"] / 2 ) + camera_shift[0]
    y_coordinates_for_screen = ( ( obj.coordinates[1] - center_coordinates[1] ) / config["scale"] ) + ( config["size"]["height"] / 2 ) + camera_shift[1]

    radius = obj.radius / config["scale"] * config["planet_radius_multiplier"]

    pygame.draw.circle(screen, obj.color, [x_coordinates_for_screen, y_coordinates_for_screen], radius)