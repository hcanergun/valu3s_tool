from PyQt5.QtWidgets import *
from rv.Monitor import Monitor
from rv.GuiLog import GuiLog
from tool_gui import Ui_MainWindow


class GuiConfig:
    def __init__(self, ui: Ui_MainWindow = None, logger: GuiLog = None, monitor: Monitor = None):
        self.__monitor = monitor
        self.__ui = ui
        self.__logger = logger
