"Pig Latin Translator"

original = input("Please enter a sentence: ").strip().lower()
words = original.split()
new_words = []
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vovel_pos = 0
        for letter in word:
            if letter not in "aieou":
                vowel_pos = vovel_pos + 1
            else:
                break
        cons = word[:vovel_pos]
        the_rest = word[vovel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
output = ' '.join(new_words)
print(output)