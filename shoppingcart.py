foods = []
prices = []
total = 100



while True:
	food = input("Enter a food to buy(q to quit):")
	if food.lower() == "":
		break
	else:
		price = input("Enter a price of a food:")
		foods.append(food)
		prices.append(price)


print ("***** Your Cart")

for food in foods:
	print (food,end=" ") #horizontally listing foods


for price in prices:
	total+=price

print (f"your total is: ${total}")