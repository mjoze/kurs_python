from units.knight import Knight
from units.archer import Archer


def main():
    k = Knight()
    k.attack()
    print(k)

    a = Archer()
    a.attack()
    print(a)


if __name__ == '__main__':
    main()