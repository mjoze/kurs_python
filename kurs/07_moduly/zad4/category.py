import json


def choose_category():
    with open('words.json', encoding='utf-8') as f:
        data = json.load(f)
    print('Available categories:')
    for key in data:
        print('--' + key)
    category = input('Select')
    if category in data.keys():
        _words = []
        for key, values in data.items():
            if key == category:
                _words.append(' '.join(values).split())
        _words = _words[0]
        return _words
    else:
        print("You have chosen the wrong category name. Try again")
        return choose_category()
