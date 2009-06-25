#podcaster skeleton
import feedparser,urllib,time,subprocess,sqlite3,bluetooth,hashlib
class podBlaster():
	def __init__():
		self.database="podcasts.db"
	#db functions
	def cursor():
		con=sqlite3.connect(self.database)
		dbconections=[con,con.cursor()]
		return dbconections
	
	def addDevice(name,address):
		con=self.cursor()
		a=con[1].execute('INSERT INTO device VALUES (null,?,?,1)' , (name,address))
		con[0].commit()

	def addFeed(name,path,url):
		con=self.cursor()
		a=con[1].execute('INSERT INTO feed VALUES (null,?,?,?,"x",1)' , (name,path,url))
		con[0].commit()	
	
	def addEpisode(name,path,url):
		con=self.cursor()
		a=con[1].execute('INSERT INTO episode VALUES (null,?,?,1)' , (feed,file))
		con[0].commit()	

	def toggleActive(id,table,active):
		con=self.cursor()
		a=con[1].execute('UPDATE '+table+' SET active=? WHERE id=?' , (active,id))
		con[0].commit()	
	
	def get(table):
		con=self.cursor()
		a=con[1].execute('SELECT * FROM '+table)
		return a
	def getEpisodes(feed):
		con=self.cursor()
		a=con[1].execute('SELECT name FROM episode WHERE id =?', (feed))
		return a		

	#feed functions
	def getFeedEntries(feed):
		feed=feedparser.parse(feed)
		return feed.entries

	
	def getUpdatedFeeds():
		updatedFeeds=[]
		c=self.cursor
		activeFeeds

	def getEnclosure(entry):
		return=entry.enclosures[0].href			 


	def getDownload(entry,destinationPath,download=True):
		url=entry.enclosures[0].href
		destinationPath=destinationPath+url.split('/')[-1]
		if download==False:
			return url.split('/')[-1]
		elif urllib.urlretrieve(url, destinationPath):
			return url.split('/')[-1]	
	
	def uploadQueue(fileList,deviceId):
		"""takes list of [id,filepath] marks uploaded files inactive"""
		uploaded=[]
		for file in filelist:
			if os.system('obexftp -b '+deviceId+'  -c E:/Music\ Downloads/ -p '+file[1]):
				uploaded.append[0]
		return uploaded
	# Business logic
	def getNewPodcasts(feed):
		a=self.get('episode')
		downloadedEpisodes=[]
		for episode in a:
			downloadedEpisodes.append(a[1])
		episodesInFeed=self.getEpisodes(feed)
		newPodcasts=list(set(episodesInFeed).difference(set(downloadedEpisodes)))
		return newPodcasts
		
			


feed="http://www.leoville.tv/podcasts/twit.xml"
data=feedparser.parse(feed)
path=data.entries[0].enclosures[0].href
track=path.split('/')
track=track[-1]
t=urllib.urlretrieve(path, track)
hashlib.md5(str(data)).hexdigest()




