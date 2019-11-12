import math
import re
def validator (prompt):
	x=input(prompt)
	while not bool (re.match(r'(?:[0]\.\d+)|(?:[1-9](?:\d+)?(?:\.\d+)?)\Z', x)):
		print ("Неправильний формат")
		x=input(prompt)
	return x
print("КорнієнкоТ.С.\nЛабораторна робота№1\nВаріант 13 \nВикористання математичних формул за виконанням певних умов.\n")
x=validator("Введіть значення Х: ")
print("x = "+x)
x=float(x)
if x>3:
    print("-3*x+9 ="+str(-3*x+9))
else:
    print("x^3/(x^2+8) = "+str((x*x*x)/(x*x+8)))


