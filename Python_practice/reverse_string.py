from functools import reduce

string = 'Major Suchodolski Lubi Nitro'
list = string.split()
list.reverse()

def add_str(a, b):
    
    return a + ' ' + b

sol = ' '.join(list)

print(reduce(add_str, list))
print(sol)