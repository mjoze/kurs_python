"""Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą łańcuch znaków i
zwracający ten sam tekst zmieniony na wielkie litery.
Utwórz funkcję zwracającą tekst
Utwórz dekorator przyjujący tę funkcję
Wywołaj funkcję, by sprawdzić, że decorator działa"""


def uppercase_decorator(func_txt):
    def upper_txt():
        txt = str(func_txt())
        return txt.upper()
    return upper_txt


@uppercase_decorator
def text():
    return "abrakadabra"


print(text())
