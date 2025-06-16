from engine.classes import *
from engine.utilities import *
import json

while True:
    data = get_correct_input_data(input())
    print(data, type(data), check_correct_value_rgb(data))