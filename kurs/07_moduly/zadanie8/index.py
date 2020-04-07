import script

if __name__ == "__main__":
    try:
        number = int(input("podaj liczbę do ciągu fibonnaciego"))
        a = script.fibonnaci(number)
        print(a)
    except:
        print("błędna wartość")