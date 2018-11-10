import sys
import npyscreen
import time
from collections import OrderedDict
from data import elementStats, chemInfo, tableElements, periods
   
 
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
            self.element.value=None
            npyscreen.notify_confirm("Sorry, that is not an element.", title='Really? Try again.', editw=1)
            self.edit()
        else:
            toInfo.element.values = info.setValues(info, self.typedElement)
            self.parentApp.switchForm("INFO")

    # Initialize table and text box
    def create(self):

        # Periodic table
        #self.table = self.add(pTable, values=pTable.elements, col_titles=pTable.periods, relx=2, rely=2, width=72, columns=18, editable=False)
        self.table = self.add(npyscreen.GridColTitles, values=tableElements, col_titles=periods, relx=2, rely=2, width=72, columns=18, editable=False)

        # Search bar to enter desired element
        self.element = self.add(npyscreen.TitleText, name="Element: ", begin_entry_at=12, rely=self.table.rely+13) 
        
        # Search button to activate info form
        self.button = self.add(npyscreen.ButtonPress, name="Search", begin_entry_at=12, rely=self.table.rely+15, relx=2, when_pressed_function=self.searchButton)
        
        # Adding info panel below table
        self.helpfulInfo = self.add(npyscreen.BoxTitle,
                _contained_widget=npyscreen.TitleFixedText,
                title="Useful Information",
                rely=self.button.rely+2,
                values=chemInfo,
                relx=2,
                editable=True,
                editw=1,
                width=80,
                name='Useful Info - Press L to search')

    # Switch to INFO form when OK is pressed
    def on_ok(self):
        sys.exit()        

class info(npyscreen.Form):
    
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

