class ty:
	def __init__(self, number, name):
		self.number = number
		self.name = name
a = ty(5*8, "Idowu")
b = getattr(a, 'name')
print(b)

#<strong>Output:strong>Idowu