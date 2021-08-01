import tkinter

class MyGUI:
	def __init__(self) -> None:
		self.main_window = tkinter.Tk()

		# Create two frames, one for the top and one for the bottom
		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		# Create three Labels for the top frame
		self.label1 = tkinter.Label(self.top_frame, text="Winken")
		self.label2 = tkinter.Label(self.top_frame, text="Blinken")
		self.label3 = tkinter.Label(self.top_frame, text="Nod")

		# Pack labels that are in the top frame.
		# Use the side="Top" argument to stack them on eachother
		self.label1.pack(side="top")
		self.label2.pack(side="top")
		self.label3.pack(side="top")

		# Now for the bottom
		self.label4 = tkinter.Label(self.bottom_frame, text="Winken")
		self.label5 = tkinter.Label(self.bottom_frame, text="Blinken")
		self.label6 = tkinter.Label(self.bottom_frame, text="Nod")

		# Organize them from the left of their frame
		self.label4.pack(side="left")
		self.label5.pack(side="left")
		self.label6.pack(side="left")

		# Now pack the frames
		self.top_frame.pack()
		self.bottom_frame.pack()

		tkinter.mainloop()

my_gui = MyGUI()