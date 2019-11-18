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
        



test = GUI_EngineControl()
