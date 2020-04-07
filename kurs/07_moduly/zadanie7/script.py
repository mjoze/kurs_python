import index

numb = []
for i in range(4):
    num = input('Enter the values from which you want to create a password')
    numb.append(num)
print(numb)


if __name__ == "__main__":
    x = index.numbers_generator(numb)
    password = ''.join(x)
    print(password)
