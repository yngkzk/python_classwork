import json
import time

with open('quest.json', encoding='utf-8') as my_file:
    quest = json.load(my_file)

greeting = f'''
Добро пожаловать в игру '{quest["info"]["name"]}'!
Авторы игры: {quest["info"]["author"]}
Версия игры: {quest["info"]["version"]}
'''
print(greeting)


def show_description(scene):
    description = quest["game"][scene]["description"]
    print(description)


def is_game_end(scene):
    if "actions" in quest["game"][scene]:
        return False
    return True


def show_actions(scene):
    print('Что будете делать?')
    for action in quest["game"][scene]["actions"]:
        print(' -> ', action["name"])


def get_user_action():
    while True:
        user_in = input()
        if user_in:
            return user_in


def check_action(scene, action_name):
    for allowed_action in quest["game"][scene]["actions"]:
        if allowed_action["name"] == action_name:
            return allowed_action["effect"]


def perform_action(effect):
    global current_scene
    current_scene = effect["go"]


current_scene = 'start'

while True:
    time.sleep(3)
    print(f'\n{"-" * 50} \n')
    show_description(current_scene)
    if is_game_end(current_scene):
        break
    show_actions(current_scene)
    action = get_user_action()
    effect = check_action(current_scene, action)
    if effect:
        perform_action(effect)
    else:
        print('Такого действия нету. Выберите другое')

