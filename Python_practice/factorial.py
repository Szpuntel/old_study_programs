def func(x):
    fact = 1
    for x in range (1, x+1):
        fact = fact * x
    print(fact)

func(10)



def factorial(x):   # Obliczania silni za pomocą rekurencji 
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(10))