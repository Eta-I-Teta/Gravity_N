from engine.utilities import not_zero
from engine.classes import *

def test_not_zero_1():
    inp_value = 0
    expected_result = 1e-18

    assert not_zero(inp_value) == expected_result

def test_not_zero_2():
    inp_value = 5.0
    expected_result = 5.0

    assert not_zero(inp_value) == expected_result

def test_not_zero_3():
    inp_value = -3.2
    expected_result = -3.2

    assert not_zero(inp_value) == expected_result

def test_not_zero_4():
    inp_value = 1e-20
    expected_result = 1e-18

    assert not_zero(inp_value) == expected_result

def test_not_zero_5():
    inp_value = 1e-18
    expected_result = 1e-18
    
    assert not_zero(inp_value) == expected_result