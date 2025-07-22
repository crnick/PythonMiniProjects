import time 

my_time = int (input("Enter the time in seconds: "))

if my_time <= 0:
    print("Time must be positive.")
else:
	for x in range(my_time,-1,-1): #count backwards
		seconds = x % 60
		minutes = int (x/60)%60
		hours = int (x / 3600)
		print(f"{hours:02}:{minutes:02}:{seconds:02}")
		time.sleep(1)


print("Time's up")
