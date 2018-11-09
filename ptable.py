import npyscreen

class elementData(npyscreen.SimpleGrid):
    
    
    # Meltpoints in K
    elements = {'H': {'name': 'Hydrogen', 'atomicNumber': 1, 'group': 1, 'period': 1, 'block': 's', 'category':'Reactive Nonmetal', 'atomicMass': 1.00794, 'electronegativity': 2.20, 'electronConfig': '1s¹', 'STPphase': 'Gas', 'meltPoint': 13.99, 'boilPoint': 20.271, 'STPdensity': 0.08988, 'triplePoint': 13.8033, 'critPoint': 32.938, 'heatCap': 28.836, 'oxStates': '-1, +1', 'covRadius': '31±5', 'vdwRadius': 120, },
 
                'He': {'name': 'Helium', 'atomicNumber': 2, 'group': 18, 'period': 1, 'block': 's', 'category':'Noble Gas', 'atomicMass': 4.002602, 'electronegativity': 'No Data', 'electronConfig': '1s²', 'STPphase': 'Gas', 'meltPoint': 0.95, 'boilPoint': 4.222, 'STPdensity': 0.1786, 'triplePoint': 2.177, 'critPoint': 5.1953, 'heatCap': 20.78, 'oxStates': '0', 'covRadius': '28', 'vdwRadius': 140, },

                'Li': {'name': 'Lithium', 'atomicNumber': 3, 'group': 1, 'period': 2, 'block': 's', 'category':'Alkali Metal', 'atomicMass': 6.94, 'electronegativity': 0.98, 'electronConfig': '[He]2s¹', 'STPphase': 'Solid', 'meltPoint': 453.65, 'boilPoint': 1603, 'STPdensity': '0.534 g/cm³', 'triplePoint': 'None', 'critPoint': 3220, 'heatCap': 24.860, 'oxStates': '+1', 'covRadius': '128±7', 'vdwRadius': 182, },
                
                'Be': {'name': 'Beryllium', 'atomicNumber': 4, 'group': 2, 'period': 2, 'block': 's', 'category':'Alkaline Earth Metal', 'atomicMass': 9.012, 'electronegativity': 1.57, 'electronConfig': '[He]2s²', 'STPphase': 'Solid', 'meltPoint': 1560, 'boilPoint': 2742, 'STPdensity': '1.85 g/cm³', 'triplePoint': 'None', 'critPoint': 3220, 'heatCap': 28.863, 'oxStates': '-1, +1', 'covRadius': '31±5', 'vdwRadius': 120, }


                }

    # Takes Element as argument, returns a list of values for grid 
    

class pTable(npyscreen.GridColTitles, npyscreen.ButtonPress):
    
    # Array of numbers used to lable the periods of the table
    periods = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']

    # 2D array of cells that represent the elements in the periodic table
    elements = [['H ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'He'], 
                ['Li', 'Be', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'B ', 'C ', 'N ', 'O ', 'F ', 'Ne'], 
                ['Na', 'Mg', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'Al', 'Si', 'P ', 'S ', 'Cl', 'Ar'],
                ['K ', 'Ca', 'Sc', 'Ti', 'V ', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr'],
                ['Rb', 'Sr', 'Y ', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I ', 'Xe'], 
                ['Cs', 'Ba', '↓ ', 'Hf', 'Ta', 'W ', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn'], 
                ['Fr', 'Ra', '↓ ', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'],
                ['  ', '  ', '↓ ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['  ', '  ', '→ ', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu'],
                ['  ', '  ', '→ ', 'Ac', 'Th', 'Pa', 'U ', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
                ]
        
 
# Main form with a periodic table and text box
class mainForm(npyscreen.ActionForm):

    # Enables editing and points to next form
    def activate(self):
        self.edit()
        self.parentApp.setNextForm("INFO")

    # Initialize table and text box
    def create(self):
        self.table = self.add(pTable, values=pTable.elements, col_titles=pTable.periods, relx=5, rely=2, width=80, columns=18, editable=False)
        self.element = self.add(npyscreen.TitleText, name="Element: ", begin_entry_at=12, rely=self.table.rely+13) 

    def getTypedElement(self):
        typedElement = self.element.value
        return typedElement

    # Switch to INFO form when OK is pressed
    def on_ok(self):
        
        # set variable in parent app to user input
        self.typedElement = self.element.value

        # Object representing Info form
        toInfo = self.parentApp.getForm("INFO")

        # Setting info grid values from relevant element data
        toInfo.element.values = info.setValues(info, self.typedElement)

        
        self.parentApp.switchForm("INFO")

class info(npyscreen.Form):
    
    def setValues(self, element):
        properties = elementData.elements[element]
        values = [['Name:', properties['name']],
                  [' '],
                  ['Period:', properties['period']],
                  ['Group:', properties['group']],
                  ['Block:', properties['block']],
                  ['Category:', properties['category']],
                  ['Atomic Number:', properties['atomicNumber']], 
                  ['Atomic Mass (Amu):', properties['atomicMass']],
                  ['Electronegativity:', properties['electronegativity']],
                  ['Electron Configuration:', properties['electronConfig']], 
                  ['Phase at STP:', properties['STPphase']], 
                  ['Density at STP (g/L):', properties['STPdensity']],
                  ['Melting Point (K):', properties['meltPoint']],
                  ['Boiling Point (K):', properties['boilPoint']],
                  ['Triple Point (K):', properties['triplePoint']],
                  ['Critical Point (K):', properties['critPoint']],
                  ['Oxidation States:', properties['oxStates']],
                  ['Heat Capacity (J/(mol·K)):', properties['heatCap']],
                  ['Covalent Radius (pm):', properties['covRadius']],
                  ['Van der Wal Radius (pm):', properties['vdwRadius']]
                  ]
        return values

    # Enables editing and points to next form
    def activate(self):
        self.edit()
        self.parentApp.setNextForm("MAIN")
    
    # Initialize information
    def create(self):
        self.element = self.add(elementData, editable=False, width=115)

####################################
# App and Form initialized and run #
####################################
class myTUI(npyscreen.NPSAppManaged):
    
    #typedElement = 'Ar'

    def onStart(self):
        firstForm = self.addForm("MAIN", mainForm, name="Periodic Table")
        secondForm = self.addForm("INFO", info, name="Information")

if __name__ == "__main__":
    npyscreen.wrapper(myTUI().run())

