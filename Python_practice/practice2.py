
#Zadanie: Wyświetl liczby od 1 do 20
#ale jezeli liczba jest parzysta wyswietl słowo parzysta

liczba = 0
while liczba < 20:
    liczba += 1
    if liczba % 2 == 1:
        print(liczba)
        
    else:
        print("parzysta")
