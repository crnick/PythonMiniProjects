import time 
import datetime #allows us to work with string represntation of time 
import pygame #allows us to work with sound effects 


def set_alarm(alarm_time):
	print(f"Alarm set for {alarm_time}")
	sound_file = "my_file.mp3"



if __name__ == "__main__":
	alarm_time = input("Enter the alarm time (HH:MM:SS)")
	set_alarm(alarm_time)
	is_running = True

	while is_running:
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time)

		if current_time == alarm_time:
			print("Wake UP!")
			pygame.mixer().init()
			pygame.mixer.music.load(sound_file)
			pygame.mixer.music.play()
			is_running= False

		time.sleep(1)
		