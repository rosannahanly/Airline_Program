
from classes import airport, aircraft, currencyExchange
from classes.aircraft import Aircraft
from classes.airport import Airport
from classes.currencyExchange import CurrencyCode, CurrencyRate
#from atlas import Atlas


airport.loadAirport('..//files/airport.csv')
aircraft.loadAircraft('..//files/aircraft.csv')
currencyExchange.loadCountryCurrency('..//files/countrycurrency.csv')
currencyExchange.loadCurrencyRates('..//files/currencyrates.csv')


print(Airport.airportCount)
print(Aircraft.airplaneCount)
print(CurrencyCode.currencyCodeCount)
print(CurrencyRate.currencyRateCount)

#Atlas(.//files/testRouteData.csv)
#print(Atlas.getDistance("DUB", "LHR")



#print(Airport.airportDict)
#print(Aircraft.airplaneDict)
#print(CurrencyCode.currencyCodeDict)
#print(CurrencyRate.currencyRateDict)