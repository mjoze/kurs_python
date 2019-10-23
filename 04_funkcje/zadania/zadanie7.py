""" Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą,
MasterCard, a może AmericanExpress.
Co wiemy o tych numerach tych kart?
All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720.
All have 16 digits.
American Express card numbers start with 34 or 37 and have 15 digits."""

# def check_card(number):
#     number_card = str(number)
#     # number_card_list = [int(i) for i in str(number)]
#
#     if int(number_card[0]) == 4 and len(number_card) >= 13:
#         print("visa")
#     elif (int(number_card[0:2]) in range(51, 56) or int(number_card[0:5]) in range(2221, 2721)) \
#             and len(number_card) == 16:
#         print('mc')
#     elif (int(number_card[0:2]) == 34 or 37) and len(number_card) == 15:
#         print('ae')
#     else:
#         print('zły numer karty')
#

v = 4195905348577260
mc = 5372077848173651
ae = 349799046528565


def is_visa(is_card, number):
    if not is_card:
        return False
    if len(number) == 16 or len(number) == 13:
        if number[0] == '4':
            return True


def is_mastercard(is_card, number):
    if not is_card:
        return False
    if len(number) == 16:
        if int(number[0:2]) in range(51, 56) or int(number[0:4]) in range(2221, 2721):
            return True


def is_american_express(is_card, number):
    if not is_card:
        return False
    if len(number) == 15:
        if number[0:2] in ("34", "37"):
            return True


can_be_card_number = False
card_number = input("Put your card number here: ")
if len(card_number) < 13 or len(card_number) > 16:
    print("wrong number")
else:
    if card_number.isdecimal():
        print("Can be card number")
        can_be_card_number = True
    else:
        print("Not a number")

if is_visa(can_be_card_number, card_number):
    print("I'm visa")
elif is_mastercard(can_be_card_number, card_number):
    print("I'm master card")
elif is_american_express(can_be_card_number, card_number):
    print("I'm american express")
else:
    print("Not known card type")
