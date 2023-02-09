import random

y = random.randint(1,12)
print("Zgadnij liczbe jaka wylosował komputer od 1 do 12")
while True:
    x = input("Podaj liczbe: ")
    if int(x) == y:
      print("Brawo Zgadłeś Liczbe ! Była nią:", y)
      break
    elif int(x) > y:
      print("Liczba jest mniejsza byczq")
    elif int(x) < y:
        print("Liczba jest wieksza byczq")