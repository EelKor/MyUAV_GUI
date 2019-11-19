from GUI_base import GUI_base
from tkinter import ttk

class GUI_EngineControl(GUI_base):

    def __init__(self):
        super().__init__()
        super().setTitle("Engine Panel")
        super().createTab("Main", "RPM", "Volt", "Temp","Msg")
        super().showTab()
        
        
        
    def RPM_Indicator(self,_object):
        pass
        
 

engine = GUI_EngineStatus()


menu_bar = Menu(engine.win)
engine.win.config(menu=menu_bar)
com_menu = Menu(menu_bar, tearoff=0)
com_menu.add_command(label="COM")
com_menu.add_separator()
com_menu.add_command(label="Ping Test")
com_menu.add_separator()
com_menu.add_command(label="Exit")
menu_bar.add_cascade(label="Network", menu=com_menu)



test_menu = Menu(menu_bar, tearoff=0)
test_menu.add_command(label="Test")
test_menu.add_command(label="Stop")
menu_bar.add_cascade(label="Test", menu=test_menu)
