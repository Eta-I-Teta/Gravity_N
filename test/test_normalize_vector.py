from engine.defs import normalize_vector
from engine.classes import *

def test_normalize_vector_1():
    inp_value = [1, 3]

    expected_result = [1/(10)**0.5, 3/(10)**0.5]

    assert normalize_vector(inp_value) == expected_result