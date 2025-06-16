from engine.utilities import get_beautiful_number
from engine.classes import *

def test_get_beautiful_number_1():
    inp_value = 9876543210
    expected_result = "9.876543e9"

    assert get_beautiful_number(inp_value) == expected_result

def test_get_beautiful_number_2():
    inp_value = 1000000
    expected_result = "1.0e6"

    assert get_beautiful_number(inp_value) == expected_result

def test_get_beautiful_number_3():
    inp_value = 12345
    expected_result = "1.2345e4"

    assert get_beautiful_number(inp_value) == expected_result

def test_get_beautiful_number_4():
    inp_value = 0.000123456
    expected_result = "1.23456e-4"

    assert get_beautiful_number(inp_value) == expected_result

def test_get_beautiful_number_5():
    inp_value = -9876.54321
    expected_result = "-9.876543e3"

    assert get_beautiful_number(inp_value) == expected_result

def test_get_beautiful_number_6():
    inp_value = 0
    expected_result = "0.0e0"

    assert get_beautiful_number(inp_value) == expected_result

def test_get_beautiful_number_7():
    inp_value = 1.0
    expected_result = "1.0e0"

    assert get_beautiful_number(inp_value) == expected_result

def test_get_beautiful_number_8():
    inp_value = 9999999999999999
    expected_result = "1.0e16"

    assert get_beautiful_number(inp_value) == expected_result

def test_get_beautiful_number_9():
    inp_value = 1.23456789e-10
    expected_result = "1.234568e-10"

    assert get_beautiful_number(inp_value) == expected_result

def test_get_beautiful_number_10():
    inp_value = 42
    expected_result = "4.2e1"

    assert get_beautiful_number(inp_value) == expected_result