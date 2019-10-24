""" Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji."""
# loss : win
rules = {
    'n':  'k',
    'k': 'p',
    'p': 'n',
}

print(rules.keys())
def declareWinner(user, ai):
    if user == ai:
        print("remis")
    elif user in rules.keys() and ai in rules.values():
        print("ai win")
    else:
        print("user win")

declareWinner('n', 'n')