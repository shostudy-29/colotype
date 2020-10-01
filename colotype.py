#Colotype
#A project by Shourya

import tkinter
import random

#List of colors in the game
colors = ['Red', 'Blue', 'Green', 'Pink', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 20

def startGame(event):
	if timeleft == 20:
		countdown()
	nextColour()

def nextColour():
	global score
	global timeleft

	if timeleft > 0:
		e.focus_set()
		if e.get().lower() == colours[1].lower():
			score += 1

		e.delete(0, tkinter.END)

		random.shuffle(colours)
		label.config(fg=str(colours[1]), text=str(colours[0]))
		scoreLabel.config(text="Score: " + str(score))

def countdown():
	global timeleft

	if timeleft > 0:
		timeleft -= 1

		timeleft.config(text="Time Left: " + str(timeleft))
		timeLabel.after(1000, countdown)

tk=tkinter.Tk()

tk.title("COLOTYPE")
tk.geometry("375x200")

instructions = tkinter.Label(tk, text= "Type in the colour of the text, net the word in the text",font=('Helvetica', 12))

instructions.pack()

scoreLabel = tkinter.Label(tk, text="Press enter to start the game")
scoreLabel.pack()

timelabel = tkinter.Label(tk,text="Timeleft: "+str(timeleft))
timelabel.pack()

label = tkinter.Label(root, font=("Helvetica",60))
label.pack()

e = tkinter.Entry(tk)
root.blind('<Return>', startGame)
e.pack()
e,focus_set()


tk.mainloop()

#Project Finished