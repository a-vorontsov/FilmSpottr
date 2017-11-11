#!/usr/bin/env python
# original code by Peter

print "Importing libraries..."
import googlemaps, csv
print "Imports done."

def addGeocode(address):
#	gmaps = googlemaps.Client(key = 'AIzaSyBOrSOIY_pfVSx-R9le50DShnzzIOqFAT8') # peter's used up API key
	gmaps = googlemaps.Client(key = 'AIzaSyCZVQx1F60aPbLcJUn5JUprEC_3Au2Gi-k') # james' fresh API key
	gmapsReply = googlemaps.geocoding.geocode(gmaps,address = address)
	if len(gmapsReply) < 1:
		print " > API fail, moving on..."
		return -1,-1
	lat = gmapsReply[0]['geometry']['location']['lat']
	lng = gmapsReply[0]['geometry']['location']['lng']
	return lng, lat


def getAddress(reader,writer):
#	with open(inputFileName, 'rb') as csvInFile:
#		with open(outputFileName, 'wb') as csvOutFile:
	for row in reader:
		if row[2] != "sceneAddress":
			lng, lat = addGeocode(row[2])
			if lng == -1 and lat == -1:
				continue
			row = row[:-2] # cut last 2 fields
			row.append(lat)
			row.append(lng)
			writer.writerow(row)
		else:
			writer.writerow(row)

#inName = "imdbAddresses0-1014.csv"
#inName = "addresses_3_UKONLYWITHDESCRIPTIONS.csv"
inName = "ukFilmLocations_NOGEOCODES.csv"
outName = "ukFilmLocations_WITH_GEOCODES.csv"
csvInFile = open(inName, 'r')#rb
csvOutFile = open(outName, 'w')#wb
reader = csv.reader(csvInFile, delimiter = ',', quotechar = '"')
writer = csv.writer(csvOutFile, delimiter = ',', quotechar = '"')

# loop over reader
#nLines = sum(1 for row in reader)
#print " > Number of lines = "+str(nLines)
startPoint = 0 # number of lines to skip
currentLine = 0
for row in reader:
	currentLine = currentLine+1
	print " > geocoding line #"+str(currentLine)#+"/"+str(nLines)
	if row[2] == "sceneAddress":
		writer.writerow(row)
	else:
		lng, lat = addGeocode(row[2])
		if lng == -1 and lat == -1:
			continue
		row = row[:-2] # cut last 2 fields
		row.append(lat)
		row.append(lng)
		writer.writerow(row)

