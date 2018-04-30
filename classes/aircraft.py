'''
Created on 13 Mar 2018

@author: rosannahanly
'''
import csv
import os

class Aircraft:
    '''
    Class to store details of each aircraft
    '''
    airplaneCount = 0
    airplaneDict = {}
    
    def __init__(self, type, units, range):
        self.type = type
        self.range = range
        self.units = units
        Aircraft.airplaneCount +=1
        Aircraft.airplaneDict[self.type] = self

def loadAircraft(filename):
    with open(os.path.join(filename), 'rt', encoding = "utf8", errors = 'replace') as f:
            reader = csv.reader(f)
            for row in reader:
                Aircraft(row[0], row[2],row[4])
    