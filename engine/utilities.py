import json
import os

with open("data/config/consts.json", "r", encoding="utf-8") as f:
    config_consts = json.load(f)
with open("data/config/display.json", "r", encoding="utf-8") as f:
    config_display = json.load(f)
with open("data/config/backend_settings.json", "r", encoding="utf-8") as f:
    config_backend_settings = json.load(f)

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

def distance(obj_1: list, obj_2: list) -> float:
    """
    This function only for pair coordinates
    Args:
        obj_1 (list): first pair coordinates, between which the distance will be calculated
        obj_2 (list): second pair coordinates, between which the distance will be calculated

    Returns:
        distance between objects
    """
    
    if (
        ( ( len(obj_1) != 2 ) or ( len(obj_2) != 2 ) ) or
        ( (not (type(obj_1[0]) is float)) and (not (type(obj_1[0]) is int)) ) or
        ( (not (type(obj_1[1]) is float)) and (not (type(obj_1[1]) is int)) ) or
        ( (not (type(obj_2[0]) is float)) and (not (type(obj_2[0]) is int)) ) or
        ( (not (type(obj_2[1]) is float)) and (not (type(obj_2[1]) is int)) )
    ):
        raise ValueError("Incorrect coordinate value")

    result = max(1, ((obj_1[0] - obj_2[0]) ** 2 + (obj_1[1] - obj_2[1]) ** 2) ** 0.5)

    return result

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

def not_zero(num: int):
    if num >= 0: sgn = 1
    else: sgn = -1
    return sgn * max(1e-18, abs(num))

def time_converter(num: int) -> str:
    century = 0
    while num >= 60*60*24*365*100:
        num -= 60*60*24*365*100
        century += 1

    year = 0
    while num >= 60*60*24*365:
        num -= 60*60*24*365
        year += 1

    day = 0
    while num >= 60*60*24:
        num -= 60*60*24
        day += 1

    hour = 0
    while num >= 60*60:
        num -= 60*60
        hour += 1

    minute = 0
    while num >= 60:
        num -= 60
        minute += 1
    second = float(round(num, 3))

    return f"{century} в. {year} лет {day} д. {hour} ч. {minute} мин. {second} с."

def get_beautiful_number(num: int) -> str:
    if num == 0:
        return "0.0e0"
    elif num == abs(num):
        sgn = 1
    else:
        num = abs(num)
        sgn = -1

    k = 0
    while num < 1:
        num *= 10
        k -=1
    while round(num, 6) >= 10:
        num /= 10
        k+=1
    
    num = round(num, 6)

    return str(sgn * num) + f"e{k}"

def list_to_json(array: list) -> json:
    j = {}
    for index in range(len(array)):
        j[str(index)] = array[index]
    return j

def read_json_file(way: str) -> json:
    with open(way, "r", encoding="utf-8") as f:
        json_file = json.load(f)
    return json_file

def save_json_file(obj: json, way: str):
    with open(way, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=4, ensure_ascii=False)

# main

def json_to_list(obj: json) -> list:
    arr = []
    for i in obj:
        arr.append(obj[i])
    return arr

clear_log = lambda: os.system('cls')

def check_for_forbidden_names(name: str, forbidden_names = config_backend_settings["forbidden_names"]) -> bool:
    return name in forbidden_names

def check_for_forbidden_symbols(name: str, forbidden_symbols = config_backend_settings["forbidden_symbols"]) -> bool:
    check = False
    for symbol in forbidden_symbols:
        if symbol in name:
            check = True
            break
    return check

def print_json_object_configuration(obj: json):
    print(f"| {obj['name']}")
    for parameter in obj:
        if parameter != "name":
            print(f"-| {parameter} : {obj[parameter]}")

def print_json_system_configuration(obj: json):
    for object_name in obj:
        print_json_object_configuration(obj[object_name])

def choose_planet_from_system(arr: list, name: str):
    for planet in arr:
        if planet["name"] == name:
            return planet

def delete_planet_from_system(arr: list, name: str):
    for index in range(len(arr)):
        if arr[index]["name"] == name:
            del arr[index]
            break

def check_object_in_system(arr: list, name: str):
    for object in arr:
        if object["name"] == name: return True
    return False

def index_into_system_by_name(arr: list, name: str) -> int:
    for index in range(len(arr)):
        if arr[index]["name"] == name:
            return index
    return 0

def get_correct_input_data(data: str):
    for delete_symbol in "[],()":
        data = data.replace(delete_symbol, "")
    if " " in data:
        data = data.split(" ")
        for index in range(len(data)):
            data[index] = float(data[index])
    else:
        data = float(data)
    return data

def check_correct_value_rgb(arr: list) -> bool:
    if len(arr) != 3:
        return False
    else:
        for color in arr:
            if (color > 255) or (color < 0):
                return False
        return True