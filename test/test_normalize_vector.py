from engine.utilities import normalize_vector
from engine.classes import *

def test_normalize_vector_1():
    inp_value = [1, 3]

    expected_result = [1/(10)**0.5, 3/(10)**0.5]

    assert normalize_vector(inp_value) == expected_result

def test_normalize_vector_2():
    inp_value = [0.5, 1.5]

    expected_result = [0.5/(2.5)**0.5, 1.5/(2.5)**0.5]

    assert normalize_vector(inp_value) == expected_result

def test_normalize_vector_3():
    inp_value = [-2, 2]

    expected_result = [-2/(8)**0.5, 2/(8)**0.5]

    assert normalize_vector(inp_value) == expected_result

def test_normalize_vector_4():
    inp_value = [5]

    expected_result = [1.0]

    assert normalize_vector(inp_value) == expected_result

def test_normalize_vector_5():
    inp_value = [1e6, 2e6]

    expected_result = [1e6/(5e12)**0.5, 2e6/(5e12)**0.5]

    assert normalize_vector(inp_value) == expected_result

def test_normalize_vector_6():
    inp_value = [1e-10, 2e-10]

    expected_result = [1e-10/(5e-20)**0.5, 2e-10/(5e-20)**0.5]

    assert normalize_vector(inp_value) == expected_result

def test_normalize_vector_7():
    inp_value = [1, 2, 2]

    expected_result = [1/3, 2/3, 2/3]

    assert normalize_vector(inp_value) == expected_result

def test_normalize_vector_8():
    inp_value = [0, 5]

    expected_result = [0, 1.0]

    assert normalize_vector(inp_value) == expected_result

def test_normalize_vector_9():
    inp_value = [3, 3, 3]

    expected_result = [3/(27)**0.5]*3

    assert normalize_vector(inp_value) == expected_result