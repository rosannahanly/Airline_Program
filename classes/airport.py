'''
Created on 13 Mar 2018

@author: rosannahanly
''' 
import csv


class Airport:
    '''
    Class to store details of each airport
    '''
    
    airportDict = {}
    airportCount = 0
    
    def __init__(self, code, lat, long, country):
        self.code = code
        self.lat = lat
        self.long = long
        self.country = country
        Airport.airportCount +=1
        Airport.airportDict[self.code] = self

def loadAirport(filename):
    with open(filename, 'rt', encoding = "utf8", errors = 'replace') as f:
            reader = csv.reader(f)
            for row in reader:
                Airport(row[4],row[6],row[7],row[3])
    

 