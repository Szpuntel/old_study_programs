# collections : Counter, nametuple, OrderedDict, defaultdict, deque

from collections import Counter

a = "aaaavvvvccc"
my_counter = Counter(a) # zlicza wartości i je wyświetla
print (my_counter)
print (my_counter.values()) # zliczba wartości i wywietla same wartości 
print (my_counter.keys()) # wyświetla klucze w tym przypdku 'a' 'v' 'c'
print (my_counter.most_common(1)) #wyswietla najczesciej wystepujący klucz 


