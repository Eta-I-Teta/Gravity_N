from engine.classes import *

def test_SpaceObject_initialization_1():
    obj = SpaceObject(
        name="Earth", 
        mass=5.97e24, 
        coordinates=[100, 200], 
        radius=6371, 
        speed=[10, 20], 
        acceleration=[0.1, 0.2], 
        color=(0, 0, 255)
    )
    
    assert obj.name == "Earth"
    assert obj.mass == 5.97e24
    assert obj.coordinates == [100, 200]
    assert obj.radius == 6371
    assert obj.speed == [10, 20]
    assert obj.acceleration == [0.1, 0.2]
    assert obj.color == (0, 0, 255)


def test_SpaceObject_initialization_2():
    obj = SpaceObject(
        name="Mars", 
        mass=6.39e23, 
        coordinates=[-300, 400], 
        radius=3389, 
        speed=[-5, 10], 
        acceleration=[0.05, -0.1], 
        color=(255, 0, 0)
    )
    
    assert obj.name == "Mars"
    assert obj.mass == 6.39e23
    assert obj.coordinates == [-300, 400]
    assert obj.radius == 3389
    assert obj.speed == [-5, 10]
    assert obj.acceleration == [0.05, -0.1]
    assert obj.color == (255, 0, 0)


def test_SpaceObject_initialization_3():
    obj = SpaceObject(
        name="Moon", 
        mass=7.34e22, 
        coordinates=[150, -50], 
        radius=1737, 
        speed=[2, -3], 
        acceleration=[-0.01, 0.02], 
        color=(200, 200, 200)
    )
    
    assert obj.name == "Moon"
    assert obj.mass == 7.34e22
    assert obj.coordinates == [150, -50]
    assert obj.radius == 1737
    assert obj.speed == [2, -3]
    assert obj.acceleration == [-0.01, 0.02]
    assert obj.color == (200, 200, 200)


def test_SpaceObject_initialization_4():
    obj = SpaceObject(
        name="Sun", 
        mass=1.99e30, 
        coordinates=[0, 0], 
        radius=696340, 
        speed=[0, 0], 
        acceleration=[0, 0], 
        color=(255, 255, 0)
    )
    
    assert obj.name == "Sun"
    assert obj.mass == 1.99e30
    assert obj.coordinates == [0, 0]
    assert obj.radius == 696340
    assert obj.speed == [0, 0]
    assert obj.acceleration == [0, 0]
    assert obj.color == (255, 255, 0)


def test_SpaceObject_initialization_5():
    obj = SpaceObject(
        name="Satellite", 
        mass=1000, 
        coordinates=[500, 600], 
        radius=5, 
        speed=[7.8, 0], 
        acceleration=[0, 9.8], 
        color=(150, 150, 150)
    )
    
    assert obj.name == "Satellite"
    assert obj.mass == 1000
    assert obj.coordinates == [500, 600]
    assert obj.radius == 5
    assert obj.speed == [7.8, 0]
    assert obj.acceleration == [0, 9.8]
    assert obj.color == (150, 150, 150)