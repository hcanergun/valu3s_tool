from PyQt5.QtWidgets import *
from rv.Monitor import Monitor


class GuiConfig:
    def __init__(self, ui: QMainWindow = None, monitor: Monitor = None):
        self.__monitor = monitor
        self.__ui = ui

    # burada tüm fonksiyonları implemente edecez.
    def addNode(self):
        # örnek
        # ilgili tüm widget lara burada self.__ui üzerinden erişebiliriiz.
        # buradaki fonksiyonları main de signal'e baglıcaz.
        self.__ui.txtNodeCreateName.text()