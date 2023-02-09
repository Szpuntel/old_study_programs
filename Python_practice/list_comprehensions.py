# list comprehension to sposób tworzenia nowej listy z mniejsza ilośćia znaków
# moze odwzorowywać funkcje lambda, łatwiejsza do czytania list = [expression for item in iterable]

square = []              # tworzy pustą liste
for i in range(1, 11):   # tworzy pętle 
    square.append(i*i)   # definiuje co powinno sie dziać przy kazdym obrocie
#print (square)           # no chyba wiadomo



squares2 =[i * i for i in range(1, 11)] # <-- ten sam program co powyżej 
#print (squares2)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`

students = [100,90,80,70,60,50,40,30] 

resoult = list(filter(lambda x:True if x > 60 else False, students)) # list() zeby wyniki były podane w liscie
                                                                     # filter() aby moc przefiltrowac wyniki za pomocą funkcji
                                                                  # lambda x: aby moc zdefiniować warunek jaki nas interesuj
resoult2 = [i if i >= 60 else "Failed" for i in students]

print(resoult2 )