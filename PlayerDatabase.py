import sqlite3

class Database:
	def __init__(self,db_name):
		self._db_name=db_name
		#Running the CreateDatabase function
		self.CreateDatabase()
	#Creating tables
	def CreateDatabase(self):
		sql = """create table if not exists Player
			 (PlayerID integer,
			 forename text,
			 surname text,
			 rating integer,
			 email text,
			 position text,
			 avaliable text,
			 
			 primary Key(PlayerID))"""
		#Running the execute_sql function passing in the sql	 
		self.execute_sql(sql)
		
		sql = """create table if not exists Match
			 (MatchID integer,
			 date text,
			 opposition text,
			 result text,
			 
			 primary Key(MatchID))"""
		#Running the execute_sql function passing in the sql	
		self.execute_sql(sql)
		
		sql = """create table if not exists Goal
				(GoalID integer,
				opposition text,
				forename text,
				quantity integer,
				
				
				primary Key(GoalID))"""
		#Running the execute_sql function passing in the sql	
		self.execute_sql(sql)

	def execute_sql(self, sql):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			cursor.execute(sql)
			db.commit()
	
	def GetAllMatches(self):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			cursor.execute("select * from Match")
			Matches = cursor.fetchall()
			return Matches
	
	def GetAllGoals(self):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			cursor.execute("select * from Goal")
			Goals = cursor.fetchall()
			return Goals
	
	def GetAllPlayers(self):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			cursor.execute("select * from Player")
			players = cursor.fetchall()
			return players
			
	def AddGoals(self,opposition,forename,quantity):
		with sqlite3.connect(self._db_name) as db:
				cursor = db.cursor()
				sql = "insert into Goal(GoalID,opposition,forename,quantity) values ((SELECT max(GoalID) FROM Goal)+1,'{0}', '{1}', '{2}')".format(opposition,forename,quantity)
				cursor.execute(sql)
				db.commit()
	
			
	def AddMatch(self,date,opposition, result):
		with sqlite3.connect(self._db_name) as db:
				cursor = db.cursor()
				sql = "insert into Match(MatchID,date,opposition,result) values ((SELECT max(MatchID) FROM Match)+1,'{0}', '{1}', '{2}')".format(date,opposition,result)
				cursor.execute(sql)
				db.commit()
			

	def AddPlayer(self,forename, surname, rating, email, position, avaliable):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			sql = "insert into Player(PlayerID,forename, surname, rating, email, position, avaliable) values ((SELECT max(PlayerID) FROM Player)+1,'{0}','{1}', {2}, '{3}', '{4}', '{5}')".format(forename, surname, rating, email, position, avaliable)
			cursor.execute(sql)
			db.commit()
	
	def UpdatePlayer(self,forename, surname, rating, email, position, avaliable,PlayerID):
		sql = "UPDATE Player set Forename = '{0}', Surname = '{1}', rating = '{2}', email = '{3}', position = '{4}', avaliable = '{5}' where PlayerID = {6}".format(forename, surname, rating, email, position, avaliable,PlayerID)
		self.execute_sql(sql)
		
	def DeletePlayer(self,PlayerID):
		sql = "DELETE from Player WHERE PlayerID = {0}".format(PlayerID)
		self.execute_sql(sql)

g_database = Database("Player_Database.db")
