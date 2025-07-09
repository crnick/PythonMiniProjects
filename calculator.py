

operator = input ("Enter an operator (+ - * /): ")
num1 = float(input ("Enter the 1st number: "))
num2 = float(input ("Enter the 2nd number: "))

def handleOperations():
	if operator == "+":
		result = num1 + num2 
		print(round(result),3)
	elif operator == "-":
		result = num1 - num2 
		print(round(result),3)
	elif operator == "*":
		result = num1 * num2
		print(round(result),3)
	elif operator == "/":
		result = num1 / num2
		print(round(result),3)
	else:
		print(f"{operator} is not a valid operator")

if __name__ == "__main__":
	handleOperations()