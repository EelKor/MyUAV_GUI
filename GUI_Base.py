import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as msg

class GUI_base:
    
    def __init__(self):
        self.win = tk.Tk()
        self.menu_bar = Menu(self.win)
        self.win.config(menu=self.menu_bar)
        self.labelframe = []
        self.LabelFrameID = []
        

    def setTitle(self,title):
        self.win.title(title)

    
    def createTab(self, name1, name2=0, name3=0, name4=0, name5=0):
        
        self.name = [0,0,0,0,0]
        self.tab = []
        
        self.name[0] = name1
        self.name[1] = name2
        self.name[2] = name3
        self.name[3] = name4
        self.name[4] = name5
        
        self.count = 0

        for i in range(5):
            if not self.name[i] == 0:
                self.count += 1
                
        self.tabControl = ttk.Notebook(self.win)

        for i in range(self.count):
            self.tab.append(ttk.Frame(self.tabControl))
            self.tabControl.add(self.tab[i], text=self.name[i])
    

    def showTab(self):
         self.tabControl.pack(expand=1, fill="both")
        


    def createLabelFrame(self, _object, title):
        
        self.labelframe.append(ttk.LabelFrame(_object, text=title))
        self.LabelFrameID.append(title)

        

    def searchLabelFrameID(self, title):
        print("=====Search -> LabelFrameID=====")
        print(title + ": " , self.LabelFrameID.index(title))
        


    def showLabelFrameID(self):
        print("========LabelFrameID========")
        for i in range(len(self.labelframe)):
            print(self.LabelFrameID[i] + " -> ", i)

        print("============================")

        
            
        

