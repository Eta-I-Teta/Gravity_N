from engine.classes import *
from engine.utilities import *
import json
import time
import os
import subprocess

clear_log = lambda: os.system('cls')

def print_json_system_configuration(obj: json):
    for object_name in obj:
        print(f"| {obj[object_name]['name']}")
        for parameter in obj[object_name]:
            if parameter != "name":
                print(f"-| {parameter} : {obj[object_name][parameter]}")

forbidden_names = [
    "save",
    "load",
    "delete",
    "main",
    "error_uncknow_command",
    "error_forbidden_name",
    "error_forbidden_symbol",
    ""
]
forbidden_symbols = ['.', ',', '<', '>', ':', '"', "'", '/', '\\', '|', '?', '*']

def check_for_forbidden_names(name: str, forbidden_names = forbidden_names) -> bool:
    return name in forbidden_names
def check_for_forbidden_symbols(name: str, forbidden_symbols = forbidden_symbols) -> bool:
    check = False
    for symbol in forbidden_symbols:
        if symbol in name:
            check = True
            break
    return check

system_configuration = json_to_list( read_json_file("data/config/standart_planet_system.json") )
object_attributes = read_json_file("data/config/backend_settings.json")["SpaceObject_attributes"]

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
            "config - Открыть текущую конфигурацию\n" \
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
        print_json_system_configuration( read_json_file(f"data/user_saves/{selected_file_name}.json") )
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
        system_configuration = json_to_list( read_json_file(f"data/user_saves/{selected_file_name}.json") )

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
        print_json_system_configuration( list_to_json(system_configuration) )
        print(
            "--------------\n" \
            "Для открытия инструкции по управлению нажмите ESC в открытой программе\n" \
            "start - Да, уверен\n" \
            "main - Нет, вернуться на главную\n" \
            "--------------"
        )
    elif (page == "start") and (input_signal == "start"):
        
        save_json_file(
            list_to_json(system_configuration),
            "data/user_saves/latest_configuration.json"
        )
        subprocess.run(["python", "render.py"])

        print("Программа запущена")
        break
    
    # Работа с текущей конфигурацией

    elif (page == "main") and (input_signal == "config"):
        page = "config"
        print("----- Текущая конфигурация -----")
        print_json_system_configuration( list_to_json(system_configuration) )
        print(
            "-------------\n" \
            "edit *object name* - Изменить параметров объекта\n" \
            "create *object name* - Создать новый объект\n" \
            "delete *object name* - Удалить объект\n" \
            "save_as *name* - Сохранить конфигурацию\n" \
            "main - Вернуться на главную\n" \
            "-------------"
        )
    elif (page == "config") and (input_signal[:4] == "edit") and (len(input_signal) > 4):
        print("----- Изменение параметров объекта -----")
    elif (page == "config") and (input_signal[:6] == "create") and (len(input_signal) > 6):
        pass
    elif (page == "config") and (input_signal[:6] == "delete") and (len(input_signal) > 6):
        pass
    elif (page == "config") and (input_signal[:7] == "save_as") and (len(input_signal) > 7):
        input_signal = input_signal.replace('save_as ', '')

        if check_for_forbidden_names(input_signal):
            input_signal = "error_forbidden_name"
            continue
        if check_for_forbidden_symbols(input_signal):
            input_signal = "error_forbidden_symbol"
            continue
        
        save_json_file(
            list_to_json( system_configuration ),
            f"data/user_saves/{input_signal}.json"
        )

        input_signal = "main"
        print("----- Файл был успешно сохранён -----")
        time.sleep(2)
        continue

    # Отображение ошибок

    elif input_signal == "error_uncknow_command":
        print(
            "----- Ошибка ввода -----\n" \
            "Программа не опознаёт введённую команду, пожалуйста попробуйте снова\n" \
            "Если вы заблудились - введите *main*, чтобы вернуться на главную\n" \
            "--------------"
        )
    elif input_signal == "error_forbidden_name":
        print(
            "----- Ошибка имени файла -----\n" \
            "Недопустимое имя файла, пожалуйста попробуйте снова\n" \
            "Если вы заблудились - введите *main*, чтобы вернуться на главную\n" \
            "--------------"
        )
    elif input_signal == "error_forbidden_symbol":
        print(
            "----- Ошибка имени файла -----\n" \
            f"Вы использовали недопустимые символы ({forbidden_symbols}), пожалуйста попробуйте снова\n" \
            "Если вы заблудились - введите *main*, чтобы вернуться на главную\n" \
            "--------------"
        )

    # Ошибка о нераспознанной команде

    else:
        input_signal = "error_uncknow_command"
        continue

    # Ввод команды

    input_signal = input("Выполнить: ")
    