donuts = {
    0: ["pączek wiśniowy", 100, 252],
    1: ["fit pączek gryczany ze śliwkami", 200, 205],
    2: ["pączek z czekoladą", 150, 315],
    3: ["pączek karmelowy-orzechowy", 100, 441],
    4: ["oreo donut", 150, 630],
    5: ["mini pączek z budyniem", 50, 126]
}
mass = 0
a = 0
for k, v in donuts.items():
    print(k, v[0], v[1], "[g]", v[2], "[kcal]")

while True:
    a = int(input("wybierz paczek"))
    for k, v in donuts.items():
        if a == k:
            mass += v[1]
            break
    print(mass)

