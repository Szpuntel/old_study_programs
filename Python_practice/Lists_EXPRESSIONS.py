# WYRAŻENIA LISTOWERS

list = list(range(10))
print (list)

new = [i * 2 for i in list]
new2 = [i + 2 for i in list if i % 2 == 0]

print (new)
print (new2)