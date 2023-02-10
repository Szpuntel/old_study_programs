class Text:
    list = []
    def dodaj(self, args):
        self.list.append(args)

    def zdejmij(self):
        if len(self.list) > 0:
            return self.list.pop(len(self.list) - 1)
        else:
            return

obj = Text()
obj.dodaj =('A')
obj.dodaj =('B')

print(obj.list)