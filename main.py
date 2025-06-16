from engine.classes import *
from engine.utilities import *
import json
import time
import os
import subprocess

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
            "Помните, что слишком высокая скорость течения времени может приводить к ошибкам в симуляции\n" \
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
    elif (page == "config") and (input_signal[:5] == "edit ") and (len(input_signal) > 5):
        input_signal = input_signal.replace("edit ", "")

        if not check_object_in_system(system_configuration, input_signal):
            input_signal = "error_invalid_object_name"
            continue
        
        modified_object = system_configuration[index_into_system_by_name(system_configuration, input_signal)]

        print(
            f"----- Изменение объекта {input_signal} -----\n" \
            "Старая информация об объекте:"
        )
        print_json_object_configuration(modified_object)
        print(
            "-------------\n" \
            "Стоит обратить внимание, что ввод нескольких чисел осуществляется через пробел\n" \
            "Новые данные:"
        )

        input_data = input("| (назвение)")
        if check_for_forbidden_names(input_signal):
            input_signal = "error_forbidden_name"
            continue
        if check_for_forbidden_symbols(input_signal):
            input_signal = "error_forbidden_symbol"
            continue
        if check_object_in_system(system_configuration, input_signal) and (input_data != input_signal):
            input_signal = "error_invalid_object_name"
            continue
        modified_object["name"] = input_data

        input_data = input("-| mass : ")
        try:
            input_data = get_correct_input_data(input_data)
            if not type(input_data) is float:
                input_signal = "error_incorrect_data_type"
                continue
            modified_object["mass"] = input_data
        except:
            input_signal = "error_incorrect_data_type"
            continue

        input_data = input("-| radius : ")
        try:
            input_data = get_correct_input_data(input_data)
            if (not type(input_data) is float) or (input_data < 1):
                input_signal = "error_incorrect_data_type"
                continue
            modified_object["radius"] = input_data
        except:
            input_signal = "error_incorrect_data_type"
            continue
        
        input_data = input("-| color : ")
        try:
            input_data = get_correct_input_data(input_data)
            if (not type(input_data) is list) or (len(input_data) != 3) or (not check_correct_value_rgb(input_data)):
                input_signal = "error_incorrect_data_type"
                continue
            modified_object["color"] = input_data
        except:
            input_signal = "error_incorrect_data_type"
            continue
        
        input_data = input("-| coordinates : ")
        try:
            input_data = get_correct_input_data(input_data)
            if (not type(input_data) is list) or (len(input_data) != 2):
                input_signal = "error_incorrect_data_type"
                continue
            modified_object["coordinates"] = input_data
        except:
            input_signal = "error_incorrect_data_type"
            continue
        
        input_data = input("-| speed : ")
        try:
            input_data = get_correct_input_data(input_data)
            if (not type(input_data) is list) or (len(input_data) != 2):
                input_signal = "error_incorrect_data_type"
                continue
            modified_object["speed"] = input_data
        except:
            input_signal = "error_incorrect_data_type"
            continue
        
        page = "main"
        input_signal = "config"
        continue
    elif (page == "config") and (input_signal[:7] == "create ") and (len(input_signal) > 7):
        input_signal = input_signal.replace("create ", "")
        if check_for_forbidden_names(input_signal):
            input_signal = "error_forbidden_name"
            continue
        if check_for_forbidden_symbols(input_signal):
            input_signal = "error_forbidden_symbol"
            continue
        if check_object_in_system(system_configuration, input_signal):
            input_signal = "error_invalid_object_name"
            continue

        system_configuration.append({
            "name": input_signal,
            "mass": 0,
            "radius": 1,
            "color": [100, 100, 100],
            "coordinates": [0, 0],
            "speed": [0, 0]
        })

        page = "main"
        input_signal = "config"
        continue
    elif (page == "config") and (input_signal[:7] == "delete ") and (len(input_signal) > 7):
        input_signal = input_signal.replace("delete ", "")

        if len(system_configuration) == 2:
            input_signal = "error_min_number_of_planets"
            continue
        if not check_object_in_system(system_configuration, input_signal):
            input_signal = "error_invalid_object_name"
            continue

        delete_planet_from_system(system_configuration, input_signal)

        page = "main"
        input_signal = "config"
        continue
    elif (page == "config") and (input_signal[:8] == "save_as ") and (len(input_signal) > 8):
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
            "----- Ошибка (недопустимое название) -----\n" \
            "Недопустимое название, пожалуйста попробуйте снова\n" \
            "Если вы заблудились - введите *main*, чтобы вернуться на главную\n" \
            "--------------"
        )
    elif input_signal == "error_forbidden_symbol":
        print(
            "----- Ошибка (недопустимый символ) -----\n" \
            f"Вы использовали недопустимые символы ({read_json_file('data/config/backend_settings.json')['forbidden_symbols']}), пожалуйста попробуйте снова\n" \
            "Если вы заблудились - введите *main*, чтобы вернуться на главную\n" \
            "--------------"
        )
    elif input_signal == "error_min_number_of_planets":
        print(
            "----- Ошибка (достигнуто минимальное количество объектов) -----\n" \
            "Нельзя создать конфигурацию с <2 планет\n" \
            "Если вы заблудились - введите *main*, чтобы вернуться на главную\n" \
            "--------------"
        )
    elif input_signal == "error_invalid_object_name":
        print(
            "----- Ошибка (некорректное имя объекта) -----\n" \
            "Невозможно обработать имя данного объекта, пожалуйста попробуйте снова\n" \
            "Если вы заблудились - введите *main*, чтобы вернуться на главную\n" \
            "--------------"
        )
    elif input_signal == "error_incorrect_data_type":
        print(
            "----- Ошибка (некорректное вид вводимых данных) -----\n" \
            "Неправильный формат вводимых данных\n" \
            "Если вы заблудились - введите *main*, чтобы вернуться на главную\n" \
            "--------------"
        )
    

    # Ошибка о нераспознанной команде

    else:
        input_signal = "error_uncknow_command"
        continue

    # Ввод команды

    input_signal = input("Выполнить: ")
    