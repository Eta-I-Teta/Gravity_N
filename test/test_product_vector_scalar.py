from engine.utilities import product_vector_scalar
from engine.classes import *

def test_product_vector_scalar_1():
    inp_scalar = 5
    inp_vector = [1, 3]

    expected_result = [5, 15]
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result

def test_product_vector_scalar_2():
    inp_scalar = 2
    inp_vector = [1, 2, 3]

    expected_result = [2, 4, 6]
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result

def test_product_vector_scalar_3():
    inp_scalar = -0.5
    inp_vector = [1.0, 2.0, 3.0]

    expected_result = [-0.5, -1.0, -1.5]
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result

def test_product_vector_scalar_4():
    inp_scalar = 0
    inp_vector = [100, -200, 3.14]

    expected_result = [0, 0, 0]
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result

def test_product_vector_scalar_5():
    inp_scalar = 10
    inp_vector = []

    expected_result = []
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result

def test_product_vector_scalar_6():
    inp_scalar = 1
    inp_vector = [-5, 0, 5]

    expected_result = [-5, 0, 5]
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result

def test_product_vector_scalar_7():
    inp_scalar = 1e6
    inp_vector = [2, 3]

    expected_result = [2e6, 3e6]
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result

def test_product_vector_scalar_8():
    inp_scalar = 0.5
    inp_vector = [10, 20]

    expected_result = [5.0, 10.0]
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result

def test_product_vector_scalar_9():
    inp_scalar = 3
    inp_vector = [0, 0, 0]

    expected_result = [0, 0, 0]
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result

def test_product_vector_scalar_10():
    inp_scalar = 2
    inp_vector = [-1, -2, -3]

    expected_result = [-2, -4, -6]
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result

def test_product_vector_scalar_11():
    inp_scalar = 1e-10
    inp_vector = [1, 2, 3]

    expected_result = [1e-10, 2e-10, 3e-10]
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result

def test_product_vector_scalar_12():
    inp_scalar = 3
    inp_vector = [7]

    expected_result = [21]
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result

def test_product_vector_scalar_13():
    inp_scalar = 2.0
    inp_vector = [1, 2]

    expected_result = [2.0, 4.0]
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result

def test_product_vector_scalar_14():
    inp_scalar = 3
    inp_vector = [1] * 1000
    
    expected_result = [3] * 1000
    
    assert product_vector_scalar(inp_scalar, inp_vector) == expected_result