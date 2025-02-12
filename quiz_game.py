print ("welcome to the quiz game!")


user_answer = input("Do you want to play? ")

if user_answer.lower() != "yes":
	quit() #immediately terminate the program.

print ("Okay! let's continue :)")
score = 0

answer = input("What deos CPU stand for? ")

if answer.lower() == "central processing unit":
	print('correct!')
	score +=1
else:
	print('Incorrect!')


answer = input("What deos GPU stand for? ")

if answer.lower() == "graphics processing unit":
	print('correct!')
	score +=1
else:
	print('Incorrect!')


answer = input("What deos RAM stand for? ")

if answer.lower() == "random access memory":
	print('correct!')
	score +=1
else:
	print('Incorrect!')


print ("You got " + str(score) + " questions correct!")
print ("You got " + str((score /3) * 100) + "%.")