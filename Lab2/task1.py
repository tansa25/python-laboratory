import re

def int_valid (prompt):
	a = input (prompt)
	while not bool (re.match(r'[1-9](\d+)?\Z', a)):
		print ("Необхідно ввести натуральне число")
		a = input (prompt)
	return (int(a))
	
def float_valid (prompt):
	a = input (prompt)
	while not bool (re.match(r'(?:[0]\.\d+)|(?:[1-9](?:\d+)?(?:\.\d+)?)\Z', a)):
		print ("Необхідно ввести дійсне число")
		a = input (prompt)
	return (float(a))

print("Корнієнко Т.С.\n Лабораторна робота 2\n Варіант13\n Організація циклу за допомогою оператора for\n ")


x = float_valid("Введіть значення x ")
s = 0
n = int_valid("Введіть значення n ")

for i in range(n):
    s = s + (x+i)**2
print(s)
