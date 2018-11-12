from chempy import balance_stoichiometry
import ast
from pprint import pprint
from chempy import Equilibrium
from sympy import symbols



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
                outputString += str(i)
                continue
            else:
                outputString += str(i + ' + ')
            

        outputString += ' → '

        count = 0
        for i in dict(prod):
            count += 1
            outputString += str(prod[i])

            if(count == len(dict(prod))):
                outputString += str(i)
                continue
            else:
                outputString += str(i + ' + ')
        return outputString
    except:
        return('Error, check format')

