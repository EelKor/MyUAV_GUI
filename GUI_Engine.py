from GUI_EngineStatus import *

def _test():
	print("Menu has been clicked")
	


engine = GUI_EngineStatus()
engine.createMenu()
engine.addMenulist("test1", _test)
engine.addMenulist("test2", _test)
engine.addMenulist("test3", _test)
engine.showMenu("test")

engine.createMenu()
engine.addMenulist("test1-1", _test)
engine.addMenulist("test1-2", _test)
engine.showMenu("test1")
