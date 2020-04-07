def bmi_calc(weight, height):
    try:
        return round(weight / (height ** 2), 3)
    except:
        print("tutaj")



def bmi_status(bmi):
    if bmi < 19:
        return "niedowaga"
    elif bmi < 25:
        return "waga normalna"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "otyłość"


def main():
    result = bmi_calc(100, 1.80)
    print(bmi_status(result))


if __name__ == "__main__":
    main()