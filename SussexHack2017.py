# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:20:58 2017

@author: Damin
"""
import googlemaps
def addGeocode(address):
    gmaps = googlemaps.Client(key='AIzaSyBOrSOIY_pfVSx-R9le50DShnzzIOqFAT8')
    a=googlemaps.geocoding.geocode(gmaps,address=address)
    lng=a[0]['geometry']['location']['lng']
    lat=a[0]['geometry']['location']['lat']
    return lng, lat

import csv
import os
def get_addrase():
    os.chdir("C:/Users/Damin/Documents/BitBucket")
    with open('testsample_NO_GEOCODES_csv.csv', 'rb') as csvfile:
        with open('testsample_WITH_GEOCODES.csv', 'wb') as csvfileR:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            spamwriter = csv.writer(csvfileR, delimiter=',', quotechar='"')
            for row in spamreader:
                if row[2]!="sceneAddress":
                    lng, lat=addGeocode(row[2])
                    row.append(lat)
                    row.append(lng)
                    spamwriter.writerow(row)
                else:
                    spamwriter.writerow(row)
#    with open('testsample_WITH_GEOCODES.csv', 'wb') as csvfile:
#        spamwriter = csv.writer(csvfileR, delimiter=',', quotechar='"')
#        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


#from csvparser import parser
#from csvparser import fields
#class AdPerformanceReportParser(parser.Parser):
#    imdbID=fields.CharField()
#    movieTitle	=fields.CharField()
#    sceneAddress=fields.CharField()
#    sceneDescription	=fields.CharField()
#    sceneLat=fields.DecimalField()
#    sceneLon=fields.DecimalField()
#    fields_order = ['imdbID','movieTitle','sceneAddress','sceneDescription',\
#                    'sceneLat','sceneLon']

