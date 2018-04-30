'''
Created on 2 Apr 2018

@author: rosannahanly
'''
import csv

class CurrencyCode:
    '''
    Class to store currency codes for all countries
    '''
    currencyCodeDict = {}
    currencyCodeCount = 0

    def __init__(self, countryName, currencyCode):
        self.countryName = countryName
        self.currencyCode = currencyCode
        CurrencyCode.currencyCodeCount += 1
        CurrencyCode.currencyCodeDict[self.countryName] = self
        #currencyCode.currencyCodeDict[self.countryName] = self

def loadCountryCurrency(fileName): 
    with open(fileName, 'r', encoding="utf-8", errors = 'replace') as f:
        reader = csv.reader(f)
        for row in reader:
            CurrencyCode(row[0],row[14])
       

class CurrencyRate:
    '''
    Class to hold the toEuro Rate for each currency
    '''
    currencyRateDict = {}
    currencyRateCount = 0
    
    def __init__(self, currencyCode, toEuroRate):
        self.currencyCode = currencyCode
        self.toEuroRate = toEuroRate
        CurrencyRate.currencyRateCount +=1
        CurrencyRate.currencyRateDict[currencyCode] = self
    
            
def loadCurrencyRates(filename):
    with open(filename, 'rt', encoding = "utf8", errors = 'replace') as f:
        reader = csv.reader(f)
        for row in reader:
            CurrencyRate(row[1], row[2])      
