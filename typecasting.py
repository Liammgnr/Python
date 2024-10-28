# Typecasting = conversion d'un type de données en un autre chaîne de caractère en entier,
# entier en chaîne, chaîne en flottant, float en chaîne ...

name = "Liammgnr"
age = 17
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa) # Convertis le nombre flottant 3.2 en nombre entier 3
print(gpa)

#age = float(age)
#print(age)

age = str(age)
print(age)
print(type(age))

#age += 1 Erreur 'cause its switch to str
age += "1" # because its an str , it cocatene 17 and 1 so 171

print(age)

name = bool(name)
print(name) # return true 'cause name isnt empty