""" Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych. Sprawdź dla każdej kart jej typ.
Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt."""


def is_visa(number):
    if len(number) == 16 or len(number) == 13:
        if number[0] == '4':
            return True


def is_mastercard(number):
    if len(number) == 16:
        if int(number[0:2]) in range(51, 56) or int(number[0:4]) in range(2221, 2721):
            return True


def is_american_express(number):
    if len(number) == 15:
        if number[0:2] in ("34", "37"):
            return True


with open('card.txt') as f:
    content = f.read()


card_numbers = content.split()

visa = []
mastercard = []
american_express = []
for card_number in card_numbers:
    if is_visa(card_number):
        visa.append(card_number)
    elif is_mastercard(card_number):
        mastercard.append(card_number)
    elif is_american_express(card_number):
        american_express.append(card_number)
    else:
        print("Not known card type")

with open('visa.txt', 'w') as f:
    f.write('\n'.join(visa))
with open('mastercard.txt', 'w') as f:
    f.write('\n'.join(mastercard))
with open('american_express.txt', 'w') as f:
    f.write('\n'.join(american_express))