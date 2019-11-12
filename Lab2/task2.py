import re

def int_valid (prompt):
	a = input (prompt)
	while not bool (re.match(r'[0-9](\d+)?\Z', a)):
		print ("Необхідно ввести натуральне число")
		a = input (prompt)
	return (int(a))

print("Корнієнко Т.С.\n Лабораторна робота 2\n Варіант13\n2.2   Організація циклу за допомогою оператора while\n ")

x = int_valid("Введіть значення:")

canBeDivided = False

while x > 1:
    x /= 3
    if x == 1:
        canBeDivided = True

if( canBeDivided ):
    print(True)
else:
    print(False)
