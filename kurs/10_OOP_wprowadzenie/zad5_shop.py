""" Utwórz klasę sklep. Sklep posiada różne produkty. W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic."""


class Shop:
    def __init__(self, products_dict):
        self.products = products_dict

    def show_products(self):
        for key, value in self.products.items():
            print("Index:", key, "Nazwa produktu:", value[0], "Cena:", value[1], "Ilość sztuk:", value[2])

    def trying(self, product_choice):
        for key, value in self.products.items():
            if product_choice == value[0]:
                print(value)
                return value

    def buy(self, product_choice):
        for key, value in self.products.items():
            if product_choice == value[0]:
                value[2] -= 1
                print(value)
                return value

    def return_product(self, product_choice):
        for key, value in self.products.items():
            if product_choice == value[0]:
                value[2] += 1
                print(value)
                return value


sklep = {
    1: ["kalosz", 23, 2],
    2: ["gumowce", 24, 3],
    3: ["walonki", 1020, 1]
        }

new_s = Shop(sklep)
a = new_s.return_product("walonki")
