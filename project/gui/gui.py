#We are going to be using Kivy for a main GUI and the included GUI Tkinter for a filechooser
#First download pygame then download Kivy. Here is the download site:
#http://www.lfd.uci.edu/~gohlke/pythonlibs/
#I tried downloading from the Kivy site but had lots of issues, 
#this site allowed the downloads to work on Windows OS and worked with Kivy's test code.
# Site for Linux version download http://kivy.org/#download


import string

from project.finite_automata.jsonToNFA import createNFA
from project.finite_automata.NFA import NFA
from project.regular_grammar.jsonToGrammar import createGrammar
from project.regular_grammar.Grammar import Grammar

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.clock import Clock
Clock.max_iteration = 20

from tkinter import Tk
from tkinter.filedialog import askopenfilename


#Main Widget
class Root(Widget):
    flag = 0
    def __init__(self):
        Widget.__init__(self)
        box = BoxLayout(orientation= 'vertical',
                        size = (600, 600))
        lblIntro = Label(text = "Please select which you would like to check:")
        btnNFA = Button(text = "NFA",
                        valign = 'middle',
                        halign = 'center')
        btnNFA.bind(on_press = self.pressed)
        btnNFA.bind(on_release = self.r1)


        btnGrm = Button(text = "Regular Grammars",
                        valign = 'middle',
                        halign = 'center')
        btnGrm.bind(on_press = self.pressed, on_release = self.r2)

        box.add_widget(lblIntro)
        box.add_widget(btnNFA)
        box.add_widget(btnGrm)
        self.add_widget(box)
    
    #These set the flag so the program knows that NFA or Regular Grammars was chosen
    def r1(self, event):
        self.flag = 1
    
    def r2(self, event):
        self.flag = 2

    #When user pushes any NFA or Regular Grammars button, this calls this popup 
    #to ask if they are importing a file or making a file for their rules
    def pressed(self,event):
        boxsave = BoxLayout(orientation = 'vertical')
        btnImport = Button(text = "Import a File",
                           valign = 'middle',
                           halign = 'center')
        btnImport.bind(on_press = self.importPress)

        btnMake = Button(text = "Create a New File",
                           valign = 'middle',
                           halign = 'center')
        btnMake.bind(on_press = self.makePress)
        
        lblSave = Label(text = "Would you Like to Import a File or Create a New File")
        
        for thing in [lblSave, btnImport, btnMake]:
            boxsave.add_widget(thing)
        
        ppu = Popup(title = "Import or Create File", 
                    content = boxsave,
                    size = (500,500), 
                    size_hint=(None, None),
                    auto_dismiss=True)
        ppu.open()
    
    #If user chooses to Make a File for the rules, then a popup is generated to save their  
    #rules in a .txt file then prompt for a string input to check against the rules. If for
    #NFA, then a popup appears asking whether the user wants to convert to DFA or check a string
    #against the rules
    def makePress (self,event):
        boxCheckConvert = BoxLayout(orientation = 'vertical')
        btnCheck = Button(text = "Check a String",
                           valign = 'middle',
                           halign = 'center',
                           size_hint = (1, .5))
        btnCheck.bind(on_press =  lambda but: self.savePress(event,txtInMake.text,txtFileName.text))
        btnConvert = Button(text = "Convert to DFA",
                           valign = 'middle',
                           halign = 'center',
                           size_hint = (1, .5))
        boxCheckConvert.add_widget(btnCheck)
        boxCheckConvert.add_widget(btnConvert)


        popCheckConvert = Popup(title = "Check String or Convert to DFA",
                           content = boxCheckConvert,
                           size = (400,400),
                           size_hint = (None, None),
                           auto_dismiss=True)


        boxMake1 = BoxLayout(orientation = 'vertical')
        lblMake1 = Label(text= "Please enter Rules")
        txtInMake1 = TextInput(text = '''{
						                    "Variables": [], 
						                    "alphabet": [], 
						                    "startVariable": "",  
						                    "Productions" : 
							                        {
                                                    
                                                    }
				                    	}''', size_hint = (1, 1.3))

        txtFileName1 = TextInput(text = "FileNameGrammar",
                        multiline = False)
        btnSave1 = Button(text = "Save File",
                           valign = 'middle',
                           halign = 'center')
        btnSave1.bind(on_press =  lambda but: self.savePress(event,txtInMake1.text,txtFileName1.text))
        
        for item1 in [lblMake1, txtInMake1,txtFileName1, btnSave1]:
            boxMake1.add_widget(item1)


        boxMake = BoxLayout(orientation = 'vertical')
        lblMake = Label(text= "Please enter Rules")
        txtInMake = TextInput(text = '''{
						                    "states": [], 
						                    "alphabet": [], 
						                    "startState": "", 
						                    "finalStates": [], 
						                    "moves" : 
							                        {
                                                    
                                                    }
				                    	}''', size_hint = (1, 1.3))

        txtFileName = TextInput(text = "File Name",
                        multiline = False)
        btnSave = Button(text = "Save File",
                           valign = 'middle',
                           halign = 'center')
        btnSave.bind(on_press = popCheckConvert.open)
              

        btnConvert.bind(on_press = lambda button: self.helper(event, txtFileName.text, txtInMake.text))



        for item in [lblMake, txtInMake,txtFileName, btnSave]:
            boxMake.add_widget(item)

        pop = Popup(title = "New File", 
                    content = boxMake,
                    size = (550,550), 
                    size_hint=(None, None),
                    auto_dismiss=True)

        btnSave.bind(on_release = pop.dismiss)


        pop1 = Popup(title = "New File", 
                    content = boxMake1,
                    size = (550,550), 
                    size_hint=(None, None),
                    auto_dismiss=True)

        btnSave.bind(on_release = pop1.dismiss)




        if self.flag == 1:
            pop.open()
        else:
            pop1.open()
    
            
    #This function helps the makePress function by allowing the function to call convertNFA 
    def helper (self, event, fileName, rules):
        tName = fileName + ".txt"
        newFile = open(tName, "w")
        newFile.write(rules)
        newFile.close()
        self.convertNFA(event, tName)
                        

    #If user chooses to Import a File, the File Chooser opens and they can select which file they wish 
    #to use as their rules. If selected in NFA, the program prompts whether they want to convert to DFA
    #or check a string against rules
    def importPress (self,event):
        boxInput = BoxLayout(orientation = 'vertical')
        lblInput = Label(text= "Please enter string you would like to test:")
        txtInput = TextInput()
        btnSaveInput = Button(text = "Save and Check",
                           valign = 'middle',
                           halign = 'center')
        btnSaveInput.bind(on_press = lambda butt: self.runIt(event,filename,txtInput.text))

        for thing in [lblInput, txtInput, btnSaveInput]:
            boxInput.add_widget(thing)

        popCompute = Popup(title = "Input String",
                           content = boxInput,
                           size = (500,500),
                           size_hint = (None, None),
                           auto_dismiss=True)


        boxCheckConvert = BoxLayout(orientation = 'vertical')
        btnCheck = Button(text = "Check a String",
                           valign = 'middle',
                           halign = 'center',
                           #size = (400,400),
                           size_hint = (1, .5))
        btnCheck.bind(on_press = popCompute.open)
        btnConvert = Button(text = "Convert to DFA",
                           valign = 'middle',
                           halign = 'center',
                           #size = (400,400),
                           size_hint = (1, .5))
        btnConvert.bind(on_press = lambda butto: self.convertNFA(event, filename))
        boxCheckConvert.add_widget(btnCheck)
        boxCheckConvert.add_widget(btnConvert)


        popCheckConvert = Popup(title = "Check String or Convert to DFA",
                           content = boxCheckConvert,
                           size = (400,400),
                           size_hint = (None, None),
                           auto_dismiss=True)

        Tk().withdraw()
        filename = askopenfilename()
        
        print(self.flag)

        if filename != "":
            if self.flag == 1 :
                popCheckConvert.open()
            else:
                popCompute.open()



    def savePress (self, event, rules, fname):
        tName = fname + ".txt"
        newFile = open(tName, "w")
        newFile.write(rules)

        boxInput = BoxLayout(orientation = 'vertical')
        lblInput = Label(text= "Please enter string you would like to test:")
        txtInput = TextInput()
        btnSaveInput = Button(text = "Save and Check",
                           valign = 'middle',
                           halign = 'center')
        btnSaveInput.bind(on_press = lambda butt: self.runIt(event,tName,txtInput.text))
        newFile.close()

        for thing in [lblInput, txtInput, btnSaveInput]:
            boxInput.add_widget(thing)

        popCompute = Popup(title = "Input String",
                           content = boxInput,
                           size = (500,500),
                           size_hint = (None, None),
                           auto_dismiss=True)
        popCompute.open()


    def popERROR (self, event):
        poperr = Popup(title = "ERROR",
                       content = Label(text = "Error occurred. \n Please make sure inputs/rules are correct \n Click outside popup to continue."),
                       size = (400,400),
                       size_hint = (None, None),
                       auto_dismiss=True)
        poperr.open()



    def convertNFA(self, event, fileName):
       file = open(fileName, "r")
       
       try:
           nfa = createNFA(file.read())
           result = nfa.toDFA()
       except AssertionError:
           self.popERROR(event)
           return

       popResult = Popup(title = "Result",
                    content = TextInput (text = result.__str__()),
                    size = (500,500),
                    size_hint = (None, None),
                    auto_dismiss=True)
       popResult.open()


    
    def runIt (self,event,fileName,strCheck):
       
       file = open(fileName, "r")
       
       if self.flag == 1:
           try:
               nfa = createNFA(file.read())
               result = nfa.isInLanguage(strCheck)
           except AssertionError:
               self.popERROR(event)
               return

           if result == True:
                resultstr = "True"
           else:
                resultstr = "False"

           popResult = Popup(title = "Result",
                             content = Label (text = resultstr),
                             size = (500,500),
                             size_hint = (None, None),
                             auto_dismiss=True)
           popResult.open()

       else:
           try:
               grammar = createGrammar(file.read())
               resultgr = grammar.isInLanguage(strCheck)
           except AssertionError:
               self.popERROR(event)
               return

           if resultgr == True:
                resultstrg = "True"
           else:
                resultstrg = "False"

           popResultg = Popup(title = "Result",
                             content = Label (text = resultstrg),
                             size = (500,500),
                             size_hint = (None, None),
                             auto_dismiss=True)
           popResultg.open()





#Execution app runs widget
class app1(App):
    def build(self):
        return Root()

#if __name__=="__main__":
app1().run()
