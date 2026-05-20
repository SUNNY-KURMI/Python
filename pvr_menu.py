# Concession stand program

menu = {"pizza" :3.00,
        "nachos" : 4.50,
        "popcorn" : 6.00,
        "fries" : 2.50}

cart = []
total = 0

print("----------Menu----------")

for key, value in menu.items():
    print(f"{key:10} : {value:.2f}")

print("----------Cart----------")

food = input("Enter the food items(q for quit): ")

while True :
    food = input("Enter the food items(q for quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print("------  Your Order  ------")
for food in cart :
    total += menu.get(food)
    print(food , end=" ")

print()
print(f"Total is: ${total:.2f}")