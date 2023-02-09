# Python's replace() method lets you replace some parts of a string with another character.
# It's often handy in data science, especially during data cleaning.
# The replace() method accepts two parameters: the replaced character and the one you'll like to replace it with.

columns = ["Cart_name", "First_name", "Last_name"]
for i in columns:
	i = i.replace("_", " ")
	print(i)