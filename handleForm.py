from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates, CurrencyCodes
from collections import OrderedDict 

c = CurrencyRates()
currencySymbols=CurrencyCodes()
result = []
class Survey():
    def __init__(self, convertFrom, convertTo, value):
        self.convertFrom=convertFrom 
        self.convertTo=convertTo
        self.value=value
        
    def convertCurrency(self):
        
        currencyFrom = self.convertFrom
        currencyTo = self.convertTo
        getValue = int(self.value)
        resultSymbol = currencySymbols.get_symbol(currencyTo)
        result = c.convert(currencyFrom, currencyTo, getValue)
        
        return dict({resultSymbol: result})
  
        
        