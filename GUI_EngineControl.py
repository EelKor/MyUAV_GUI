from GUI_base import GUI_base
from tkinter import ttk

class GUI_EngineControl(GUI_base):
    pass


test = GUI_EngineControl()

test.setTitle("EngineControl")
test.createTab("test1","test2","test3")
test.showTab()

ttk.Label(test.tab[0],text="Label1").grid(column=0, row=0)
test.createLabelFrame(test.tab[0], "test22")

test.labelframe[0].grid(column=1, row=0)
test.showLabelFrameID("test22")

ttk.Label(test.labelframe[0], text="LAbel2").grid(column=0, row=0)

test.createLabelFrame(test.tab[0],"Label2")
test.labelframe[1].grid(column=3, row=0)
test.showLabelFrameID("Label2")

ttk.Label(test.labelframe[1], text="Label2").grid(column=0, row=0)

