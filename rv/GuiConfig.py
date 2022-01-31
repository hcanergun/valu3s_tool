from PyQt5.QtWidgets import *
from rv.Monitor import Monitor
from rv.GuiLog import GuiLog
from tool_gui import Ui_MainWindow


class GuiConfig:
    def __init__(self, ui: Ui_MainWindow = None, logger: GuiLog = None, monitor: Monitor = None):
        self.__monitor = monitor
        self.__ui = ui
        self.__logger = logger

    def importConfig(self):

        # open file dialog and address the file to import
        filepath = "file/to/import"
        filepath = None
        try:
            if not filepath:
                raise ImportError(f"<CONFIG IMPORT> An error occurred while {filepath} importing")
                # assert num % 2 == 0,"hata var"
        except ImportError:
            self.__logger.printLog(f"An error occurred while {filepath} importing")

        except:
            self.__logger.printLog(f"An error occurred while {filepath} importing")
        finally:
            pass
