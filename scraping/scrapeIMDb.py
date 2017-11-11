#!/usr/bin/env python

print "Importing libraries..."
import sys, urllib2, re
print "Imports done."

# function to scrape locations from imdb
def scrapeLocations(locationsPageURL):
	#print "\n > Looking at URL "+url
	pagemovieData = urllib2.urlopen(url)
	imdbID = re.sub("http://www.imdb.com/title/","",locationsPageURL)
	imdbID = re.sub("/locations","",imdbID)
	movieData = []
	movieData.append(imdbID)
	address = ""
	
	# read imdb page line by line
	for pageline in pagemovieData:

		# get movie title
		if "<meta property='og:title' content" in pageline:
			pageline = re.sub("<meta property='og:title' content=\"", "",pageline)
			pageline = re.sub("\" />","",pageline)
			movieData.append(pageline.strip())
		
		# get location address
		if pageline.startswith("itemprop='url'"):
			if "<span class=\"nobr\">" in pageline: # movie title again, so skip
				continue
			elif "itemprop='url'>" in pageline: # address
				pageline = re.sub("itemprop='url'>","",pageline)[:-1]
				address = str(pageline.strip())
				#print " > > location: "+pageline
		
		# location description
		elif "</dd>" in pageline:
				pageline = re.sub("</dd>","",pageline)
				pageline = re.sub("\(","",pageline)
				pageline = re.sub("\)","",pageline)[:-1]
				movieData.append([address,pageline.strip()])
				#print " > > > description: "+pageline
		elif "<h2>See also</h2>" in pageline: # locations are over
			break
		elif "It looks like we don't have any Filming Locations for this title yet." in pageline:
			movieData.append("NOLOCATIONS")
			break
	return movieData

# output file
outputFile = open('imdbAddresses.csv','w') # 'a' means append, so you won't overwrite anything in the file already
outputFile.write("----------")

# read list of IMDb urls
urlFileName='imdbURLsTIDY.dat'
urlFile = open(urlFileName,'r')
nLines = sum(1 for line in open(urlFileName))
print " > Number of lines = "+str(nLines)
startPoint = 1012 # number of lines to skip
currentLine = 0
for line in urlFile:
	try:
		currentLine = currentLine +1
		if currentLine < startPoint:
			continue
		print " > Processing URL "+str(currentLine)+"/"+str(nLines)+" = "+str(round(float(currentLine)/float(nLines),2))+"%"
		url = line.strip()+"locations"
		movieData = scrapeLocations(url)
		
		# construct output
		outputStub = movieData[0]+","+movieData[1]+","
		if movieData[2] is "NOLOCATIONS":
			print " > No location information."
			continue
		else:
			for datum in movieData[2:]:
				output = movieData[0]+","+movieData[1]+",\""+datum[0]+"\","+datum[1]+",,\n"
				outputFile.write(output)
	except Exception, e:
		print " > Got an error: "+str(e)+" from URL: "+str(line)
		print " > Moving on..."
		continue

outputFile.close()
print " > Done!"








