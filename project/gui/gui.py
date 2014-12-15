#We are going to be using Kivy for a main GUI and the included GUI Tkinter for a filechooser
#First download pygame then download Kivy. Here is the download site:
#http://www.lfd.uci.edu/~gohlke/pythonlibs/
#I tried downloading from the Kivy site but had lots of issues, 
#this site allowed the downloads to work on Windows OS and worked with Kivy's test code.
# Site for Linux version download http://kivy.org/#download, not yet tested


import string

from project.finite_automata.jsonToNFA import createNFA
from project.finite_automata.NFA import NFA

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
    newFile = ""
    impFile = ""
    input = ""
    rule = ""
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

        #dont need DFA
        btnDFA = Button(text = "DFA",
                        valign = 'middle',
                        halign = 'center')
        btnDFA.bind(on_press = self.pressed, on_release = self.r2)

        btnGrm = Button(text = "Regular Grammars",
                        valign = 'middle',
                        halign = 'center')
        btnGrm.bind(on_press = self.pressed, on_release = self.r3)

        box.add_widget(lblIntro)
        box.add_widget(btnNFA)
        box.add_widget(btnDFA)
        box.add_widget(btnGrm)
        self.add_widget(box)
    
    #These set the flag so the program knows which function to use to check string
    def r1(self, event):
        self.flag = 1

    def r2(self, event):
        self.flag = 2

    def r3(self, event):
        self.flag = 3

    #When user pushes any NFA,DFA, or Regular Grammars button, this calls this popup 
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
    #rules in a .txt file then prompt for a string input to check against the rules 
    def makePress (self,event):
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
        btnSave.bind(on_press =  lambda but: self.savePress(event,txtInMake.text,txtFileName.text))
        
        for item in [lblMake, txtInMake,txtFileName, btnSave]:
            boxMake.add_widget(item)

        pop = Popup(title = "New File", 
                    content = boxMake,
                    size = (550,550), 
                    size_hint=(None, None),
                    auto_dismiss=False)

        btnSave.bind(on_release = pop.dismiss)
        pop.open()
                

    #If user chooses to Import a File, the File Chooser opens and they can select which file they wish 
    #to use as their rules and prompts for the string input
    def importPress (self,event):
        boxInput = BoxLayout(orientation = 'vertical')
        lblInput = Label(text= "Please enter string you would like to test:")
        txtInput = TextInput()
        btnSaveInput = Button(text = "Save and Check",
                           valign = 'middle',
                           halign = 'center')
        btnSaveInput.bind(on_press = lambda butt: self.runIt(event,filename,txtInput.text))##################

        for thing in [lblInput, txtInput, btnSaveInput]:
            boxInput.add_widget(thing)

        popCompute = Popup(title = "Input String",
                           content = boxInput,
                           size = (500,500),
                           size_hint = (None, None),
                           auto_dismiss=True)

        Tk().withdraw()
        filename = askopenfilename()
        
        print(self.flag)#check flag changes
        self.impFile = filename
        print(self.impFile)#check file name 

        if filename != "":
            popCompute.open()


    def savePress (self, event, rules, fname):
        tName = fname + ".txt"
        newFile = open(tName, "w")
        newFile.write(rules)##put in self.rule
        

        boxInput = BoxLayout(orientation = 'vertical')
        lblInput = Label(text= "Please enter string you would like to test:")
        txtInput = TextInput()
        btnSaveInput = Button(text = "Save and Check",
                           valign = 'middle',
                           halign = 'center')
        btnSaveInput.bind(on_press = lambda butt: self.runIt(event,tName,txtInput.text))##################
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
                       content = Label(text = "Error occurred. \n Click outside popup to continue."),
                       size = (400,400),
                       size_hint = (None, None),
                       auto_dismiss=True)
        poperr.open()


    def runIt (self,event,fileName,strCheck):
       
       file = open(fileName, "r")
       
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

#Execution app runs widget
class app1(App):
    def build(self):
        return Root()

#if __name__=="__main__":
app1().run()