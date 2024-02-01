import view
import model

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                view.read_animals()
            case 2:
                view.read_comands()
            case 3:
                model.add_animal()
            case 4:
                model.del_animal()
            case 5:
                model.learn_comand()
            case 6:
                break

