import json
import text_fields
import view

animals_list = []
comands_list = []

class Animals:
    def animal_name(self):
        self.name = input(text_fields.animal_name)


class Pets(Animals):
    pass

class PackAnimals(Animals):
    pass

class Dogs(Pets):
    pass

class Cats(Pets):
    pass

class Hamsters(Pets):
    pass

class Horses(PackAnimals):
    pass

class Camels(PackAnimals):
    pass

class Donkeys(PackAnimals):
    pass

def save_animals():
    with open('animals.json', 'w') as file:
        json.dump(animals_list, file)
    print(text_fields.animal_append)

def add_animal():
    animal = view.animals_types()
    match animal:
        case 'Собака':
            new_animal = Dogs()
            new_animal.animal_name()
            animals_list.append({'Собака': new_animal.name})
            save_animals()
            print(new_animal.name)
        case 'Кошка':
            new_animal = Cats()
            new_animal.animal_name()
            animals_list.append({'Кошка': new_animal.name})
            save_animals()
        case 'Хомяк':
            new_animal = Hamsters()
            new_animal.animal_name()
            animals_list.append({'Хомяк': new_animal.name})
            save_animals()
        case 'Лошадь':
            new_animal = Horses()
            new_animal.animal_name()
            animals_list.append({'Лошадь': new_animal.name})
            save_animals()
        case 'Верблюд':
            new_animal = Camels()
            new_animal.animal_name()
            animals_list.append({'Верблюд': new_animal.name})
            save_animals()
        case 'Осёл':
            new_animal = Donkeys()
            new_animal.animal_name()
            animals_list.append({'Осёл': new_animal.name})
            save_animals()
        case _:
            print(text_fields.wrong_animal)


def learn_comand():
    animal_type = input(text_fields.type_animal)
    animal_name = input(text_fields.name_comand)
    animal_comand = input(text_fields.say_comand)
    with open('animals.json') as file:
         animals = json.load(file)
    for animal in animals:
        for k, v in animal.items():
            if k == animal_type and v == animal_name:
                comands_list.append({f'{animal_type} {animal_name}': f'умеет {animal_comand}'})
                with open('animals_comands.json', 'w') as file:
                    json.dump(comands_list, file)
                return (print(f'{animal_type} {animal_name} теперь умеет {animal_comand}'))
    return (print(text_fields.comand_wrong))


def del_animal():
    print(text_fields.deleate)
    animal_type = input(text_fields.type_animal)
    animal_name = input(text_fields.name_comand)
    with open('animals.json') as file:
         animals = json.load(file)
    for animal in animals:
        for k, v in animal.items():
            if k == animal_type and v == animal_name:
                animals.remove(animal)
                with open('animals.json', 'w') as file:
                    json.dump(animals, file)
                return (print(text_fields.animal_del))
    return(print(text_fields.comand_wrong))