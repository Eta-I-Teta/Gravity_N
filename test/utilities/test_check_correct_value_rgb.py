from engine.utilities import check_correct_value_rgb
from engine.classes import *

def test_check_correct_value_rgb_1():
    inp_value = [1, 256, 0]
    expected_result = False

    assert check_correct_value_rgb(inp_value) == expected_result

def test_check_correct_value_rgb_2():
    inp_value = [0, 255, 0]
    expected_result = True

    assert check_correct_value_rgb(inp_value) == expected_result

def test_check_correct_value_rgb_3():
    inp_value = [-1, 128, 200]
    expected_result = False

    assert check_correct_value_rgb(inp_value) == expected_result

def test_check_correct_value_rgb_4():
    inp_value = [100, 100, 100]
    expected_result = True

    assert check_correct_value_rgb(inp_value) == expected_result

def test_check_correct_value_rgb_5():
    inp_value = [0, 0, 0]
    expected_result = True

    assert check_correct_value_rgb(inp_value) == expected_result

def test_check_correct_value_rgb_6():
    inp_value = [255, 255, 255]
    expected_result = True

    assert check_correct_value_rgb(inp_value) == expected_result