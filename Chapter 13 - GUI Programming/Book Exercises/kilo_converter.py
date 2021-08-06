import tkinter
import tkinter.messagebox

class KiloConverter:
	def __init__(self) -> None:
		self.window = tkinter.Tk()

		# Two frames to group the widgets
		self.top_frame = tkinter.Frame(self.window)
		self.bottom_frame = tkinter.Frame(self.window)

		# Create the widgets for the top frame
		self.prompt_label = tkinter.Label(self.top_frame, text="Enter distance in kilometers: ")
		self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

		# Pack the top frames widgets
		self.prompt_label.pack(side="left")
		self.kilo_entry.pack(side="left")

		# Create the button widgets for the bottom frame
		self.calc_button = tkinter.Button(self.bottom_frame, text="Convert", command=self.convert)
		self.quit_botton = tkinter.Button(self.bottom_frame, text="Quit", command=self.window.destroy)

		self.calc_button.pack()
		self.quit_botton.pack()

		self.top_frame.pack()
		self.bottom_frame.pack()

		tkinter.mainloop()

	def convert(self):
		# Get the data from the widget
		kilo = float(self.kilo_entry.get())
		miles = kilo * 0.6214
		tkinter.messagebox.showinfo("Results", f"{kilo} kilometers is equal to {miles} miles.")

converter = KiloConverter()