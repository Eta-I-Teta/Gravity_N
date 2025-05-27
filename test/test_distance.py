from engine.utilities import distance

def test_distance_1():
    inp_A = coordinates = [0, 0]
    inp_B = coordinates = [0, 0]

    expected_result = 0
    
    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result

def test_distance_2():
    inp_A = coordinates = [3,4]
    inp_B = coordinates = [0, 0]

    expected_result = 5

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result

def test_distance_3():
    inp_A = coordinates = [3, 4]
    inp_B = coordinates = [0, 0]

    expected_result = 5

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result

def test_distance_4():
    inp_A = coordinates = [3, 4]
    inp_B = coordinates = [4, 3]

    expected_result = 2**0.5

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result

def test_distance_4():
    inp_A = coordinates = [3, 4]
    inp_B = coordinates = [4, 3]

    expected_result = 2**0.5

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result

def test_distance_5():
    inp_A = coordinates=[3, 4]
    inp_B = coordinates=[6, 8]

    expected_result = 5.0

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result

def test_distance_6():
    inp_A = coordinates=[5, -3]
    inp_B = coordinates=[-2, 7]

    expected_result = 149**0.5

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result

def test_distance_7():
    inp_A = coordinates=[0, 5]
    inp_B = coordinates=[0, -3]

    expected_result = 8.0

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result

def test_distance_8():
    inp_A = coordinates=[-2, 0]
    inp_B = coordinates=[7, 0]

    expected_result = 9.0

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result

def test_distance_9():
    inp_A = coordinates=[1.5, 2.5]
    inp_B = coordinates=[4.5, 6.5]

    expected_result = 5.0

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result

def test_distance_10():
    inp_A = coordinates=[1e308, 1e308]
    inp_B = coordinates=[-1e308, -1e308]

    expected_result = float('inf')

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result

def test_distance_11():
    inp_A = coordinates=[7, 10]
    inp_B = coordinates=[7, 20]
    
    expected_result = 10.0

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result

def test_distance_12():
    inp_A = coordinates=[10, 5]
    inp_B = coordinates=[20, 5]
    
    expected_result = 10.0

    assert distance(inp_A, inp_B) == expected_result
    assert distance(inp_B, inp_A) == expected_result