# lamda to funkcja napisana w jednej lini aktcptuje jakąkolwiek liczbe rgumentów
# ale ma tylko jedno wyrażenie (jest to tak jakby skórt funkcji zamiast jej pisanie)
# uzyteczna jezeli uzywamy ja przez ktortki okres czasu.


# def double(x):      <--- funkcja
#     return x * 2
# print(double(5))

double = lambda x:x *2             # <--- skrócona funkcja z uzyciem lambdy
#print(double(5))


multiplay = lambda x, y: x * y
#print(multiplay(8,8))

fullname = lambda first_name, last_name: first_name + ' ' + last_name
#print(fullname('Rafal','Bobaski'))

age_check = lambda age:True if age > 18 else False
# print(age_check(4))



def function(f, number):
    return f(number)

# print(function(lambda x: x * x,  3))

# def kwadrat(x):
#     return x * x

# print(kwadrat(5))

# wyn = (lambda x: x*x)(5)
# print(wyn)


# lam = lambda x: x*x
# print(lam(5))
# print(lam(76))

# lam2 = lambda x, y: x*y
# print (lam2(2, 5))

# print((lambda x,y: x*y)(5,7))