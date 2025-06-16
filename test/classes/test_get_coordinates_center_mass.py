from engine.classes import *

def test_get_coordinates_center_mass_1():
    planet1 = SpaceObject(mass=10, coordinates=[0, 0])
    planet2 = SpaceObject(mass=20, coordinates=[3, 0])
    planet3 = SpaceObject(mass=30, coordinates=[0, 4])
    
    space = OuterSpace(planets=deque([planet1, planet2, planet3]))
    
    result = space.get_coordinates_center_mass()
    expected_result = [(0*10 + 3*20 + 0*30) / 60, (0*10 + 0*20 + 4*30) / 60]
    assert result == expected_result

def test_get_coordinates_center_mass_2():
    planet1 = SpaceObject(mass=5, coordinates=[1, 2])
    planet2 = SpaceObject(mass=5, coordinates=[3, 6])
    
    space = OuterSpace(planets=deque([planet1, planet2]))
    
    result = space.get_coordinates_center_mass()
    expected_result = [(1*5 + 3*5)/10, (2*5 + 6*5)/10]
    assert result == expected_result

def test_get_coordinates_center_mass_3():
    planet = SpaceObject(mass=8, coordinates=[4, 4])
    
    space = OuterSpace(planets=deque([planet]))
    
    result = space.get_coordinates_center_mass()
    expected_result = [4, 4]
    assert result == expected_result

def test_get_coordinates_center_mass_4():
    planet1 = SpaceObject(mass=100, coordinates=[10, 20])
    planet2 = SpaceObject(mass=200, coordinates=[30, 40])
    
    space = OuterSpace(planets=deque([planet1, planet2]))
    
    result = space.get_coordinates_center_mass()
    expected_result = [(10*100 + 30*200)/300, (20*100 + 40*200)/300]
    assert result == expected_result

def test_get_coordinates_center_mass_5():
    planet1 = SpaceObject(mass=1, coordinates=[-5, -5])
    planet2 = SpaceObject(mass=1, coordinates=[5, 5])
    planet3 = SpaceObject(mass=1, coordinates=[-5, 5])
    planet4 = SpaceObject(mass=1, coordinates=[5, -5])
    
    space = OuterSpace(planets=deque([planet1, planet2, planet3, planet4]))
    
    result = space.get_coordinates_center_mass()
    expected_result = [0, 0]
    assert result == expected_result

def test_get_coordinates_center_mass_6():
    planet1 = SpaceObject(mass=0, coordinates=[1, 1])
    planet2 = SpaceObject(mass=10, coordinates=[2, 2])
    
    space = OuterSpace(planets=deque([planet1, planet2]))
    
    result = space.get_coordinates_center_mass()
    expected_result = [2, 2]
    assert result == expected_result