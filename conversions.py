#weight calculator 


weight = float(input ("Enter your weight "))
unit = input ("kilograms or Pounds? (K or L):  ")

if unit == "k":
	weight = weight * 2.205
	unit = "Lbs."
elif unit == "L":
	weight = weight / 2.205 #convert to kilograms.
	unit = "kgs."
else:
	print (f"{unit} was not valid")

print (f"Your weight is: {weight} {unit}")