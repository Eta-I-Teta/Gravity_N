from engine.classes import *

def test_get_most_remote_planet_1():
    planet1 = SpaceObject(coordinates=[0, 0])
    planet2 = SpaceObject(coordinates=[3, 0])
    planet3 = SpaceObject(coordinates=[0, 4])
    
    space = OuterSpace(planets=deque([planet1, planet2, planet3]))
    center = [0, 0]
    
    excepted_result = planet3
    
    assert excepted_result == space.get_most_remote_planet(center)


def test_get_most_remote_planet_2():
    planet1 = SpaceObject(coordinates=[1, 1])
    planet2 = SpaceObject(coordinates=[-5, 0])
    planet3 = SpaceObject(coordinates=[3, 2])
    planet4 = SpaceObject(coordinates=[0, -10])
    
    space = OuterSpace(planets=deque([planet1, planet2, planet3, planet4]))
    center = [0, 0]
    
    excepted_result = planet4
    
    assert excepted_result == space.get_most_remote_planet(center)


def test_get_most_remote_planet_3():
    planet1 = SpaceObject(coordinates=[100, 100])
    planet2 = SpaceObject(coordinates=[-100, -100])
    planet3 = SpaceObject(coordinates=[100, -100])
    
    space = OuterSpace(planets=deque([planet1, planet2, planet3]))
    center = [0, 0]
    
    excepted_result = [planet1, planet2]
    
    result = space.get_most_remote_planet(center)
    assert result in excepted_result


def test_get_most_remote_planet_4():
    planets = deque()
    for i in range(10000):
        planets.append(SpaceObject(coordinates=[i, i]))
    
    space = OuterSpace(planets=planets)
    center = [0, 0]
    
    excepted_result = planets[-1]
    
    assert excepted_result == space.get_most_remote_planet(center)