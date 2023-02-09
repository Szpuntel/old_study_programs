# Filter nie wykonuj działań tylko sprawdza warunek i zwraca wartości true do nowej listy.

numbers = [2, 10, 12, 15, 20, 25, 30, 35]

age = lambda x:True if x > 18 else False  # <-- lambda ktora przypisuje true do licz wiekszych niz 18 do mniejszych false
resoult = filter(age, numbers) # <-- filter sprawdza warunek i wyswietla tylko elemnty ktore dostały True

print(list(resoult))   #<-- Zwracamy wynik hjnnjmnnnnnnnnnnnnn cv