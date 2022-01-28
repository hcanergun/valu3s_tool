from PyQt5.QtWidgets import *
from tool_gui import Ui_MainWindow

class GuiLog:
    def __init__(self, ui: QMainWindow = None):
        #self.__ui = ui
        self.__ui = Ui_MainWindow()

    def printLog(self,message:str):
        self.__ui.lwLog.addItem(message)
