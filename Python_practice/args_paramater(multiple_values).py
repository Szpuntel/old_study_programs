# *args = parametr który zapakuje argumenty do tumple.
# spoko ponuiewaz funkcja moze obsłóżyć różna liczbe argumentów.

# def add(num1,num2):
#     sum = num1+num2
#     return sum

# print(add(2,5))

def add(*args): # <--- Nie musi być *args. Wazne żeby przed nazwą była '*'
    sum = 0
    args = list(args) #<-- Zamiana tuple czyli listy w której nie mozna zmieniać ani dodawać zmiennych, na liste ktora mozna modyfikować.
    for i in args:
        sum += i
    return sum


print(add(5,6,8,4,3,6,8,5,5))
print(add(5,3,6,8,5,5))

