#!/usr/bin/env python

print "Importing libraries..."
import sys, urllib2, re
print "Imports done."

# function to scrape locations from imdb
def scrapeLocations(locationsPageURL):
	print "\n > Looking at URL "+url
	pagemovieData = urllib2.urlopen(url)
	imdbID = re.sub("http://www.imdb.com/title/","",locationsPageURL)
	imdbID = re.sub("/locations","",imdbID)
	movieData = []
	movieData.append(imdbID)
#	locationInfo = ["",""]
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
				#movieData.append(pageline.strip())
				address = str(pageline.strip())
#				locationInfo[0] = str(pageline.strip())
				#print " > > location: "+pageline
		
		# location description
		elif "</dd>" in pageline:
				pageline = re.sub("</dd>","",pageline)
				pageline = re.sub("\(","",pageline)
				pageline = re.sub("\)","",pageline)[:-1]
				#movieData.append(pageline.strip())
				#description = pageline.strip()
#				locationInfo[1] = str(pageline.strip())
#				locationInfoTemp = locationInfo
				#movieData.append(locationInfoTemp)
				movieData.append([address,pageline.strip()])
#				print locationInfo
#				print " > > > description: "+pageline
		elif "<h2>See also</h2>" in pageline: # locations are over
			break
		elif "It looks like we don't have any Filming Locations for this title yet." in pageline:
			movieData.append("NOLOCATIONS")
			break
	return movieData

# read list of IMDb urls
urlFileName='imdbURLsONLY.dat'
urlFile = open(urlFileName,'r')
for line in urlFile:
	url = line.strip()+"locations"
	movieData = scrapeLocations(url)

	# construct output
	outputStub = movieData[0]+","+movieData[1]+","
	if movieData[2] is "NOLOCATIONS":
		print " > No location information."
		continue
	else:
		for datum in movieData:#[2:]:
#			None
			print datum
#		for i, datum in enumerate(movieData[2:]):
#			None








