
#We are going to be using Kivy for a GUI
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
from kivy.uix.widget import Widget

class Root(Widget):
    def __init__(self):
        Widget.__init__(self)
        box = BoxLayout(orientation= 'vertical',
                        size = (600,600))
        lblIntro = Label(text = "Please select which you would like to check:")
        btnNFA = Button(text = "NFA",
                        valign = 'middle',
                        halign = 'center')
        btnNFA.bind(on_press = self.pressed)
        
        btnDFA = Button(text = "DFA",
                        valign = 'middle',
                        halign = 'center')
        btnDFA.bind(on_press = self.pressed)

        btnGrm = Button(text = "Regular Grammars",
                        valign = 'middle',
                        halign = 'center')
        btnGrm.bind(on_press = self.pressed)
        
        box.add_widget(lblIntro)
        box.add_widget(btnNFA)
        box.add_widget(btnDFA)
        box.add_widget(btnGrm)
        self.add_widget(box)

    def pressed(self,event):
        boxsave = BoxLayout(orientation = 'vertical')
        btnImport = Button(text = "Import a File",
                           valign = 'middle',
                           halign = 'center')
        btnMake = Button(text = "Create a New File",
                           valign = 'middle',
                           halign = 'center')
        lblSave = Label(text = "Would you Like to Import a File or Create a New File")
        
        for thing in [lblSave, btnImport, btnMake]:
            boxsave.add_widget(thing)
        
        ppu = Popup(title = " Title", 
                    content = boxsave,
                    size = (500,500), 
                    size_hint=(None, None),
                    auto_dismiss=True)
        ppu.open()

class app1(App):
    def build(self):
        return Root()

if __name__=="__main__":
    app1().run()