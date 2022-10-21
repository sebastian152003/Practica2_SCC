import re
texto = input("ingrese un texto: ")

pat1 = re.sub(r"[0-6-8-9]", " " , texto)
pat2 = re.sub(r"[^\w+\¿?_]","", pat1)
pat3 = re.sub(r"\s+","",pat2)
print(pat3)