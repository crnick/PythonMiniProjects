#graphical library -> allows us to create grid layout and place widgets on screen
import tkinter as tk 


def main():
	window = tk.Tk() #creates a tk window
	window.title("Text Editor")
	text_edit = tk.Text(window,font = "Helvetica 18") #create text widget
	text_edit.grid(row=0,column=1) # place this element on the parent grid
	window.mainloop() #keeps the window unless users clicks X button or force quits.


main()