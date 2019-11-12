def search_mail(lists, email):
    for i in lists:
        if i == email:
            print(email)
            return True
    return False


mail = input("podaj mail")
lista = ['mk', 'mj']
print(search_mail(lista, mail))

