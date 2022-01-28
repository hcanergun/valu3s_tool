from PyQt5.QtWidgets import *
from tool_gui import Ui_MainWindow
import sys
from rv.GuiConfig import GuiConfig
from rv.GuiVerifier import GuiVerifier
from rv.GuiLog import GuiLog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.__guiLog = GuiLog(self.__ui)
        self.__guiConfig = GuiConfig(self.__ui,self.__guiLog)
        self.__guiVerifier = GuiVerifier(self.__ui,self.__guiLog)


        # bu fonk cagırılarak baslangıctakı tanımlamalar yapılmıs olacak; signal vs.
        self.initGui()

    def initGui(self):
        # self.pushButton.clicked.connect(self.lineEdit.clear)
        self.__ui.btnConfigImportConf.clicked.connect(self.__guiConfig.importConfig)
        self.__ui.btnPropertyImport.clicked.connect(self.__guiVerifier.importProperty)
        self.__ui.btnPropertySave.clicked.connect(self.__guiVerifier.saveProperty2File)








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
