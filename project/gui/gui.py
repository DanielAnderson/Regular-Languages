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

class Root(App):
    def build(self):
        box = BoxLayout(orientation= 'vertical')
        lblIntro = Label(text = "Please select which you would like to check:")
        btnNFA = Button(text = "NFA",
                        valign = 'middle',
                        halign = 'center')
        btnDFA = Button(text = "DFA",
                        valign = 'middle',
                        halign = 'center')
        btnGrm = Button(text = "Regular Grammars",
                        valign = 'middle',
                        halign = 'center')
        box.add_widget(lblIntro)
        box.add_widget(btnNFA)
        box.add_widget(btnDFA)
        box.add_widget(btnGrm)
        return box


if __name__=="__main__":
    Root().run()