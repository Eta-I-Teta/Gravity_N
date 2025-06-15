from engine.classes import *
from engine.utilities import *
import json
import time
import os
import subprocess

clear_log = lambda: os.system('cls')

def print_json_planet_system(obj: json):
    for planet_name in obj:
        print(f"| {obj[planet_name]['name']}")
        for parameter in obj[planet_name]:
            if parameter != "name":
                print(f"-| {parameter} : {obj[planet_name][parameter]}")

planet_configuration = json_into_array( read_json_file("data/config/standart_planet_system.json") )

forbidden_names_files_and_planets = [
    "save",
    "load",
    "delete",
    "main",
    ""
]

input_signal = "main"
page = "main"

do_clear = True

while True:

    clear_log()

    # Главная и выход
    
    if input_signal == "main":
        page = "main"
        print(
            "----- Главная -----\n" \
            "start - Запустить программу\n" \
            "files - Посмотреть файлы сохранений\n" \
            "*save *name* - Сохранить конфигурацию\n" \
            "*edit - Изменить конфигурацию\n" \
            "exit - Выйти из программы\n" \
            "--------------"
        )
    elif (page == "main") and (input_signal == "exit"):
        print("Вы вышли из программы")
        break
    
    # Работа с файлами

    elif (page == "main") and (input_signal == "files"):
        page = "files"

        save_files = []
        for file_name in os.listdir("data/user_saves"):
            if ".json" in file_name:
                save_files.append(file_name.replace(".json", ""))
        
        print("----- Доступные файлы -----")
        for i in save_files:
            print(f"| {i}")
        print(
            "--------------\n" \
            "Введите название файла, чтобы его выбрать\n" \
            "main - для выхода в главное меню\n" \
            "--------------"
        )
    elif (page == "files") and (input_signal in save_files):
        page = "selected_file"
        selected_file_name = input_signal

        print(
            f"----- Файл {selected_file_name} -----\n" \
            "Содержание:"
        )
        print_json_planet_system( read_json_file(f"data/user_saves/{selected_file_name}.json") )
        print(
            "-------------\n" \
            "load - Загрузить конфигурацию\n" \
            "delete - Удалить конфигурацию\n" \
            "main - Вернуться на главную\n" \
            "-------------"
        )
    elif (page == "selected_file") and (input_signal == "delete"):
        os.remove(f"data/user_saves/{selected_file_name}.json")

        input_signal = "main"
        print("----- Файл был успешно удалён -----")
        time.sleep(2)
        continue
    elif (page == "selected_file") and (input_signal == "load"):
        planet_configuration = json_into_array( read_json_file(f"data/user_saves/{selected_file_name}.json") )

        input_signal = "main"
        print("----- Файл был успешно загружен -----")
        time.sleep(2)
        continue

    # Запуск рендера

    elif (page == "main") and (input_signal == "start"):
        page = "start"
        print(
            "----- Вы уверены, что хотите запустить программу? -----\n" \
            "Конфигурация запуска:"
        )
        print_json_planet_system( list_to_json(planet_configuration) )
        print(
            "--------------\n" \
            "start - Да, уверен\n" \
            "main - Нет, вернуться на главную\n" \
            "--------------"
        )
    elif (page == "start") and (input_signal == "start"):
        
        save_json_file(
            list_to_json(planet_configuration),
            "data/user_saves/latest_configuration.json"
        )
        subprocess.run(["python", "render.py"])

        print("Программа запущена")
        break
    
    # Ошибка о нераспознанной команде

    else:
        print(
            "----- Ошибка ввода -----\n" \
            f"Программа не опознаёт введённую команду *{input_signal}*, пожалуйста попробуйте снова\n" \
            "Если вы заблудились - введите *main*, чтобы вернуться на главную\n" \
            "--------------"
        )

    # Ввод команды

    input_signal = input("Выполнить: ")
    