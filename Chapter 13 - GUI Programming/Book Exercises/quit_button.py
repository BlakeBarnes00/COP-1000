import tkinter
import tkinter.messagebox

class MyGUI:
	def __init__(self) -> None:
		# Create the main window
		self.window = tkinter.Tk()

		self.button = tkinter.Button(self.window, text="Click Me", command=self.do_something)
		self.quit_button = tkinter.Button(self.window, text="Quit", command=self.window.destroy)

		self.button.pack()
		self.quit_button.pack()

		tkinter.mainloop()

	def do_something(self):
		tkinter.messagebox.showinfo("Response", "Thanks for the click.")
	
gui = MyGUI()