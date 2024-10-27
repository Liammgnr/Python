# Variable = Un conteneur pour une valeur (chaîne, entier, flottant, booléen)
#            Une variable se comporte comme si i était la valeur qu'elle contient
first_name = "Liam"
food = "Lasagna"
email = "liam.mgnr@outlook.com"

# Chaine de caractère
print("-"*30 , "# Chaine de caractère")
print()
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

print()
print("-"*30 , "# Entiers")
print()

# Entiers
age = 17
quantity = 3
num_of_students = 30

print(f"You are {age} years old.")
print(f"You are buying {quantity} items")
print(f"Your class have {num_of_students} students")

print()
print("-"*30 , "# Flottant")
print()

# flottant

price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is {price}€")
print(f"Your gpa is : {gpa}")
print(f"You ran {distance}km")

print()
print("-"*30 , "# Booléen")
print()

# Booléen

is_student = True
for_sale = False
is_online = True

if is_student :
    print("You are a student")
else :
    print("Your are NOT a student")

print(f"Are you a student? : {is_student}")

if for_sale :
    print("This item is for sale")
else :
    print("This item is NOT available")

if is_online :
    print("You are online")
else :
    print("You are not online")



