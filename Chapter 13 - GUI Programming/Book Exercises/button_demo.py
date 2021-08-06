import tkinter
from tkinter import messagebox

class MyGUI:
	def __init__(self) -> None:
		# Create the window widget
		self.main_window = tkinter.Tk()

		# Create the button widget
		self.my_button = tkinter.Button(self.main_window, text="CLICK ME!", command=self.do_something)

		# Pack the button
		self.my_button.pack()

		# Main window loop
		tkinter.mainloop()

	# The function the button will use.
	def do_something(self):
		tkinter.messagebox.showinfo("Response", "Thanks for clicking.")

my_gui = MyGUI()