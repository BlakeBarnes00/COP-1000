import tkinter

class KiloConverter:
	def __init__(self) -> None:
		# Main window
		self.window = tkinter.Tk()

		# Create the frames to group widgets
		self.top_frame = tkinter.Frame()
		self.mid_frame = tkinter.Frame()
		self.bot_frame = tkinter.Frame()

		# Create the widgets for the top frame
		self.prompt_label = tkinter.Label(self.top_frame, text="Enter a distance in KM: ")
		self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

		# Pack the widgets into the top frame
		self.prompt_label.pack(side="left")
		self.kilo_entry.pack(side="left")

		# Create the widgets for the middle frame
		self.disc_label = tkinter.Label(self.mid_frame, text="Converted to Miles: ")

		# We need a StringVar object to associate with an output label. Use the objects
		# set method to store the string of blank characters
		self.value = tkinter.StringVar()

		# Create label associated with StringVar object. They will automatically be 
		# displayed in the label
		self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)

		# Pack the middle frames widgets
		self.disc_label.pack(side="left")
		self.miles_label.pack(side="left")

		# Create the button widgets for the bottom of the frame
		self.calc_button = tkinter.Button(self.bot_frame, text="Convert", command=self.convert)
		self.quit_button = tkinter.Button(self.bot_frame, text="Quit", command=self.window.destroy)

		# Pack the buttons
		self.calc_button.pack(side="left")
		self.quit_button.pack(side="left")

		# Pack all the frames
		self.top_frame.pack()
		self.mid_frame.pack()
		self.bot_frame.pack()

		# Enter the main loop
		tkinter.mainloop()

	def convert(self):
		# Get the value entered by the user
		kilo = float(self.kilo_entry.get())

		# Convert to miles
		miles = kilo * 0.6214

		# Convert miles to a string and store it in the StringVar object
		# so that it updates automatically
		self.value.set(miles)

program = KiloConverter()