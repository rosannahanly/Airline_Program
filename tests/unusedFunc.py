from math import pi, sin, cos, acos, radians, asin, sqrt
from classes.airport import Airport
from classes.aircraft import Aircraft
from classes.currencyExchange import CurrencyCode, CurrencyRate
from itertools import permutations
from numba.types import none
from classes import airport, aircraft
#from atlas import greatcircledist

def DistanceBetweenAirports(latitude1, longitude1, latitude2, longitude2):
        radius_earth = 6371 #km
        theta1 = float(longitude1) * (2*pi)/360
        theta2 = float(longitude2) * (2*pi)/360
        phi1 = (90 - float(latitude1)) * (2*pi)/360
        phi2 = (90 - float(latitude2)) * (2*pi)/360
        distance = acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2)) * radius_earth
        return distance
    
def createMatrix (airportInput, aircraftInput):
    '''
    Function creates a matrix of airports and assigns weights based on distances between them
    '''
    air = Aircraft.airplaneDict.get(aircraftInput)
    if air.units == 'imperial':
        fuelCapacity = float(air.range) * 1.60934
    else:
        fuelCapacity =float(air.range)
    Matrix =[[0]*len(airportInput) for i in range(len(airportInput))]
    for i in range(len(airportInput)):
        a1 = Airport.airportDict.get(airportInput[i])
        country = a1.country
        currencyCode = CurrencyCode.currencyCodeDict.get(country).currencyCode
        toEuroRate = float(CurrencyRate.currencyRateDict.get(currencyCode).toEuroRate)
        lat1 = a1.lat
        long1 = a1.long
        for j in range(len(airportInput)):
            a2 = Airport.airportDict.get(airportInput[j])
            country = a2.country          
            lat2 = a2.lat
            long2 = a2.long
            if (i ==j):
                dis = 0
            else:
                #dis = greatcircledist(lat1, long1, lat2, long2)
                if dis > fuelCapacity:
                    dis = 999999999999999
                else:
                    dis = dis *toEuroRate
            Matrix[i][j] = dis
    return Matrix

#print(createMatrix(airports, 'A319'))

'''
class Atlas():
    
    atlas = {}
    
    def __init__(self, csvFile):
        self.loadData(csvFile)
    
    def loadData(self, csvFile):
        
        #Function loads in csv file
           
        f = open(csvFile)
      
        for line in f:
            line = line.split(",")
            i = Airport(line[4], line[6], line[7], line[3], line[1])
            self.atlas[line[4]] = i
    
    def getAirport(self, code):
        
        #Function returns airport info (object) based on code given
        
        return self.atlas[code]
  
    @staticmethod
    def DistanceBetweenAirports(latitude1, longitude1, latitude2, longitude2):
        radius_earth = 6371 #km
        theta1 = float(longitude1) * (2*pi)/360
        theta2 = float(longitude2) * (2*pi)/360
        phi1 = (90 - float(latitude1)) * (2*pi)/360
        phi2 = (90 - float(latitude2)) * (2*pi)/360
        distance = acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2)) * radius_earth
        return distance
    
    def getDistance(self, code1, code2):
        airport1 = self.getAirport(code1)
        airport2 = self.getAirport(code2)
        
        distance = self.DistanceBetweenAirports(airport1.lat, airport1.long, airport2.lat, airport2.long)
        return distance
'''
