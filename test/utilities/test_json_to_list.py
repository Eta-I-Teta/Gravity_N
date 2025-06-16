from engine.utilities import json_to_list
import json

def test_json_to_list_1():
    inp_value = {
        "2": {"value": "abc"}
    }
    expected_result = [
        {"value": "abc"}
    ]

    assert json_to_list(inp_value) == expected_result

def test_json_to_list_2():
    inp_value = {
        "1": {"id": 1, "name": "item1"},
        "5": {"id": 5, "name": "item5"}
    }
    expected_result = [
        {"id": 1, "name": "item1"},
        {"id": 5, "name": "item5"}
    ]

    assert json_to_list(inp_value) == expected_result

def test_json_to_list_3():
    inp_value = {}
    expected_result = []

    assert json_to_list(inp_value) == expected_result

def test_json_to_list_4():
    inp_value = {
        "10": {"active": False},
        "20": {"active": True},
        "30": {"active": False}
    }
    expected_result = [
        {"active": False},
        {"active": True},
        {"active": False}
    ]

    assert json_to_list(inp_value) == expected_result