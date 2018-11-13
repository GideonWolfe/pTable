import sys
import npyscreen
import time
from collections import OrderedDict
from data import elementStats, chemInfo, tableElements, periods
from solve import solveEq
from substance import analyze 

#############################
##                         ##  
##       MAIN FORM         ##
##                         ##
#############################
class mainForm(npyscreen.ActionFormMinimal):

    # Enables editing and points to next form
    def activate(self):
        self.edit()
    

    # Function called when user presses search
    def searchButton(self):
        # set variable to user input
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

        ##################
        # Periodic Table #
        ##################

        # Periodic table
        self.table = self.add(npyscreen.GridColTitles,
                values=tableElements,
                col_titles=periods,
                relx=3,
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
                relx=3) 
        
        # Search button to activate info form
        self.button = self.add(npyscreen.ButtonPress,
                name="Search",
                begin_entry_at=12,
                rely=2,
                relx=36,
                when_pressed_function = self.searchButton)
        
    
    
        ######################
        # Molarity Calcuator #
        ######################
                
        self.molarityCalc = self.add(npyscreen.BoxTitle,
                _contained_widget = npyscreen.TitleFixedText,
                relx = self.table.relx+74,
                rely = 2,
                editable = False,
                height = 16,
                width = 71,
                name = 'Molarity Calcuator')
        
        mainForm.soluteMassField = self.add(npyscreen.TitleText,
                name = 'Mass of Solute (g):',
                use_two_lines = False,
                width = 35,
                relx = self.molarityCalc.relx+2,
                rely = self.molarityCalc.rely + 2,
                begin_entry_at = 20)

        mainForm.soluteMolarMassField = self.add(npyscreen.TitleText,
                name = 'Molar Mass of Solute (g/mol):',
                use_two_lines = False,
                width = 40,
                relx = self.molarityCalc.relx+2,
                rely = self.molarityCalc.rely + 3,
                begin_entry_at = 30)
         
        mainForm.volumeField = self.add(npyscreen.TitleText,
                name = 'Volume of Solution (L):',
                use_two_lines = False,
                width = 35,
                relx = self.molarityCalc.relx+2,
                rely = self.molarityCalc.rely + 4,
                begin_entry_at = 24)

        self.getConcentrations = self.add(solutionButton,
                relx = self.molarityCalc.relx+1,
                rely = self.molarityCalc.rely + 5,
                name = 'Calculate')
        
        mainForm.solutionGrid = self.add(npyscreen.SimpleGrid,
                width = 65,
                columns = 2,
                height = 3,
                column_width = 62,
                relx = self.molarityCalc.relx + 2,
                rely = self.molarityCalc.rely + 7)

                
        ######################
        # Chemistry Database #
        ######################
        
        self.database = self.add(npyscreen.BoxTitle,
                _contained_widget=npyscreen.TitleFixedText,
                title = "Useful Information",
                rely = 19,
                values = chemInfo,
                relx = 77,
                editable = True,
                editw = 1,
                width = 73,
                height = 21,
                name = 'Chemistry Database')
       
        self.testButton = self.add(databaseButton,
                relx = self.database.relx + 55,
                rely = self.database.rely + 1,
                name = "Expand"
                )
        
        #####################
        # Equation Balancer #
        #####################
       
        # Box widget
        self.equationBalancer = self.add(npyscreen.BoxTitle,
                _contained_widget=npyscreen.TitleFixedText,
                name="Equation Balancer: Use Format Below. Output Scrolls",
                values=[' ', 'CaCl₂ + AgNO₃ → Ca(NO₃)₂ + AgCl || CaCl2 + AgNO3 = Ca(NO3)2 + AgCl'],
                relx=2,
                rely=19,
                width = 72,
                height = 9,
                editable=False)
        
        # Equation entry field
        mainForm.equationBalancerField = self.add(npyscreen.TitleText,
                name = ':',
                relx = self.equationBalancer.relx+1,
                rely = self.equationBalancer.rely+4,
                use_two_lines = False,
                begin_entry_at = 2,
                width = 45)

        # Solver output
        mainForm.equationBalancerOutput = self.add(npyscreen.FixedText,
                value = None,
                editable = True,
                relx = 5,
                rely = 25,
                width = 40)       
        
        # Solve button
        mainForm.equationBalancerButton = self.add(solveButton,
                name = 'Solve',
                relx = 50,
                rely = 23,
                use_two_lines=False,
                editw=0,
                )
        

        
        
        #####################
        # Compound Analyzer #
        #####################
        
        # Box Widget
        self.compoundAnalyzer = self.add(npyscreen.BoxTitle,
                _contained_widget=npyscreen.TitleFixedText,
                name="Compound Analyzer: Use Above Format",
                values=[' '],
                relx=2,
                rely=28,
                width = 72,
                height = 12,
                editable=False)
        
        # Entry Field
        mainForm.compoundAnalyzerField = self.add(npyscreen.TitleText,
                name = ':',
                relx = self.compoundAnalyzer.relx+1,
                rely = self.compoundAnalyzer.rely+2,
                use_two_lines = False,
                begin_entry_at = 2,
                width = 45)
        

        # Analyzer output
        mainForm.compoundAnalyzerOutput = self.add(npyscreen.SimpleGrid,
                value = None,
                editable = True,
                use_two_lines=True,
                column_width = 44,
                relx = self.compoundAnalyzer.relx+3,
                rely = self.compoundAnalyzer.rely+5,
                height = 3,
                width = 65)       
        
        # Analyze button
        mainForm.compoundAnalyzerButton = self.add(analyzeButton,
                name = 'Analyze',
                relx = self.compoundAnalyzer.relx+48,
                rely = self.compoundAnalyzer.rely+2,
                use_two_lines=False,
                editw=0,
                )



    # Exit program form when OK is pressed
    def on_ok(self):
        sys.exit()        




#############################
##                         ##  
##       INFO FORM         ##
##                         ##
#############################

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
        self.element = self.add(npyscreen.SimpleGrid, editable=False, width=235, editw=0)


####################
#                  #
#  Button Classes  #
#                  # 
####################
class solveButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.editing = False
        mainForm.equationBalancerOutput.value = solveEq(mainForm.equationBalancerField.value)
        mainForm.equationBalancerOutput.edit()

class databaseButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.editing = False
        self.parent.parentApp.switchForm("DATABASE")

class analyzeButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.editing = False
        mainForm.compoundAnalyzerOutput.values = analyze(mainForm.compoundAnalyzerField.value)
        mainForm.compoundAnalyzerOutput.edit()

class solutionButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.editing = False
        try:
            conMolar = round(float(mainForm.soluteMassField.value)/float(mainForm.volumeField.value), 4) 
            conMass = round(conMolar/float(mainForm.soluteMolarMassField.value), 4)
            values = [['Molar Concentration (M): '+str(conMolar)], ['Mass Concentration (% w/v): '+str(conMass)]]
        except:
            values = [['Error: Try Again.']]
        
        mainForm.solutionGrid.values = values
        mainForm.solutionGrid.edit()
        

###################
#                 #
#  Database Form  #
#                 #
###################
class database(npyscreen.Form):
    
    # Enables editing and points to next form
    def activate(self):
        self.edit()
        self.parentApp.setNextForm("MAIN")
    
    # Initialize information
    def create(self):
        self.add(npyscreen.BoxTitle,
                _contained_widget=npyscreen.TitleFixedText,
                title = "Chemistry Database",
                rely = 1,
                relx = 1,
                height = 40,
                width = 167,
                values = chemInfo,
                editable = True,
                )


####################################
# App and Form initialized and run #
####################################
class myTUI(npyscreen.NPSAppManaged):
    
    def onStart(self):
        self.addForm("INFO", info, name="Information")
        self.addForm("MAIN", mainForm, name="pTable")
        self.addForm("DATABASE", database, name="Chemistry Database")

if __name__ == "__main__":
    npyscreen.wrapper(myTUI().run())

