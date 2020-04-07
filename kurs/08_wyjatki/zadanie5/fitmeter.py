import bmi


while True:
    try:
        w = float(input("Give me your weight [kg]: "))
        break
    except:
        print(" value in the wrong format")

while True:
    try:
        h = float(input("Give me your height [m]: "))
        break
    except:
        print(" value in the wrong format")

bmi_result = bmi.bmi_calc(w, h)
bmi_stan = bmi.bmi_status(bmi_result)
print(bmi_stan)


