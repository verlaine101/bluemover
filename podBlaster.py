import feedFunctions,dbFunctions,os
#make new objects
db = dbFunctions.dbFunctions()
pod = feedFunctions.feedFunctions()
deviceID='00:1F:00:B6:21:C0'
#first get feeds from db
feeds=db.get('feed')
for feed in feeds:
	print feed[1]
	entries = pod.getFeedEntries(feed[3])
	feedDirectory=feed[2]
	#iterate through entries entering new episode in db
	for entry in entries:
		enclosure=pod.getEnclosure(entry)
		episode=pod.getEpisode(enclosure)
		path=feedDirectory+episode
		#Add new podcats into db
		if not inDb(episode):
			db.addEpisode(feed[0],episode)
		#download podcast marked for downloapythod
		if downloadEpisode:
			pod.getDownload(enclosure,path)
#getlist of downloads to be transferred 
downloads=db.getTransferList()
	#if there are items in the queue and the bluetooth device is present attempt to transfer
	if downloads:
		for download in downloads:
			print download[1]
			 if os.system('bluetooth-transfer '+deviceId+' '+download[1]) == 0:
				db.setUploaded(download[0])

