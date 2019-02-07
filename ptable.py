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
                relx=100,
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
                relx=self.table.relx) 
        
        # Search button to activate info form
        self.button = self.add(npyscreen.ButtonPress,
                name="Search",
                begin_entry_at=12,
                rely=2,
                relx=self.table.relx+63,
                when_pressed_function = self.searchButton)
        
    
    
        ######################
        # Molarity Calcuator #
        ######################
                
        self.molarityCalc = self.add(npyscreen.BoxTitle,
                _contained_widget = npyscreen.TitleFixedText,
                relx = 1,
                rely = 17,
                editable = False,
                height = 24,
                width = 43,
                name = 'Solution Calcuator')
        
        self.label1 = self.add(npyscreen.TitleText,
                value = '- Concentration From Solute & Volume -',
                name = ' ',
                begin_entry_at = 1,
                use_two_lines = False,
                rely = self.molarityCalc.rely + 2,
                relx = self.molarityCalc.relx + 1,
                width = 41,
                height = 1,
                editable = False
                )

        mainForm.soluteMassField = self.add(npyscreen.TitleText,
                name = 'Mass of Solute (g):',
                use_two_lines = False,
                width = 30,
                relx = self.molarityCalc.relx+2,
                rely = self.molarityCalc.rely + 3,
                begin_entry_at = 20)

        mainForm.soluteMolarMassField = self.add(npyscreen.TitleText,
                name = 'Molar Mass of Solute (g/mol):',
                use_two_lines = False,
                width = 39,
                relx = self.molarityCalc.relx+2,
                rely = self.molarityCalc.rely + 4,
                begin_entry_at = 30)
         
        mainForm.volumeField = self.add(npyscreen.TitleText,
                name = 'Volume of Solution (L):',
                use_two_lines = False,
                width = 35,
                relx = self.molarityCalc.relx+2,
                rely = self.molarityCalc.rely + 5,
                begin_entry_at = 24)

        self.getConcentrations = self.add(solutionButton,
                relx = self.molarityCalc.relx+1,
                rely = self.molarityCalc.rely + 6,
                name = 'Calculate')
        
        mainForm.solutionGrid = self.add(npyscreen.SimpleGrid,
                values = [['']],
                width = 40,
                columns = 1,
                height = 3,
                column_width = 40,
                relx = self.molarityCalc.relx + 2,
                rely = self.molarityCalc.rely + 7)
        
        self.label2 = self.add(npyscreen.TitleText,
                value = '- Dilute Solution of Known Molarity -',
                name = ' ',
                begin_entry_at = 1,
                use_two_lines = False,
                rely = self.molarityCalc.rely + 10,
                relx = self.molarityCalc.relx + 1,
                width = 40,
                height = 1,
                editable = False
                )

        mainForm.stockConcentration = self.add(npyscreen.TitleText,
                name = 'Molarity of Stock (M):',
                relx = self.molarityCalc.relx + 2,
                rely = self.molarityCalc.rely + 11,
                use_two_lines = False,
                width = 35,
                begin_entry_at = 23)
        
        mainForm.desiredVolume = self.add(npyscreen.TitleText,
                name = 'Desired Final Volume (L):',
                relx = self.molarityCalc.relx + 2,
                rely = self.molarityCalc.rely + 12,
                use_two_lines = False,
                width = 35,
                begin_entry_at = 26)
        
        mainForm.desiredConcentration = self.add(npyscreen.TitleText,
                name = 'Desired Molarity (M):',
                relx = self.molarityCalc.relx + 2,
                rely = self.molarityCalc.rely + 13,
                use_two_lines = False,
                width = 35,
                begin_entry_at = 22)
        
        self.getReqVolume = self.add(concentrationButton,
                relx = self.molarityCalc.relx+1,
                rely = self.molarityCalc.rely + 14,
                name = 'Calculate')

        mainForm.concentrationGrid = self.add(npyscreen.SimpleGrid,
                values = [['']],
                width = 40,
                columns = 1,
                height = 1,
                column_width = 40,
                relx = self.molarityCalc.relx + 2,
                rely = self.molarityCalc.rely + 15)
        
        self.label3 = self.add(npyscreen.TitleText,
                value = '- Calc Mass Req. For Molar Solution -',
                name = ' ',
                begin_entry_at = 1,
                use_two_lines = False,
                rely = self.molarityCalc.rely + 17,
                relx = self.molarityCalc.relx + 1,
                width = 40,
                height = 1,
                editable = False
                )

        mainForm.formulaWeight = self.add(npyscreen.TitleText,
                name = 'Formula Weight (g/mol):',
                relx = self.molarityCalc.relx + 2,
                rely = self.molarityCalc.rely + 18,
                use_two_lines = False,
                width = 40,
                begin_entry_at = 23)
        
        mainForm.desiredVolume2 = self.add(npyscreen.TitleText,
                name = 'Desired Final Volume (L):',
                relx = self.molarityCalc.relx + 2,
                rely = self.molarityCalc.rely + 19,
                use_two_lines = False,
                width = 40,
                begin_entry_at = 26)
        
        mainForm.desiredConcentration2 = self.add(npyscreen.TitleText,
                name = 'Desired Molarity (M):',
                relx = self.molarityCalc.relx + 2,
                rely = self.molarityCalc.rely + 20,
                use_two_lines = False,
                width = 40,
                begin_entry_at = 22)
        
        self.getReqMass = self.add(reqMassButton,
                relx = self.molarityCalc.relx+1,
                rely = self.molarityCalc.rely + 21,
                name = 'Calculate')

        mainForm.reqMassGrid = self.add(npyscreen.SimpleGrid,
                values = [['']],
                width = 40,
                columns = 1,
                height = 1,
                column_width = 40,
                relx = self.molarityCalc.relx + 2,
                rely = self.molarityCalc.rely + 22)



        ######################
        # Chemistry Database #
        ######################
        
        self.database = self.add(npyscreen.BoxTitle,
                _contained_widget=npyscreen.TitleFixedText,
                title = "Useful Information",
                rely = 17,
                values = chemInfo,
                relx = 44,
                editable = True,
                editw = 1,
                width = 53,
                height = 24,
                name = 'Chemistry Database')
       
        self.testButton = self.add(databaseButton,
                relx = self.database.relx + 40,
                rely = self.database.rely + 1,
                name = "Expand"
                )
        
        ##############
        # Notes Area # 
        ##############
        self.notes = self.add(npyscreen.BoxTitle,
                _contained_widget=npyscreen.TitleText,
                title = "Notes",
                rely = self.database.rely,
                value = '',
                relx = self.database.relx+53,
                values =  ["", "Scratch sheet for notes, not saved on exit"],
                editable = True,
                editw = 1,
                width = 70,
                height = 24,
                name = 'Notes')

        self.notesField = self.add(npyscreen.MultiLineEdit,
                name = ':',
                relx = self.notes.relx+2,
                rely = self.notes.rely+2,
                use_two_lines = True,
                begin_entry_at = 2,
                width = 43)

        #####################
        # Equation Balancer #
        #####################
       
        # Box widget
        self.equationBalancer = self.add(npyscreen.BoxTitle,
                _contained_widget=npyscreen.TitleFixedText,
                name="Equation Balancer: CaCl₂ + AgNO₃ → Ca(NO₃)₂ + AgCl | CaCl2 + AgNO3 = Ca(NO3)2 + AgCl",
                values=[' '],
                relx=1,
                rely=9,
                width = 96,
                height = 8,
                editable=False)
        
        # Equation entry field
        mainForm.equationBalancerField = self.add(npyscreen.TitleText,
                name = ':',
                relx = self.equationBalancer.relx+1,
                rely = self.equationBalancer.rely+2,
                use_two_lines = False,
                begin_entry_at = 2,
                width = 45)

        # Solver output
        mainForm.equationBalancerOutput = self.add(npyscreen.FixedText,
                value = None,
                editable = True,
                use_two_lines = False,
                relx =  3,
                rely =  14,
                width = 40)       
        
        # Solve button
        mainForm.equationBalancerButton = self.add(solveButton,
                name = 'Solve',
                relx = self.equationBalancer.relx+75,
                rely = self.equationBalancer.rely+2,
                use_two_lines=False,
                editw=0,
                )
        

        
        
        #####################
        # Compound Analyzer #
        #####################
        
        # Box Widget
        self.compoundAnalyzer = self.add(npyscreen.BoxTitle,
                _contained_widget=npyscreen.TitleFixedText,
                name="Compound Analyzer",
                values=[' '],
                relx=1,
                rely=1,
                width = 96,
                height = 8,
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
                values = [['']],
                editable = True,
                use_two_lines=True,
                column_width = 73,
                relx = self.compoundAnalyzer.relx+3,
                rely = self.compoundAnalyzer.rely+4,
                height = 3,
                width = 73)       
        
        # Analyze button
        mainForm.compoundAnalyzerButton = self.add(analyzeButton,
                name = 'Analyze',
                relx = self.compoundAnalyzer.relx+75,
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
            mass = float(mainForm.soluteMassField.value)
            molarMass = float(mainForm.soluteMolarMassField.value)
            volume = float(mainForm.volumeField.value)
            moles = molarMass * mass

            conMolar = round(((mass/volume)/molarMass), 4) 
            conMass = round(((mass/volume)/10), 4)
            values = [['Molar Concentration (M): '+str(conMolar)], ['Mass Concentration (% w/v): '+str(conMass)]]
        except:
            values = [['Error: Try Again.']]
        
        mainForm.solutionGrid.values = values
        mainForm.solutionGrid.edit()
        
class concentrationButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.editing = False

        try:
            M1 = float(mainForm.stockConcentration.value)
            M2 = float(mainForm.desiredConcentration.value)
            V2 = float(mainForm.desiredVolume.value)
            if M2 > M1:
                values = [['Error: Concentration Must Decrease']]
            else:
                values = [['Required Volume (L): '+str(round(((V2*M2)/M1), 3))]]
        except:
            values = [['Error: Try Again.']]

        mainForm.concentrationGrid.values = values
        mainForm.concentrationGrid.edit()

class reqMassButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.editing = False
        try:
            mMass = float(mainForm.formulaWeight.value)
            finalVol = float(mainForm.desiredVolume2.value)
            finalCon = float(mainForm.desiredConcentration2.value)
            finalMass = round((finalCon*finalVol*mMass), 6)
            values = [['Req. Mass (g): '+str(finalMass)]]
            mainForm.reqMassGrid.values = values
        except:
            values = [['Error: Try Again']]
            mainForm.reqMassGrid.values = values
        
        mainForm.reqMassGrid.edit()


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
                editw = True
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

