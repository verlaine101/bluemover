#podcaster skeleton
import feedparser,urllib,time,subprocess,sqlite3,bluetooth,hashlib
class feedFunctions(object):
	def __init__(self):
		pass

	def getFeedEntries(self,feed):
		feed=feedparser.parse(feed)
		return feed.entries

	
	def getUpdatedFeeds(self):
		updatedFeeds=[]
		c=self.cursor
		activeFeeds

	def getEnclosure(self,entry):
		return entry.enclosures[0].href

	def getEpisode(self,enclosure):
		return enclosure.split('/')[-1]	 

	def getDownload(self,url,destinationPath,download=True):
		if download==False:
			return url.split('/')[-1]
		elif urllib.urlretrieve(url, destinationPath):
			return url.split('/')[-1]	
	
	def uploadQueue(self,fileList,deviceId):
		"""takes list of [id,filepath] marks uploaded files inactive"""
		uploaded=[]
		for file in filelist:
			if os.system('obexftp -b '+deviceId+'  -c E:/Music\ Downloads/ -p '+file[1]):
				uploaded.append[0]
		return uploaded

		
			







