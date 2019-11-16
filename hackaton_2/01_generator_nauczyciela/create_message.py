import csv


def create_message():
    with open('messages.csv', 'r', encoding='utf-8') as f:
        reader1 = csv.reader(f)
        txt = list(reader1)
    message = []
    length = 4
    while length > 0:
        print("treść nowej wiadomości", message)
        for item in range(len(txt)):
            print(item, ':', ''.join(txt[item]), end='** ')
        print()
        wybierz = int(input("treść wiadomości"))
        message.append(''.join(txt[wybierz]))
        message.append('{}')
        length -= 1
    return ' '.join(message)


new_message = create_message()
print(new_message)