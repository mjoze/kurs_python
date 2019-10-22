""" Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą,
MasterCard, a może AmericanExpress.

Co wiemy o tych numerach tych kart?

All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.

MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720.
All have 16 digits.

American Express card numbers start with 34 or 37 and have 15 digits."""


def check_card(number):
    number_card = str(number)
    number_card_list = [int(i) for i in str(number)]
    print(number_card_list)
    if number_card_list[0] == 4 and len(number_card_list) >= 13:
        print("visa")
    elif (int(number_card[0:2]) in range(51, 55) or int(number_card[0:5]) in range(2221, 2720)) \
            and len(number_card_list) == 16:
        print('mc')
    elif (int(number_card[0:2]) == 34 or 37) and len(number_card_list) == 15:
        print('ae')
    else:
        print('zły numer karty')


check_card(3422211111111111)


