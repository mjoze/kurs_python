"""What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and
an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []"""


def anagrams(word, words):
    word1 = []
    word2 = []
    results = []
    for i in word:
        word1.append(i)
    word1.sort()
    counter = 0
    while True:
        for i in words[counter]:
            word2.append(i)
        word2.sort()
        if word1 == word2:
            results.append(words[counter])
        counter += 1
        word2 = []
        if counter == len(words):
            return results


"Clever"
# def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]