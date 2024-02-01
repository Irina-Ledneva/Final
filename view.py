import text_fields
import json

def input_choice():
    while True:
        number = input(text_fields.input_choice)
        if number.isdigit() and 0 < int(number) < 7:
            return int(number)
        else:
            print(text_fields.wrong_choice)

def main_menu():
    print(text_fields.menu)
    return input_choice()

def read_animals():
    with open('animals.json') as file:
        animals = json.load(file)
        count = 1
        for animal in animals:
            print()
            print(f'Питомец {count}')
            for key, value in animal.items():
                print(f'{key}: {value}')
            count += 1
            print()
        print(f'Всего животных: {count - 1}')

def animals_types():
    print(text_fields.types_of_animals)
    return(input(text_fields.animal_choice))

def read_comands():
    print(text_fields.comands)
    with open('animals_comands.json') as file:
        comands = json.load(file)
        for comand in comands:
            for key, value in comand.items():
                print(f'{key} {value}')