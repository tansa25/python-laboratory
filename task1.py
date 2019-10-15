if1 <= month <= 12:
if month == 2:
if 1 <= day <= 28: #в невисокосний рік в лютому 28 днів
return True
else:
return False

elif month == 4 or month == 6 or month == 9 or month == 11: #місяці з 30 днями
if 1 <= day <= 30:
return True
else:
return False
else: # місяці з 31 днями
if 1 <= day <= 31:
return True
else:
return False
else:
return False

#------------------------------------------------------------------------------- 

## end off def date(...) 
##------------------------------------------------------------------------------------------------

## Вводимо дату :

den = int(input(" Ввести число дня : "))
mesyac = int(input(" Ввести число місяця : "))
god = 2019

YesNo = date(den,mesyac)

if YesNo :
print(" Дата вірна !")
else :
print("Дата НЕКОРРЕКТНА ... ???")



