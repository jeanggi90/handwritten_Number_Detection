#! /usr/bin/env python3

from tkinter import *		# GUI
import io 					# Get Canvas Content
from PIL import Image

import sys					# Exiting
import subprocess			# Clear Terminal

root = None
image = None

class Window(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master

		self.master.title("Draw a Number")
		self.pack(fill=BOTH, expand=1)

		self.addCanvas()
		self.addBottons()


	def addCanvas(self):
		self.canvas = Canvas(self.master, width=500, height=500, bg="gray")
		self.canvas.pack()

		self.canvas.bind("<B1-Motion>", self.paint)

	def paint(self, event):
		x, y = (event.x), (event.y)
		r = 6
		self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="black")

	def addBottons(self):
		clearButton = Button(self.master, text="Clear", command=self.clearCanvas, height=1, width=5)
		clearButton.place(x=0, y=0)

		exportImageButton = Button(self.master, text="Detect Number", command=self.getImage, height=1, width=10)
		exportImageButton.place(x=80, y=0)

	def clearCanvas(self):
		self.canvas.delete("all")

	def getImage(self):
		"""
			Convertes the canvascontent to a postscript and then to an image. 
		"""
		global root, image

		postscript = self.canvas.postscript(colormode="gray")
		image = Image.open(io.BytesIO(postscript.encode('utf-8')))

		root.destroy()

class Menu:

	def drawMenu():

		while 1:
			subprocess.run( "clear")
			print("--------------")
			print("     Menu     ")
			print("--------------")
			print("1. Draw a numbe and feed it to the neural network.")
			print("2. Train neural network")
			print("9. Exit")
			print("--------------")

			try:
				i = int(input("Please select an option from above\n"))

				if i == 1:
					# Input menu

					if getInputImage():
						# Got image
						# TODO: Feed to cnn
						break

					else:
						# Did not get image
						Menu.drawMenu()

				elif i == 2:
					# Train cnn
					break

				elif i == 9:
					# Exit
					sys.exit()

				else:
					print("Invalid input. Please select one of the options")

			except SystemExit:
				print("Exiting")
				sys.exit()

			except:
				print("Invalid input. Please enter a number")

def getInputImage():
	"""
		Opens the drawing board and returns a boolean depending on whether we got an image or not
	"""
	global root, image

	image = None # Set to nil so that we can later check whether we received an image or not

	root = Tk()

	root.geometry("500x540")
	root.resizable(width=False, height=False)

	app = Window(root)
	root.mainloop()

	if image:
		print("Got image")
		image.show()
		return true

	else:
		# print("Did not get an image")
		return fale

if __name__ == '__main__':

	Menu.drawMenu()
	# getInputImage()
	