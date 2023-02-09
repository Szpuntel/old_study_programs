numbers1 = {0, 1, 2, 3, 4}
numbers2 = {3,4,5,6}
words = set(['a', 'b', 'c'])

print(numbers1)
print(words)
s = 'k'
numbers1.add(s)
print(numbers1)

print (1 in numbers1)
print ('a' in numbers1)

print(numbers1 | numbers2) #sumuje wartosci
print(numbers1 & numbers2) #Wyswitla tylko wartosci powtarzajace sie w obu zbiorach
print(numbers1 - numbers2) # Usuwanie tych samych wartosci
print(numbers1 ^ numbers2) # Usuwanie wartosci powtarzajacych sie w obu zbiorach (różnica symetryczna)
