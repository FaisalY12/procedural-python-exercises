import name_generator
import os
import pdb

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def get_user_name():
    name = input("\nHi, what's your name?\n")
    return name

def get_user_birth_month():
    month = input("\nAnd what month were you born in?\n")
    return month

def get_user_animal():
    animal = input("\nFinally, would you like to have a dragon name, or a penguin name? Type 'dragon' or 'penguin'.\n")
    return animal

def run():
    clear_screen()
    try:
        name = get_user_name()
        month = get_user_birth_month()
        animal = get_user_animal()
        result = handle_dragon_generator(month) if animal == 'dragon' else handle_penguin_generator(month)
        print(f"\nHey {name}, your {animal} name is: {result}\n")
    except Exception as e:
        pdb.set_trace()
        print("\nTerribly sorry, there's been an error!\n")
    finally:
        print("\nThanks for using our animal name generator!!\n")
    
def handle_dragon_generator(month):
    func = getattr(name_generator.dragon_name, "user_dragon")
    result = func(month)
    return result

def handle_penguin_generator(month):
    func = getattr(name_generator.penguin_name, "user_penguin")
    result = func(month)
    return result

if __name__ == "__main__":
    run()