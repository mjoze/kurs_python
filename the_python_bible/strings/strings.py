# name = 'Mark'
# print(type(name))
# hello = 'Hello world'
# print(hello)

# ask user for name
name = input("What is your name?: ")
# print(name)
# ask user for age
age = input("How old are you?")
# print(type(age))
# ask user for city
city = input("What city do you live in?: ")
# ask user what they enjoy
love = input("What do you love doing")
# create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, love)
# print output to screen
print(output)