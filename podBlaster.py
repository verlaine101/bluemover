import feedFunctions,dbFunctions,os
#make new objects
db = dbFunctions.dbFunctions()
pod = feedFunctions.feedFunctions()
deviceID='00:1F:00:B6:21:C0'
#first get feeds from db
feedList=[]
feeds=db.get('feed')
#must create list as db will be locked for writing while we iterate through it
for feedEntry in feeds:
	feedList.append(feedEntry)

for feed in feedList:
	print feed[1]
	entries = pod.getFeedEntries(feed[3])
	feedDirectory=feed[2]
	#iterate through entries entering new episode in db if not already
	for entry in entries:
		enclosure=pod.getEnclosure(entry)
		episode=pod.getEpisode(enclosure)
		path=feedDirectory+episode
		#Add new podcats into db with and set to download and transfer
		print episode
		if db.inDb(episode) == False:
			db.addEpisode(feed[0],episode,enclosure)
			
#download marked episodes
downloads=db.getDownloadList()
if downloads:
	for download in downloads:
		print download[1],download[2]
		if pod.getDownload(download[1],download[2]):
			db.setDownloaded(download[0])
							



# get list of downloads to be transferred 
downloads=db.getTransferList()
	#if there are items in the queue and the bluetooth device is present attempt to transfer
if downloads:
	for download in downloads:
		print 'obexftp -b '+deviceID+' -c E:/Podcasts/ -p '+download[1]
		if os.system('obexftp -b '+deviceID+' -c E:/Podcasts/ -p '+download[1]) == 0:
			db.setTransfered(download[0])

