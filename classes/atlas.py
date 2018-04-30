'''
Created on 28 Apr 2018

@author: rosannahanly
'''
import csv
from math import sin, cos, radians, asin, sqrt
from classes.airport import Airport
from classes.aircraft import Aircraft
from classes.currencyExchange import CurrencyCode, CurrencyRate
from itertools import permutations

class Atlas:
    '''
    Class that calculates the shortest route for an aircraft 
    when given a csv file that has the origin airport as the 1st column and the next 4 columns being the airports to visit 
    and the 6th column the aircraft code 
    '''


    def __init__(self, filename):
        '''
        Constructor
        '''
        self.filename = filename
        self._loadRoute(filename)
        
    def _loadRoute(self, filename):
        with open(filename, encoding = "utf8", errors = 'replace') as f:
            reader = csv.reader(f)
            for row in reader:
                self._saveToCSV(row)
    
    def _saveToCSV(self, row):
        '''
        Saves results in a csv file
        '''
        output = self._shortestRoute(row)
        #print(output)
        with open('results.csv', 'a') as file:
            wr = csv.writer(file, dialect = 'excel')
            wr.writerow(output)
    
    def _shortestRoute(self, row):
        '''
    Function finds the shortest path between airports 
    '''
        self.row = row
        airportInput = [row[0], row[1], row[2], row[3], row[4]]
        aircraftInput = row[5]
        #print("The route you are trying to calculate is ", airportInput, "with aircraft", aircraftInput)
        airportsToVisit = [row[1], row [2], row[3], row[4]]
        originAirport = row[0]
        iteneries = self._permute(airportsToVisit) #iteneries is a list
        lowestcost = 99999999999
        cheapestperm = []
        for perm in iteneries:
            perm.extend([originAirport, perm[0]])
            #print(perm)
            price = self._cost(perm, aircraftInput)
    
            if price < lowestcost:
                lowestcost = price
                cheapestperm = [originAirport, perm[0], perm[1], perm[2], perm[3], originAirport]
        output = []     
        #output.append(cheapestperm)
        #output.append(aircraftInput)   
        if lowestcost >= 99999999999:
            output.append(airportInput)
            output.append(aircraftInput)
            output.append("No Possible Route") 
            #print("I'm sorry this journey is not possible") 
        else:
            output.append(cheapestperm)
            output.append(aircraftInput)
            output.append(lowestcost)
            #print("The most economic journey is ", cheapestperm, "It will cost ", lowestcost)
        #print('************************************************************')
        return output
     
    def _permute(self, destinationList): 
        '''
        function finds all combinations for destination airports and converts them to a list (Found on stack overflow)
        '''
        self.destinationList = destinationList
        permutationTuples = permutations(destinationList) 
        return list([list(_) for _ in permutationTuples])
    
    def _cost(self, itinerary, aircraft): #O(n) time complexity
        
        '''
        Func cals cost for an itinerary with a given aircraft
        '''
        air = Aircraft.airplaneDict.get(aircraft)
        if air.units == 'imperial':
            fuelCapacity = float(air.range) * 1.60934
        else:
            fuelCapacity =float(air.range)   
        totalCost = 0 #counter keeps track of cost of journey
        for i in range(len(itinerary) - 1):
            #using dictionaries from classes to find desired variables
            a1 = Airport.airportDict.get(itinerary[i])
            #print(a1)
            country = a1.country
            currencyCode = CurrencyCode.currencyCodeDict.get(country).currencyCode
            toEuroRate = float(CurrencyRate.currencyRateDict.get(currencyCode).toEuroRate)
            lat1 = a1.lat
            long1 = a1.long
            a2 = Airport.airportDict.get(itinerary[i+1])
            #print(a2)
            country = a2.country          
            lat2 = a2.lat
            long2 = a2.long
            distance = self._greatCircleDistance(long1, lat1, long2, lat2)
            #print(distance)
            if distance > fuelCapacity:
                distance = 99999999999
            else:
                distance *= toEuroRate
            totalCost +=distance
            #print(totalCost)
        return totalCost
    
    def _greatCircleDistance(self, long1, lat1, long2, lat2):

        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
            """
        # convert decimal degrees to radians 
        long1, lat1, long2, lat2 = map(radians, [float(long1), float(lat1), float(long2), float(lat2)])
        # haversine formula 
        dlon = long2 - long1
        #print(long2)
        #print(long1) 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        #print(c*r)
        return c * r

