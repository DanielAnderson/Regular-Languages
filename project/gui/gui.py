#We are going to be using Kivy for a main GUI and the included GUI Tkinter for a filechooser
#First download pygame then download Kivy. Here is the download site:
#http://www.lfd.uci.edu/~gohlke/pythonlibs/
#I tried downloading from the Kivy site but had lots of issues, 
#this site allowed the downloads to work on Windows OS and worked with Kivy's test code.
# Site for Linux version download http://kivy.org/#download, not yet tested


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from tkinter import Tk      #not sure if compatible with linux
from tkinter.filedialog import askopenfilename

flag = 0
newFile = ""
inFile = ""


class Root(Widget):
    def __init__(self):
        Widget.__init__(self)
        box = BoxLayout(orientation= 'vertical',
                        size = (600,600))
        lblIntro = Label(text = "Please select which you would like to check:")
        btnNFA = Button(text = "NFA",
                        valign = 'middle',
                        halign = 'center')
        btnNFA.bind(on_press = self.pressed, on_release = self.r1)
        
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
    
    def r1(self, event):
        flag = 1

    def r2(self, event):
        flag = 2

    def r3(self, event):
        flag = 3

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

    def makePress (self,event):
        boxMake = BoxLayout(orientation = 'vertical')
        lblMake = Label(text= "Please enter input")
        txtInput = TextInput()
        btnSave = Button(text = "Save File",
                           valign = 'middle',
                           halign = 'center')
        ###btnSave.bind(on_press = self.________computefunction_______)##################

        for item in [lblMake, txtInput, btnSave]:
            boxMake.add_widget(item)

        pop = Popup(title = "New File", 
                    content = boxMake,
                    size = (500,500), 
                    size_hint=(None, None),
                    auto_dismiss=True)
        pop.open()

    def importPress (self,event):
        Tk().withdraw()
        filename = askopenfilename()
        print(filename)

class app1(App):
    def build(self):
        return Root()

if __name__=="__main__":
    app1().run()