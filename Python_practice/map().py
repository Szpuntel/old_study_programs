from math import ceil

numbers = [2, 10, 12, 15, 20, 25, 30, 35]

# Mapa Kazdy argumnt po kolei wykonuje funkcje wskazana w pierwszym argumncie.

def function(x):
    return x * 2

resoult = map(function, numbers)

print(list(resoult))

# (Moze to też być funkcja anonimowa w postaci lambdy

resoult2 = map(lambda x: x * 2, numbers)

print(list(resoult2))

# Kolejny przykład

store = [("shirt", 20),
         ("pants", 150),
         ("hat", 40),
         ("shoes", 350),]

to_dollars = lambda data: (data[0], ceil(data[1] / 4.65))
to_russian_rubles = lambda data: (data[0], ceil(data[1] * 14))

store_dolla = list(map(to_dollars, store))
to_russian_rubles = list(map(to_russian_rubles, store))

for i in to_russian_rubles:
    print(i)
