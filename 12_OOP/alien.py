import random


class Player:
    """ Gracz w grze strzelance. """

    def blast(self, enemy):
        shoot = random.randint(1, 10)
        print("Wróg ma 3 punkty życia")
        print('Gracz razi wroga trafiając: {}\n'.format(shoot))
        if shoot >= 3:
            enemy.die()
        else:
            enemy.win()


class Alien:
    """ Obcy w grze strzelance. """

    def win(self):
        print('Alien mlaska na zakończenie i idzie spać')

    def die(self):
        print('Obcy z trudem łapie oddech, "To już koniec. Ale prawdziwie wielki koniec... \n',
              'Walczyliśmy do końca. Nie, to nie koniec. Larwy moje jednoczcie się! \n',
              'O tak one pomszczą mnie pewnego dnia... \n',
              'Żegnaj, okrutny Wszechświecie! Umieeeraaam"')


if __name__ == '__main__':
    hero = Player()
    invader = Alien()
    print('************ Śmierć Obcego ************\n')
    hero.blast(invader)
    input('\n\nAby zakończyć program, naciśnij klawisz Enter.')
