# reduce wykonuje funkcje na dwóch pierwszych elementach i powtarza proces
# dopóki nie doda ostatniego elementu np. dodawanie tablicy
# ['H', 'W', 'D', 'P']   dodaje pierwsze dwa elemnty wiec
# ['HW', 'D', 'P'] wykonuje sie nadal wiec
# ['HWD','P'] i ostatni raz
# ['HWDP']


# Funkcja w tym przypadku dodaje do siebie elementy tworzać jedno słowo

import functools
import re

letters = ["H", "I", "O", "P", "Q", "R", "S"]
word = functools.reduce(lambda x,y : x+y , letters)

print (word)

# Przykład z silnią gdzie mnozy elemnty

factorial = [5,4,3,2,1]

resoult = functools.reduce(lambda x,y : x * y , factorial)

print (resoult)

