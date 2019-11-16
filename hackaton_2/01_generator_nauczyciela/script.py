import csv
import random


def open_csv_file(file):
    with open(file + '.csv', 'r') as f:
        reader = csv.reader(f)
        students = list(reader)
    return students


def create_students_dict(lista):
    students = {}
    for element in lista:
        students[element[0] + element[1] + element[2]] = [element[1], element[2], element[3], element[4]]
    return students


def view_class(students):
    for v in students.values():
        print('-'.join(v))


def search_name(name, students):
    lista = []
    for key, value in students.items():
        if name in key:
            lista.append(value)
    print(lista)
    return lista


def search_grade(grade, students):
    lista = []
    for key, value in students.items():
        if value[3] == grade:
            lista.append(value)
    print(lista)
    return lista


def search_task(task, students):
    lista = []
    for key, value in students.items():
        if value[2] == task:
            lista.append(value)
    print(lista)
    return lista


def prepare_group_mail(your_choice):
    if your_choice == 's':
        new_name = input("Give me the name you're looking for:")
        if new_name == '':
            print("Error")
        generate_searching = search_name(new_name, students_list)
        return generate_searching
    if your_choice == 'o':
        new_grade = input("Enter the grades you are looking for:")
        if new_grade == '':
            print("Error")
        generate_searching = search_grade(new_grade, students_list)
        return generate_searching
    if your_choice == 'z':
        new_task = input("enter the number of tasks you are looking for")
        if new_task == '':
            print("Error")
        generate_searching = search_task(new_task, students_list)
        return generate_searching


def send_message(students, message):
    names = []
    tasks = []
    grades = []
    mail = []
    for iterate in students:
        names.append(iterate[0])
        tasks.append(iterate[2])
        grades.append(iterate[3])
    for name, task, grade in zip(names, tasks, grades):
        mail.append(message.format(name, task, grade, int(grade) + 1))
    save = str(random.randrange(1, 100))
    with open(save + '.txt', 'w') as f:
        f.write('\n'.join(mail))


def select_message(message):
    with open(message, 'r') as f:
        message_txt = f.readlines()
        message_txt = ''.join(message_txt)
    return message_txt


if __name__ == "__main__":
    message_new = 'message.txt'
    selected_message = select_message(message_new)
    files = ['3a', '3b']
    print("Available classes:")
    for classes in files:
        print(classes)
    try:
        file1 = input("Select file")
        open_class_file = open_csv_file(file1)
        students_list = create_students_dict(open_class_file)
        view_class(students_list)
        print("Look for: student -- S, grades -- O, or tasks -- Z")
        your_choice_ = input("").lower()
        try:
            generate_new_search = prepare_group_mail(your_choice_)
            send_message(generate_new_search, selected_message)
        except Exception as e:
            print('Error', e)
    except FileNotFoundError as fn:
        print("Error", fn)


else:
    print('The file was imported as a module')