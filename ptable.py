import sys
import npyscreen
from collections import OrderedDict

class elementData(npyscreen.SimpleGrid):
    
    
    # Meltpoints in K
    elements = {'H': OrderedDict([('Name:', 'Hydrogen'), ('Atomic Number:', 1), ('Group:', 1), ('Period:', 1), ('Block:', 's'), ('Category', 'Reactive Nonmetal'), ('Atomic Mass (u):', 1.00794), ('Electronegativity:', 2.20), ('Electron Configuration:', '1s¹'), ('Phase at STP:', 'Gas'), ('Melting Point (K):', 13.99), ('Boiling Point (K):', 20.271), ('Density at STP (g/L):', 0.08988), ('Triple Point (K):', 13.8033), ('Critical Point (K):', 32.938), ('Heat Capacity (J/(mol·K)):', 28.836), ('Oxidation States:', '-1, +1'), ('Covalent Radius (pm):', '31±5'), ('Van Der Waals Radius (pm):', 120), ('Crystal Structure:', 'Hexagonal'), ('Speed of Sound (gas, 27˚C, m/s)', 1310), ('Thermal Conductivity (W/(m·K))', 0.1805), ('Magnetic Ordering:', 'Diamagnetic')]),
    
            'He': OrderedDict([('Name:', 'Helium'), ('Atomic Number:', 2), ('Group:', 18), ('Period:', 1), ('Block:', 's'), ('Category', 'Noble Gas'), ('Atomic Mass (u):', 4.002602), ('Electronegativity:', 'No Data'), ('Electron Configuration:', '1s²'), ('Phase at STP:', 'Gas'), ('Melting Point (K):', 0.95), ('Boiling Point (K):', 4.222), ('Density at STP (g/L):', 0.1786), (' → at Melting Point (g/cm³):', 0.145), ('Triple Point (K):', 2.117), ('Critical Point (K):', 5.1953), ('Heat Capacity (J/(mol·K)):', 20.78), ('Oxidation States:', '0'), ('Covalent Radius (pm):', '28'), ('Van Der Waals Radius (pm):', 140), ('Crystal Structure:', 'Hexagonal Close-Packed'), ('Thermal Conductivity (W/(m·K))', 0.1513), ('Magnetic Ordering:', 'Diamagnetic')]),


            'Li': OrderedDict([('Name:', 'Lithium'), ('Atomic Number:', 3), ('Group:', 1), ('Period:', 2), ('Block:', 's'), ('Category', 'Alkali Metal'), ('Atomic Mass (u):', 6.94), ('Electronegativity:', 0.98), ('Electron Configuration:', '[He]2s¹'), ('Phase at STP:', 'Solid'), ('Melting Point (K):', 453.65), ('Boiling Point (K):', 1603), ('Density at RT (g/cm³):', 0.534), (' → at Melting Point (g/cm³):', 0.512), ('Critical Point (K):', 3220), ('Heat of Fusion (kJ/mol):', 3.00 ), ('Heat of Vaporization (kJ/mol):', 136), ('Heat Capacity (J/(mol·K)):', 24.860), ('Oxidation States:', '+1'), ('Atomic Radius (pm):', 152), ('Covalent Radius (pm):', '128±7'), ('Van Der Waals Radius (pm):', 182), ('Crystal Structure:', 'Body-Centric Cubic'), ('Thermal Expansion at 25˚C: (µm/(m·K))', 46), ('Thermal Conductivity (W/(m·K))', 84.8), ('Electrical Resistivity at 25˚C (nΩ·m)', 98.2), ('Magnetic Ordering:', 'Paramagnetic')]),
                
            
            'Be': OrderedDict([('Name:', 'Beryllium'), ('Atomic Number:', 4), ('Group:', 2), ('Period:', 2), ('Block:', 's'), ('Category', 'Alkaline Earth Metal'), ('Atomic Mass (u):', 9.012), ('Electronegativity:', 1.57), ('Electron Configuration:', '[He]2s²'), ('Phase at STP:', 'Solid'), ('Melting Point (K):', 1560), ('Boiling Point (K):', 2742), ('Density at RT (g/cm³):', 1.85), (' → at Melting Point (g/cm³):', 1.690), ('Critical Point (K):', 5205), ('Heat of Fusion (kJ/mol):', 12.2 ), ('Heat of Vaporization (kJ/mol):', 292), ('Heat Capacity (J/(mol·K)):', 16.443), ('Oxidation States:', '+2, +1'), ('Atomic Radius (pm):', 112), ('Covalent Radius (pm):', '96±3'), ('Van Der Waals Radius (pm):', 153)]),
                

                }

    

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
class mainForm(npyscreen.ActionFormMinimal):

    # Enables editing and points to next form
    def activate(self):
        self.edit()
        self.parentApp.setNextForm("INFO")

    # Function called when user presses search
    def searchButton(self):
        # set variable in parent app to user input
        self.typedElement = self.element.value

        # Object representing Info form
        toInfo = self.parentApp.getForm("INFO")

        # Setting info grid values from relevant element data
        toInfo.element.values = info.setValues(info, self.typedElement)

        self.parentApp.switchForm("INFO")

    # Initialize table and text box
    def create(self):
        self.table = self.add(pTable, values=pTable.elements, col_titles=pTable.periods, relx=2, rely=2, width=72, columns=18, editable=False)
        self.element = self.add(npyscreen.TitleText, name="Element: ", begin_entry_at=12, rely=self.table.rely+13) 
        self.button = self.add(npyscreen.ButtonPress, name="Search", begin_entry_at=12, rely=self.table.rely+15, relx=2, when_pressed_function=self.searchButton)
    
    # Switch to INFO form when OK is pressed
    def on_ok(self):
        sys.exit()        

class info(npyscreen.Form):
    
    def setValues(self, element):
        
        # Dictionary of element properties
        properties = elementData.elements[element]
        
        # Values to pass to info grid
        values = []
        
        for key in list(properties):
            datum = []
            datum.append(key)
            datum.append(properties[key])
            values.append(datum)
        return values

    # Enables editing and points to next form
    def activate(self):
        self.edit()
        self.parentApp.setNextForm("MAIN")
        mainForm = self.parentApp.getForm("MAIN")
        mainForm.element.value=None
    
    # Initialize information
    def create(self):
        self.element = self.add(elementData, editable=False, width=160)

####################################
# App and Form initialized and run #
####################################
class myTUI(npyscreen.NPSAppManaged):
    

    def onStart(self):
        firstForm = self.addForm("MAIN", mainForm, name="Periodic Table")
        secondForm = self.addForm("INFO", info, name="Information")

if __name__ == "__main__":
    npyscreen.wrapper(myTUI().run())

