
#prints the current balance
def showBalance(balance):
	print(f"Your balance is{balance:.2f}")

def deposit():
	amount = float(input ("Enter the amount to be deposited"))
	if amount < 0;
		print("Not a valid amount")
		return 0
	else:
		return amount


def withdraw(balance):
	amount = float(input ("Enter the amount to be withdrawn"))
	if amount > balance:
		print("Insufficient funds")
		return 0
	elif amount < 0:
		print ("Amount cannot be negative")
		return 0
	else:
		return amount


def main():
	balance = 0;
	is_running = True


	while is_running:
		print("Banking program");
		print("1. Show Balance");
		print("2. Depost")
		print("3. Withdraw")
		print("4. Exit")

		choice = input ("Enter your choice")

		if choice == "1":
			showBalance(balance)
		elif choice == "2":
			amount = deposit()
			balance += amount
		elif choice == "3":
			amount =withdraw(balance)
			balance -= amount
		elif choice == "4":
			is_running = False;
		else:
			print("Enter a valid choice")

if __name__ == "__main__":
	main()