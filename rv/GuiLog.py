from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from tool_gui import Ui_MainWindow


class GuiLog:
    def __init__(self, ui: Ui_MainWindow = None):
        self.__ui = ui

    def printLog(self, message: str = None, color: str = None):
        item = QListWidgetItem(message)
        if color == "red":
            item.setForeground(Qt.red)
        elif color == "green":
            item.setForeground(Qt.green)
        elif color == "yellow":
            item.setForeground(Qt.yellow)
        elif color == "blue":
            item.setForeground(Qt.blue)
        else:
            item.setForeground(Qt.black)

        self.__ui.lwLog.addItem(item)
        self.__ui.lwLog.scrollToBottom()
