
def upper(text):
    return text.upper()

def lower(text):
    return text.lower()

def higer_function(func, text):
    text = func(text)
    print(text)

a = input("podej no text ktory chcesz powiekrzc i pomniejszyc byczq")

higer_function(upper, a)
higer_function(lower, a)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(5)
print(divide(55))