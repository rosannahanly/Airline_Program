'''
Created on 26 Apr 2018

@author: rosannahanly
'''

from classes import aircraft, airport, currencyExchange
import sys
from classes.flightPlan import FlightPlan

def main():
    airport.loadAirport('files/airport.csv')
    aircraft.loadAircraft('files/aircraft.csv')
    currencyExchange.loadCountryCurrency('files/countrycurrency.csv')
    currencyExchange.loadCurrencyRates('files/currencyrates.csv')
    
    if len(sys.argv) > 1:
        FlightPlan(sys.argv[1])
        #Atlas(sys.argv[1])
    else:
        #Atlas('files/test.csv') #This is the brute for method & will produce better answer but not as efficent
        FlightPlan('files/test.csv')

    
if __name__ == '__main__':
    main()
    print("The program has been terminated and the results are in the results.csv file")