from chempy import balance_stoichiometry
from chempy import Substance
from chempy import Reaction


def solveEq(userString):
    
    try:    
        outputString = ''
        bothSides = userString.split(' = ')
        reactants = set(bothSides[0].split(' + '))
        products = set(bothSides[1].split(' + '))

        reac, prod = balance_stoichiometry(reactants, products)

        count = 0
        for i in dict(reac):
            count += 1
            outputString += str(reac[i])

            if(count == len(dict(reac))):
                addedStr = str(Substance.from_formula(i).unicode_name)
                outputString += addedStr
                continue
            else:
                addedStr = str(Substance.from_formula(i).unicode_name)
                outputString += addedStr + ' + '
            

        outputString += ' → '

        count = 0
        for i in dict(prod):
            count += 1
            outputString += str(prod[i])

            if(count == len(dict(prod))):

                addedStr = str(Substance.from_formula(i).unicode_name)
                outputString += addedStr
                continue
             
            else:
                addedStr = str(Substance.from_formula(i).unicode_name)
                outputString += addedStr + ' + '

        
        return outputString
    
    except:
        return('Error: Unsolveable or Bad Formatting')

