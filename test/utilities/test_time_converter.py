from engine.utilities import time_converter
from engine.classes import *

def test_time_converter_1():
    inp_value = 1e6
    expected_result = "0 в. 0 лет 11 д. 13 ч. 46 мин. 40.0 с."

    assert time_converter(inp_value) == expected_result

def test_time_converter_2():
    inp_value = 60
    expected_result = "0 в. 0 лет 0 д. 0 ч. 1 мин. 0.0 с."
    
    assert time_converter(inp_value) == expected_result

def test_time_converter_3():
    inp_value = 3600
    expected_result = "0 в. 0 лет 0 д. 1 ч. 0 мин. 0.0 с."
    
    assert time_converter(inp_value) == expected_result

def test_time_converter_4():
    inp_value = 86400
    expected_result = "0 в. 0 лет 1 д. 0 ч. 0 мин. 0.0 с."
    
    assert time_converter(inp_value) == expected_result

def test_time_converter_5():
    inp_value = 31536000
    expected_result = "0 в. 1 лет 0 д. 0 ч. 0 мин. 0.0 с."
    
    assert time_converter(inp_value) == expected_result

def test_time_converter_6():
    inp_value = 3153600000
    expected_result = "1 в. 0 лет 0 д. 0 ч. 0 мин. 0.0 с."
    
    assert time_converter(inp_value) == expected_result

def test_time_converter_7():
    inp_value = 123456789
    expected_result = "0 в. 3 лет 333 д. 21 ч. 33 мин. 9.0 с."
    
    assert time_converter(inp_value) == expected_result