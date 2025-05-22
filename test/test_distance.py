from engine.defs import distance
from engine.classes import *

def test_distance_1():
    inp_A = SpaceObject()
    inp_B = SpaceObject()

    expected_result = 0

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result

def test_distance_2():
    inp_A = SpaceObject(coordinates = [3,4])
    inp_B = SpaceObject()

    expected_result = 5

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result