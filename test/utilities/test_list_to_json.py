from engine.utilities import list_to_json

def test_list_to_json_1():
    inp_value = []
    expected_result = {}
    assert list_to_json(inp_value) == expected_result


def test_list_to_json_2():
    inp_value = [
        {"value": "abc"}
    ]
    expected_result = {
        "0": {"value": "abc"}
    }
    assert list_to_json(inp_value) == expected_result


def test_list_to_json_3():
    inp_value = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]
    expected_result = {
        "0": {"id": 1, "name": "Alice"},
        "1": {"id": 2, "name": "Bob"},
        "2": {"id": 3, "name": "Charlie"}
    }
    assert list_to_json(inp_value) == expected_result


def test_list_to_json_4():
    inp_value = [
        {"user": {"name": "John", "age": 30}},
        {"user": {"name": "Jane", "age": 25}}
    ]
    expected_result = {
        "0": {"user": {"name": "John", "age": 30}},
        "1": {"user": {"name": "Jane", "age": 25}}
    }
    assert list_to_json(inp_value) == expected_result


def test_list_to_json_5():
    inp_value = [
        "text",
        123,
        True,
        None,
        {"key": "value"}
    ]
    expected_result = {
        "0": "text",
        "1": 123,
        "2": True,
        "3": None,
        "4": {"key": "value"}
    }
    assert list_to_json(inp_value) == expected_result