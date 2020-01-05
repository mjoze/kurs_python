# print(type(2))
# print(type(0.2))
import random

health = 50
easy = 1
medium = 2
hard = 3
difficulty = easy
potion_health = int(random.randint(25, 50) / difficulty)
health = health + potion_health
print(health)
