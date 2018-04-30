'''
Created on 27 Apr 2018

@author: rosannahanly
'''
from math import sin, cos, radians, asin, sqrt
from classes.airport import Airport
from classes.aircraft import Aircraft
from classes.currencyExchange import CurrencyCode, CurrencyRate
import csv
import sys


class FlightPlan:
    '''
    Class that finds the best available route with given airports and aircraft and stores result in a csv file
    '''

    error = float('inf')
    
    def __init__(self, filename):
        '''
        Constructor
        '''
        self.filename = filename
        self.loadRoute(filename)
        
    def loadRoute(self, filename):
        '''
        Opens file and calculates best route for each row
        '''
        
        with open(filename, encoding = "utf8", errors = 'replace') as f:
            reader = csv.reader(f)
            for row in reader:
                self._writeToCSV(row)
            
    def _greatcircledist(self, long1, lat1, long2, lat2):
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
            """
        # convert decimal degrees to radians 
        long1, lat1, long2, lat2 = map(radians, [float(long1), float(lat1), float(long2), float(lat2)])
    
        # haversine formula 
        dlon = long2 - long1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        #print(c*r)
        return c * r
        
    
    def _createGraph(self, airportInput, aircraftInput): #O(n2) time complexity
        '''
        function creates a weighted directed graph
        '''
        air = Aircraft.airplaneDict.get(aircraftInput)
        if air == None:
            return FlightPlan.error
        if air.units == 'imperial':
            fuelCapacity = float(air.range) * 1.60934
        else:
            fuelCapacity =float(air.range)
        graph = {}
        for i in range(len(airportInput)):
            graph[airportInput[i]] = {}
            a1 = Airport.airportDict.get(airportInput[i])
            if a1 == None:
                return FlightPlan.error
            country = a1.country
            currencyCode = CurrencyCode.currencyCodeDict.get(country).currencyCode
            toEuroRate = float(CurrencyRate.currencyRateDict.get(currencyCode).toEuroRate)
            lat1 = a1.lat
            long1 = a1.long
            for j in range(len(airportInput)):
                a2 = Airport.airportDict.get(airportInput[j])
                if a2 == None:
                    return FlightPlan.error
                country = a2.country          
                lat2 = a2.lat
                long2 = a2.long
                dis = self._greatcircledist(long1, lat1, long2, lat2)
                if dis > fuelCapacity:
                    dis = 999999999999
                else:
                    dis *= toEuroRate
                if airportInput[i] == airportInput[j]:
                    pass
                else:
                    graph[airportInput[i]][airportInput[j]] = dis
        return graph

    def _greedyAlgo(self, row): #O(n2) time complexity 
        '''
        Finds the best route by always choosing the closest airport
        '''
        self.row = row
        route = [row[0]] #list keeps track of the route taken
        airportIdx = set() #set keeps track of the indexes of the airports visited
        totalPrice = [] #incrementing counter keeps track of the journey cost    
        airportInput = [row[0], row[1], row[2], row[3], row[4]]
        aircraftInput = row[5]
        #print("The route you are trying to calculate is ", airportInput, "with aircraft", aircraftInput)
        graph = self._createGraph(airportInput, aircraftInput) #create a weighted directed graph
        if graph == FlightPlan.error:
            print("Something went wrong. \nPlease make sure the csv file is in the format of airportCode, airportCode, airportCode, airportCode, airportCode, aircraftCode. \nor that all codes are correct") 
            sys.exit()
        #print(graph)
        lowestprice = 99999999999 #this is the value set for route that can't be completed 
        currentAirport = 0
        airportIdx.add(currentAirport)
        foundAirport = 0
        j = 1
        while j < len(airportInput):
            for i in range(0, len(airportInput)):
                if i in airportIdx:
                    pass
                else:
                    cost = graph.get(airportInput[currentAirport], {}).get(airportInput[i])
                    if cost == None:
                        pass
                    elif cost < lowestprice:
                        lowestprice = cost
                        foundAirport = i
            totalPrice.append(lowestprice)
            #print(totalPrice)
            route.append(row[foundAirport])
            airportIdx.add(foundAirport)
            currentAirport = foundAirport
            lowestprice = 99999999999
            j += 1
        totalPrice.append(graph.get(airportInput[currentAirport], {}).get(airportInput[0]))
        totalPrice = sum(totalPrice)
        if totalPrice >= 99999999999:
            totalPrice = "No Possible Route"
        output = []
        route.append(row[0])
        output.append(route)
        output.append(aircraftInput)
        output.append(totalPrice)
        return output
        
    def _writeToCSV(self, row):
        '''
        Saves results in a csv file
        '''
        output = self._greedyAlgo(row)
        #print(output)
        with open('results.csv', 'a') as file:
            wr = csv.writer(file, dialect = 'excel')
            wr.writerow(output)
        

        
        
            

        