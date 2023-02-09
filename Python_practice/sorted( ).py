f = {1, 4, 9, 3} # Try it on a set

sort = {"G":8, "A":5, "B":9, "F":3} # Try it on a dictionary

#print(sorted(f, reverse=True)) # Descending

#print(sorted(sort.values())) # Ascending (default)

students = [("Sebastian", "F", 60),       #<-- row 1   <--- LISTA
            ("Patrick", "D", 20),       #<-- row 2
            ("Bobby", "F", 48),          #<-- row 3 
            ("Ludwiq", "G", 89)]        #<-- row 4
#               ^       ^   ^
#               |       |   |
#         column1 column2 column3

grade = lambda grade: grade[1]  # <-- przypisanie grade drugiej kolumny

students.sort(key=grade)    # <-- teraz mozemy sortowac za pomocą grade

for i in students:
    print(i)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print()

students2 = (("Sebastian", "F", 60),       #<-- row 1   <--- KROTKA
            ("Patrick", "D", 20),       #<-- row 2
            ("Bobby", "F", 48),          #<-- row 3 
            ("Ludwiq", "G", 89))        #<-- row 4
#               ^       ^   ^
#               |       |   |
#         column1 column2 column3

age = lambda ages: ages[2]
sorted_studens2 = sorted(students, key = age)

for i in sorted_studens2:
    print(i)
