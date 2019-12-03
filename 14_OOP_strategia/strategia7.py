from units.archer import Archer
from units.knight import Knight

archers = []

for _ in range(3):
    archers.append(Archer())

knights = []

for _ in range(4):
    knights.append(Knight())

army = archers + knights
print(army)

for warrior in army:
    warrior.attack()

print(army)

