class TeamLayoutData:
	def __init__(self):
		#List of all possible positions 
		self.position = ["GK","LB","CB","CB","RB","LM","CM","CM","RM","ST","ST"]
		#Each position is blank
		self.player_assigned = [None, None, None, None, None, None, None, None, None, None, None]
	
g_teamlayout = TeamLayoutData()