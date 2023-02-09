slowo = input("podaj słowo: ")
if slowo[0] == slowo[len(slowo)-1] and slowo[1] == slowo[len(slowo)-2]:
    print("tak jest palindromem")
else:
    print("nie jest palindromem")
    