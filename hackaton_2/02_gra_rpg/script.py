"""Stwórz bohatera w którym:

Użytkownik może podać płeć wojownika, rasę oraz imię lub je wylosować z listy.
Generator imion bohatera powinen brać pod uwagę płeć bohatera oraz rasę i zwracać
wygenerowane imię zgodnie z założoną konwencją.
Generator imion powinen znajdować sie w oddzielnym module.
Bohater powinen mieć dostępny ekwipunek oraz 10 stopniowy poziom energii.
Sposób implamentacji dobierz na podstawie całości."""
import random
import name_generator as ig


def
n = int(input("z ilu liter zbudować imię"))
name = ig.generate_name(n)
person = {'name': '',
          'character type': [],
          'equipment': []
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
print(person)