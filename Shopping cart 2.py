items = []
prices = []
total = 0
while True:
    item = input("What item did you buy? (Just hit enter if you want to quit.):   ")
    if item == "":
        break
    else:
        price = float(input(f"What's the price of your {item}?:   "))
        items.append(item)
        prices.append(price)
print("---------------This your cart.-------------")
for item in items:
    print(item)
for price in prices:
    total += price

print(f"Your total charge is = {total}")