
#Zadanie: Wyświetl liczby od 1 do 20
#ale jezeli liczba jest podzielna przez 3 napisz FIZZ jezeli przez
#5 to BUZZ jezeli przez 3 i 5 to FIZZBUZZ wyswietl

# for x in range (1,21):
#     if x % 3 == 0 and x % 5 == 0:
#         print("FIZZBUZZ")
#     elif x % 3 == 0:
#         print("FIZZ")
#     elif x % 5 == 0:
#         print("BUZZ")
#     else:
#         print(x)

def fizzBuzz(n):
        list = []
        for number in range (1,n):
            if number % 3 == 0 and number % 5 == 0:
                list.append("FizzBuzz")
            elif number % 3 == 0:
                list.append("Fizz")
            elif number % 5 == 0:
                list.append("Buzz")
            else:
                list.append(number)

        print(list)

fizzBuzz(155)

