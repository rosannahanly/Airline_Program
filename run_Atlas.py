'''
Created on 30 Apr 2018

@author: rosannahanly
'''

from classes import airport, aircraft, currencyExchange
from classes.atlas import Atlas
import sys 

def main():
    airport.loadAirport('files/airport.csv')
    aircraft.loadAircraft('files/aircraft.csv')
    currencyExchange.loadCountryCurrency('files/countrycurrency.csv')
    currencyExchange.loadCurrencyRates('files/currencyrates.csv')
    
    if len(sys.argv) > 1:
        Atlas(sys.argv[1])
    else:
        Atlas('files/test.csv') 
        

    
if __name__ == '__main__':
    main()
    print("The program has been terminated and the results are in the results.csv file")

if __name__ == '__main__':
    pass