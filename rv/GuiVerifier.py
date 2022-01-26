from PyQt5.QtWidgets import *
from rv.RMLOracle import RMLOracle
from rv.TLOracle import TLOracle


class GuiVerifier:
    def __init__(self, ui: QMainWindow = None, rmlOracle: RMLOracle = None, tlOracle: TLOracle = None):
        self.__rmlOracle = rmlOracle
        self.__ui = ui
        self.__tlOracle = tlOracle