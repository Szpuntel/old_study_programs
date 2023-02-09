import sys


no_of_tries = 5
word = input("Podaj Słowo do odgadywwania: ")

used_letters = []
user_word = []


def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

for _ in word:
    user_word.append("_")

while True:
    letter = input("Podaj Litere: ")
    used_letters.append(letter)
    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("nie ma takiej litery")
        no_of_tries -= 1
        print("Pozostało prób", no_of_tries)

        if no_of_tries == 0:
            print("Koniec gry byczq")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter
        print(user_word)

        if "".join(user_word) == word:
            print("Brawo to jest to słowo")
            sys.exit(0)

    print("Użyte litery:", used_letters)