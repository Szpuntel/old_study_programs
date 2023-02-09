#Yield Generuje wyniki na bierzaco i continue dalsze wykonywanie programu

def gen():
    i = 0
    while i < 5:
        yield i
        i += 1

for i in gen():
    print(i)

print(list(gen()))

def gen2(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1

for i in gen2(25):
    print (i)

print(list(gen2(30)))