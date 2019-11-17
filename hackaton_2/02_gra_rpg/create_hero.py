import random
import name_generator as ig


def create_hero():
    n = int(input("z ilu liter zbudować imię"))
    name = ig.generate_name(n)
    person = {'name': '',
              'character type': [],
              'equipment': [],
              'money': 100,
              'health': 100,
              'stamina': 100
              }
    sex = ['male', 'female']
    race = ['human', 'dwarf', 'elf']
    equipment = ['sword', 'shovel', 'axe', 'bow', 'bow', 'shield', 'helmet', 'armour', 'wand', 'hammer']
    player = []
    player_equipment = []
    for i in sex:
        print(i)
    select_sex = input("Wybierz płeć")
    player.append(select_sex)
    for i in race:
        print(i)
    select_race = input("wybierz rasę")
    player.append(select_race)
    for i in range(4):
        player_equipment.append(random.choice(equipment))
    person['character type'] = player
    person['equipment'] = player_equipment
    person['name'] = name
    return person


hero = create_hero()
print(hero)