list = [10, 20, 28, 38, 40]
if all ([i % 2 == 0 for i in list]):
    print("Wszystkie parzyste")

if any([i % 2 == 1 for i in list]):
    print("Przynajmniej jeden jest parzysty")

for i  in enumerate(list): # Krotki 
    print(i[0]+1,"-", i[1])