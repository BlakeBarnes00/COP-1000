class ContestResult():
	def __init__(self):
		self.winner = ""
		self.second_place = ""
		self.third_place = ""

	def set_winner(self, name):
		self.winner = name
	
	def set_second_place(self, name):
		self.second_place = name

	def set_third_place(self, name):
		self.third_place = name
	
	def get_winner(self):
		return self.winner
	
	def get_second_place(self):
		return self.second_place
	
	def get_third_place(self):
		return self.third_place
		