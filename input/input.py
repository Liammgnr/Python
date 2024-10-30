# Input() = Une fonction qui invite l'utilisateur à saisir des données
#           Renvoie les données saisies sous forme de chaîne de caractères

#input("What is your name? :")

name = input("What is your name? :")
age = input("How old are you ? :")

# age = age + 1 retourne une erreur car age est une chaîne de caractères
#               on ne peut pas concaténer une chaîne de caractères et un entier donc :

age = int(age) # Convertis la chaîne de caractères en entier
age = age + 1 # Ajoute 1 à l'entier

# ou sinon on peut faire ( qui est plus simple et court ) :

age2 = int(input("How old are you ? :"))
age2 = age2 + 1
print(f"You are {age2} years old.")

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old.")