# print(type(2))
# print(type(0.2))
import random
import math

health = 50
easy = 1
medium = 2
hard = 3
difficulty = easy
potion_health = int(random.randint(25, 50) / difficulty)
health = health + potion_health
print(health)

print(math.pi)
print(math.e)
print(math.floor(2.1))
print(math.ceil(2.1))
print(math.pow(2, 2))
print(2 ** 2)