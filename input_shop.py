# Exercice 2 Shopping Cart Program

item = input("Enter the item you want to buy :")
price = float(input("Enter the price of the item :"))
quantity = int(input("Enter the quantity of the item :"))
total = price * quantity

print(f"Your {quantity} {item}(s) will cost you {total} euros.")