#weight calculator 


weight = float(input ("Enter your weight "))
unit = input ("kilograms or Pounds? (K or L):  ")

if unit == "k":
	weight = weight * 2.205
	unit = "Lbs."
	print (f"Your weight is: {round(weight,1)} {unit}")
elif unit == "L":
	weight = weight / 2.205 #convert to kilograms.
	unit = "kgs."
	print (f"Your weight is: {round(weight,1)} {unit}")
else:
	print (f"{unit} was not valid")



#temperature conversions
unit = input ("Enter temperature in Celcius or Fahrenheit (C/F): ")
temp =  float(input ("Enter the temperature:  "))

if unit == "C":
	temp = round((9*temp) /5 +32,1)
elif unit == "F":
	temp = round((temp - 32) * 5 /9,1)
else:
	print (f"{unit} was not valid")


