def longest_sequence(var):
    max_count = 1
    count = 1
    txt = []
    max_txt = []
    for i in range(len(var)-1):
        if var[i] == var[i+1]:
            txt.append(var[i])
            count += 1
        else:
            count = 1
            txt = []
        if count > max_count:
            max_count = count
            if len(txt) > len(max_txt):
                max_txt = txt
    max_txt.append(max_txt[0])
    a = ''.join(max_txt)
    return a, max_count


if __name__ == "__main__":
    print('funkcja do wyszukiwania najdłuższej sekwencji')
