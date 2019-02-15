from chempy import Substance
from chempy import mass_fractions
from chempy import balance_stoichiometry
from chempy import *
import collections
import data
from chempy.units import default_units as u
from mendeleev import element as e

def analyze(equation):
    

    # Parsing substance from formula
    try:
        substance = Substance.from_formula(equation)
    except:
        return [["Error: Check Formatting"]]

    try:
        # Gets elemental symbol for given atomic number
        def getSymbol(atomicNum):
            intElement = int(atomicNum)
            myElement = e(intElement)
            return(str(myElement.symbol))

        
        # Initializing empty list
        inputList = []
        
        
        # Adding tuples to inputList

        # No charge stat, ie element
        if 0 not in substance.composition.keys():
            for element in substance.composition.keys():
                inputList.append((getSymbol(element), substance.composition[element]))
        else:
            for element in substance.composition.keys():
                if element != 0:
                    inputList.append((getSymbol(element), substance.composition[element]))
                


        # Casting to OrderedDict
        inputList = collections.OrderedDict(inputList)

        # Actually getting mass percents
        massPercents = mass_fractions(inputList)
        
        # Result
        mpStr = str()
        
        # Build result string
        for element in massPercents.keys():
            valueDecimal = round(massPercents[element], 3)
            valuePercent = round(valueDecimal*100, 3)
            mpStr += element+': ('+str(valuePercent)+'%) '
        
        
        outputList = [['Molar Mass: ' + str(substance.molar_mass(u))],
                ['Mass %\'s: ' + str(mpStr)],
                ['Charge: ' + str(substance.charge)]]

        return outputList
    except:
        return [["Error: Something went wrong"]]
