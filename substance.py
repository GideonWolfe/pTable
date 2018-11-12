from chempy import Substance
from chempy import mass_fractions
from chempy import balance_stoichiometry
from chempy import *
import collections
import data

def analyze(equation):
    try:
        # Gets elemental symbol for given atomic number
        def getSymbol(atomicNum):
            symbol = '' 
            for element in data.elementStats.keys():
                elementInfo = data.elementStats[element]
                if elementInfo['Atomic Number:'] == atomicNum:
                    symbol = element
                else:
                    continue
            return symbol

        
        # Initializing empty list
        inputList = []
        
        # Parsing substance from formula
        substance = Substance.from_formula(equation)
        
        # Adding tuples to inputList
        for element in substance.composition.keys():
            inputList.append((getSymbol(element), substance.composition[element]))

        # Casting to OrderedDict
        inputList = collections.OrderedDict(inputList)

        # Actually getting mass percents
        massPercents = mass_fractions(inputList)
        
        # Result
        outputStr = str()
        
        # Build result string
        for element in massPercents.keys():
            valueDecimal = round(massPercents[element], 3)
            valuePercent = round(valueDecimal*100, 3)
            outputStr += element+': '+str(valueDecimal)+' ('+str(valuePercent)+'%) '

        return outputStr
    
    except:
        return "Error: Check Formatting"

