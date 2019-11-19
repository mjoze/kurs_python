"""Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki.
Utwórz dowolne atrybuty i metody. Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.
Utwórz kilka storczyków z różnymi parametrami."""


class Storczyk:
    krolestwo = "roślin"

    def __init__(self, kolor, kwitnienie, gatunek):
        self.kolor = kolor
        self.kwitnienie = kwitnienie
        self.gatunek = gatunek


storczyk1 = Storczyk("biały", True, "blady")
storczyk2 = Storczyk("fioletowy", True, "błotny")
