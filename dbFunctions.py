#podcaster skeleton
import feedparser,urllib,time,subprocess,sqlite3,bluetooth,hashlib

class dbFunctions(object):
	def __init__(self):
		self.database="podcasts.db"
	#db functions
	def cursor(self):
		con=sqlite3.connect(self.database)
		dbconections=[con,con.cursor()]
		return dbconections
	
	def transaction(self,execute):
		con=self.cursor()
		a=con[1].execute(execute)
		con[0].commit()
		con[0].close()
	
	def addDevice(self,name,address):
		execute="'INSERT INTO device VALUES (null,?,?,1)'"
		self.transaction(execute)

	def addFeed(self,name,path,url):
		con=self.cursor()
		a=con[1].execute('INSERT INTO feed VALUES (null,?,?,?,"x",1)' , (name,path,url))
		con[0].commit()	
	
	def addEpisode(self,feed,file):
		con=self.cursor()
		a=con[1].execute('INSERT INTO episode VALUES (null,?,?,0,0)' , (feed,file))
		con[0].commit()	
		
	def toggleActive(self,table,ep_id,active):
		con=self.cursor()
		a=con[0].execute('UPDATE '+table+' SET active=? WHERE id=?' , (active,ep_id))
		con[0].commit()
		con[0].close()
	def get(self,table):
		con=self.cursor()
		a=con[1].execute('SELECT * FROM '+table)
		return a
		con[0].close()
	def getEpisode(self,name):
		con=self.cursor()
		a=con[1].execute('SELECT name FROM episode WHERE name =?', (name))
		return a
	def inDb(self,name):
		if self.getEpisode():
			return True
		else:
			return False
	def getTransferList(self):
		transferList[]
		con=self.cursor()
		a=con[1].execute('SELECT id,feed,name FROM episode WHERE transfer = 1')
		for episode in a:
			#get path from feed, and append  id and path+file
		return transferList
		
		

		
			






