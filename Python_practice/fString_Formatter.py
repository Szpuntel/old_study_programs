# FORMATOWANIE CIAGOW STRING
name = "booby"
age = 17
args = ['Jacobi', 25]


text = 'Hi my name is {0} and i have {1} years'.format(args[0], args[1]) 

text1 = "Hey my name is %s and i would like to know that im %i years old" % (name, age)

text2 = f"Hey my name is {name} and im {age} years old"

text3 = f"multipling 5x86 in string, whichi is:{5*86}."

print (text)
print (text1)
print (text2)
print (text3)

# Przypisanie nazwy
# text = 'Hi my name is {name} and i have {years} years'.format(name = args[0], years = args[1])