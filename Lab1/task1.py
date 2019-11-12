import re

def validator (prompt):
	date = input(prompt)
	if not bool (re.match(r'((([0]?[1-9])|([1-2][0-9]))\.(([0][1-9])|([1][0-2])))|([3][0]\.(([0][13456789)|([1][0-2])))|([3][1]\.(([0][13578])|([1][02])))\Z', date)):
		print ("Не дата")
	else: print ("Дата вірна")
		
date = validator ("Введіть дату: ")
