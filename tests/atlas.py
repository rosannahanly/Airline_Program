'''
Created on 4 Apr 2018

@author: rosannahanly
'''
from math import sin, cos, radians, asin, sqrt
from classes.airport import Airport
from classes.aircraft import Aircraft
from classes.currencyExchange import CurrencyCode, CurrencyRate
from itertools import permutations



def greatcircledist(long1, lat1, long2, lat2):
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
        return c * r
    
            
def shortestPath (row): #O(n!) time complexity
    '''
    Function finds the shortest path between airports 
    '''
    airportInput = [row[0], row[1], row[2], row[3], row[4]]
    aircraftInput = row[5]
    print("The route you are trying to calculate is ", airportInput, "with aircraft", aircraftInput)
    airportsToVisit = [row[1], row [2], row[3], row[4]]
    originAirport = row[0]
    iteneries = permute(airportsToVisit) #iteneries is a list
    lowestcost = 99999999999
    cheapestperm = []
    for perm in iteneries:
        perm.extend([originAirport, perm[0]])
        #print(perm)
        price = cost(perm, aircraftInput)

        if price < lowestcost:
            lowestcost = price
            cheapestperm = [originAirport, perm[0], perm[1], perm[2], perm[3], originAirport]
            
    if lowestcost == 99999999999:
        print("I'm sorry this journey is not possible") 
    else:
        print("The most economic journey is ", cheapestperm, "It will cost ", lowestcost)
    print('************************************************************')

def permute(destinationList): 
    '''
    function finds all combinations for destination airports and converts them to a list (Found on stack overflow)
    '''
    permutationTuples = permutations(destinationList) 
    return list([list(_) for _ in permutationTuples])          

def cost(itinerary, aircraft): #O(n) time complexity 
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
        country = a1.country
        currencyCode = CurrencyCode.currencyCodeDict.get(country).currencyCode
        toEuroRate = float(CurrencyRate.currencyRateDict.get(currencyCode).toEuroRate)
        lat1 = a1.lat
        long1 = a1.long
        a2 = Airport.airportDict.get(itinerary[i+1])
        country = a2.country          
        lat2 = a2.lat
        long2 = a2.long
        distance = greatcircledist(long1, lat1, long2, lat2)
        if distance > fuelCapacity:
            distance = float('inf')
        else:
            distance *= toEuroRate
        totalCost +=distance
    return totalCost

def createGraph(airportInput, aircraftInput): #O(n2) time complexity
    '''
    function creates a weighted directed graph
    '''
    air = Aircraft.airplaneDict.get(aircraftInput)
    if air.units == 'imperial':
        fuelCapacity = float(air.range) * 1.60934
    else:
        fuelCapacity =float(air.range)
    graph = {}
    for i in range(len(airportInput)):
        graph[airportInput[i]] = {}
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
            dis = greatcircledist(lat1, long1, lat2, long2)
            if dis > fuelCapacity:
                dis = None
            else:
                dis *= toEuroRate
            if airportInput[i] == airportInput[j]:
                pass
            else:
                graph[airportInput[i]][airportInput[j]] = dis
    return graph

def greedyAlgo(row): #O(n2) time complexity 
    route = [row[0]] #list keeps track of the route taken
    airportIdx = set() #set keeps track of the indexes of the airports visited
    totalPrice = 0 #incrementing counter keeps track of the journey cost    
    airportInput = [row[0], row[1], row[2], row[3], row[4]]
    aircraftInput = row[5]
    graph = createGraph(airportInput, aircraftInput) #create a weighted directed graph 
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
        totalPrice += lowestprice
        route.append(row[foundAirport])
        airportIdx.add(foundAirport)
        currentAirport = foundAirport
        lowestprice = 99999999999
        j += 1
    totalPrice  += (graph.get(airportInput[currentAirport], {}).get(airportInput[0]))
    route.append(row[0])
    if totalPrice >= 99999999999:
        print("I'm sorry this journey is not possible")
    else:
        print("The route produced by the greedy algorithm is ", route, "it will cost ", totalPrice)