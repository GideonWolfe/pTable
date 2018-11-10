import sys
import npyscreen
import time
from collections import OrderedDict
from data import elementStats, chemInfo, tableElements, periods
from equationBalancer import balance   

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
        if  (info.setValues(info, self.typedElement)) == False:
            self.element.value = None
            npyscreen.notify_confirm("Sorry, that is not an element.", title='Really? Try again.', editw=1)
            self.edit()
        else:
            toInfo.element.values = info.setValues(info, self.typedElement)
            self.parentApp.switchForm("INFO")
            self.element.editing = True

    # Initialize table and text box
    def create(self):

        # Periodic table
        self.table = self.add(npyscreen.GridColTitles,
                values=tableElements,
                col_titles=periods,
                relx=2,
                rely=4,
                width=73,
                columns=18,
                editable=False)

        # Search bar to enter desired element
        self.element = self.add(npyscreen.TitleText,
                name="Element Lookup: ",
                use_two_lines = False,
                begin_entry_at = 16,
                width = 30,
                rely=2,
                relx=2) 
        
        # Search button to activate info form
        self.button = self.add(npyscreen.ButtonPress,
                name="Search",
                begin_entry_at=12,
                rely=2,
                relx=35,
                when_pressed_function = self.searchButton)
        
        # Adding info panel below table
        self.helpfulInfo = self.add(npyscreen.BoxTitle,
                _contained_widget=npyscreen.TitleFixedText,
                title = "Useful Information",
                rely = 3,
                values = chemInfo,
                relx = 77,
                editable = True,
                editw = 1,
                width = 73,
                height = 37,
                name = 'Chemistry Database')
        
        self.equationBalancer = self.add(npyscreen.BoxTitle,
                _contained_widget=npyscreen.TitleFixedText,
                name="Equation Balancer: Use format below",
                values=[' ', 'C₇H₁₆ + O₂ → CO₂ + H₂O | C7H16+O2->CO2+H2O'],
                relx=2,
                rely=19,
                width = 72,
                height = 9,
                editable=False)
        
        self.equationBalancerField = self.add(npyscreen.TitleText,
                name = ':',
                relx = 3,
                rely = 23,
                use_two_lines = False,
                begin_entry_at = 2,
                width = 45)

        self.equationBalancerOutput = self.add(npyscreen.FixedText,
                relx = 2,
                rely = 26,
                width = 20,
                value = None)
        

        self.molarMassCalculator = self.add(npyscreen.BoxTitle,
                _contained_widget=npyscreen.TitleFixedText,
                name="Molar Mass Calculator:",
                values=[' '],
                relx=2,
                rely=28,
                width = 72,
                height = 12,
                editable=False)


        #TODO add solver button
        #self.equationBalancerButton = self.add(solveButton,
        #        relx=76,
        #        rely=25,
        #        width = 5, 
        #        name='Solve',)


    # Exit program form when OK is pressed
    def on_ok(self):
        sys.exit()        

class info(npyscreen.Form):
   
    # Generate list of properties for input element
    def setValues(self, element):
        
        # Check to see if user input is valid
        if element not in elementStats.keys():
            return False
        
        # Dictionary of element properties
        properties = elementStats[element]
        
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
        self.element = self.add(npyscreen.SimpleGrid, editable=False, width=160, editw=0)

####################################
# App and Form initialized and run #
####################################
class myTUI(npyscreen.NPSAppManaged):
    

    def onStart(self):
        self.addForm("INFO", info, name="Information")
        self.addForm("MAIN", mainForm, name="Periodic Table")


if __name__ == "__main__":
    npyscreen.wrapper(myTUI().run())

