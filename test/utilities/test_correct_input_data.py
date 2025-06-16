from engine.utilities import get_correct_input_data
from engine.classes import *

def test_get_correct_input_data_1():
    inp_value = "1()[],45"
    expected_result = 145.0

    assert get_correct_input_data(inp_value) == expected_result

def test_get_correct_input_data_2():
    inp_value = "123 456 789"
    expected_result = [123.0, 456.0, 789.0]

    assert get_correct_input_data(inp_value) == expected_result

def test_get_correct_input_data_3():
    inp_value = "3.14, 2.718"
    expected_result = [3.14, 2.718]

    assert get_correct_input_data(inp_value) == expected_result

def test_get_correct_input_data_4():
    inp_value = "100"
    expected_result = 100.0

    assert get_correct_input_data(inp_value) == expected_result

def test_get_correct_input_data_5():
    inp_value = "42"
    expected_result = 42.0

    assert get_correct_input_data(inp_value) == expected_result

def test_get_correct_input_data_6():
    inp_value = "1, 2, 3, 4, 5"
    expected_result = [1.0, 2.0, 3.0, 4.0, 5.0]

    assert get_correct_input_data(inp_value) == expected_result