

#import atlas
#from atlas import DistanceBetweenAirports, airports
#print(DistanceBetweenAirports(53.666, -6.432, 53.7777, -4.5555))
from classes import aircraft, airport
from classes import currencyExchange
#from atlas import shortestPath, greedyAlgo
import csv

def readRouteData(fileName): #read test route data file and load into the memory
    with open(fileName, encoding = "utf8", errors = 'replace') as f:
        reader = csv.reader(f)
        for row in reader:
            pass
            #shortestPath(row)

def readRouteData2(fileName): #read test route data file and load into the memory
    with open(fileName, encoding = "utf8", errors = 'replace') as f:
        reader = csv.reader(f)
        for row in reader:
            pass
            #greedyAlgo(row)

def main():
    
    #airport.loadAirports('..//files/airport.csv')
    aircraft.loadAircraft('..//files/aircraft.csv')
    currencyExchange.loadCountryCurrency('..//files/countrycurrency.csv')
    currencyExchange.loadCurrencyRates('..//files/currencyrates.csv')
    readRouteData('..//files/testRouteData.csv')
    #readRouteData2('..//files/testRouteData.csv')
    
if __name__ == '__main__':
    main()

