import random


a = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
b = ['e', 'y', 'o', 'i', 'a', 'u']
new_nick = []
nickname = ['Niski', 'Wielki', "Waleczny", "Kulawy", "Okrągły", "Czeski", "Brudny", "Cichy"]


def generate_name(n):
    for i in range(n):
        if i % 2 == 0:
            new_nick.append(random.choice(a))
        else:
            new_nick.append(random.choice(b))
    nick = random.choice(nickname)
    name =''.join(new_nick).capitalize() + " " + nick
    return name

#
# print("Create new nickname")
# numbers = int(input("enter the number of characters"))
# a = generate_name(numbers)
# print(a)