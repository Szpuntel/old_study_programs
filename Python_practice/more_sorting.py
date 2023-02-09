#sprawdz czy liczby podzielne sa przez 3 jezeli tak to je wyswietl
#po czym przenies je do odzelnej listy i przesortuj je


Liczby = [233,232,233,21,76,46,251,250,300,666,234,297,222,111,6934,233,34,124]
liczby2 = []
for liczba in Liczby:
    if liczba % 3 == 0:
        print(liczba)
        liczby2.append(liczba)
print(sorted(liczby2))
