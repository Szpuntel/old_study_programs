
# operator walrus czyli ' := ' pozwala przypisać wartość zmiennej jako część wiekszego wyrażenia

#happy = True
#print (happy)   # <--- Mozna zapisać jak linie poniżej

#print (happy := True)   # <-- Dzięki niemu mozemy zapisać kod dużo ktocej


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# foods = list()                  <-- Cały ten kod zapisany za pomoca larger expression z uzuciem := ponieżej
# while True:
#     food = input('What food do you like? ')   
#     if food == 'exit':
#          break
#     else:
#         foods.append(food)

foods = list()
while food := input('What food do you like? ') != 'exit':
    foods.append(food)