# def example_function():
#
#     def nested_function():
#         print('Jestem w srodku zagnieżdżenia')
#
#     return nested_function
#
#
# new_function = example_function()
#
# new_function()


def sound_decorator(func_as_param):
    def hau_nested():
        print('Hau ~ hau')
        func_as_param()
    return hau_nested


def pet_func():
    print('Pies to najlepszy przyjaciel człowieka')


pet_func()
# print('--------------')
# dog = sound_decorator(pet_func)
# dog()

