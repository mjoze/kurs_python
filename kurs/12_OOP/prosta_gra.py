import game, random

print("Witaj w najprostszej grze na świecie!\n")
again = None
while again != "n":
    players = []
    num = game.ask_number(question="Podaj liczbę graczy (2 - 5):", low=2, high=5)
    for i in range(num):
        name = input("Nazwa gracza: ")
        score = random.randrange(100) + 1
        player = game.Player(name, score)
        players.append(player)

    print("\nOto wyniki gry:")
    for player in players:
        print(player)

    again = game.ask_yes_no("\nCzy chcesz zagrać ponownie? (t/n):")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
