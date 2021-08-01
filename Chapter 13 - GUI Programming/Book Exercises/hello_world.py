import tkinter

class MyGUI:
	def __init__(self) -> None:
		# Create the window
		self.main_window = tkinter.Tk()

		# Create Label Widget
		self.label = tkinter.Label(self.main_window, text="Hello World")

		# Call the Label widget's pack method.
		self.label.pack()

		# Main loop
		tkinter.mainloop()

my_gui = MyGUI()