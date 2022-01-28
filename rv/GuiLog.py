from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class GuiLog:
    def __init__(self, ui: QMainWindow = None):
        self.__ui = ui

    def printLog(self, message: str = None, color: str = None):
        item=QListWidgetItem(message)
        if color=="red":
            item.setForeground(Qt.red)
        elif color=="green":
            item.setForeground(Qt.green)
        elif color=="yellow":
            item.setForeground(Qt.yellow)
        elif color=="blue":
            item.setForeground(Qt.blue)
        else:
            item.setForeground(Qt.black)

        self.__ui.lwLog.addItem(item)

