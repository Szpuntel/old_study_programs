class Test:
    def __del__(self):
        print("Bye class")
    
obj = Test()
obj2 = obj
list = [obj2]
del obj
del obj2
del list[0]

print("The end")

