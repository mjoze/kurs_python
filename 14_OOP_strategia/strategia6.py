from units.knight import Knight


knights = []

for _ in range(4):
    knights.append(Knight())

# print(knights)

for knight in knights:
    knight.walk(2000)

knights.append(Knight())

for knight in knights:
    knight.attack()

print(knights)
