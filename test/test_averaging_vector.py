from engine.utilities import averaging_vector
from engine.classes import *

def test_averaging_vector_1():
    inp_vector = [[4, 3], [3, 4]]
    expected_result = [3.5, 3.5]
    
    assert averaging_vector(inp_vector) == expected_result

def test_averaging_vector_2():
    inp_vector = [[5, 10]]
    expected_result = [5, 10]
    
    assert averaging_vector(inp_vector) == expected_result

def test_averaging_vector_3():
    inp_vector = [[1, 2], [3, 4], [5, 6]]
    expected_result = [(1+3+5)/3, (2+4+6)/3]
    
    assert averaging_vector(inp_vector) == expected_result

def test_averaging_vector_4():
    inp_vector = [[-1, -2], [1, 2]]
    expected_result = [0.0, 0.0]
    
    assert averaging_vector(inp_vector) == expected_result

def test_averaging_vector_5():
    inp_vector = [[0, 0], [0, 0]]
    expected_result = [0.0, 0.0]
    
    assert averaging_vector(inp_vector) == expected_result

def test_averaging_vector_6():
    inp_vector = [[1], [2], [3]]
    expected_result = [2.0]
    
    assert averaging_vector(inp_vector) == expected_result