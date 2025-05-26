import json

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