from PyQt5.QtWidgets import *
from tool_gui import Ui_MainWindow
import sys
from rv.GuiConfig import GuiConfig
from rv.GuiVerifier import GuiVerifier
from rv.GuiLog import GuiLog
from rv.Monitor import Monitor
from rv.RMLOracle import RMLOracle
from rv.TLOracle import TLOracle
from rv.GuiMonitor import GuiMonitor

"""
catkin make yapılacak monitor için;
$ roslaunch src/monitor/run.launch

"""

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.__monitor = Monitor()
        self.__rmlOracle = RMLOracle()
        self.__tlOracle = TLOracle()

        self.__guiLog = GuiLog(self.__ui)
        self.__guiConfig = GuiConfig(self.__ui, self.__guiLog, self.__monitor)
        self.__guiVerifier = GuiVerifier(self.__ui, self.__guiLog, self.__rmlOracle, self.__tlOracle)
        self.__guiMonitor = GuiMonitor(self.__ui,self.__guiLog)

        # bu fonk cagırılarak baslangıctakı tanımlamalar yapılmıs olacak; signal vs.
        self.initGui()

    def initGui(self):

        self.__ui.btnPropertyImport.clicked.connect(self.__guiVerifier.importProperty)
        self.__ui.btnPropertySave.clicked.connect(self.__guiVerifier.saveProperty2File)

        self.__ui.btnPropertyDefineCreate.clicked.connect(self.__guiVerifier.addProperty)
        self.__ui.btnPropertyDefineUpdate.clicked.connect(self.__guiVerifier.editProperty)
        self.__ui.btnPropertyDefineDelete.clicked.connect(self.__guiVerifier.deleteProperty)
        self.__ui.cbxPropertyDefineVerifier.activated.connect(self.__guiVerifier.setVerifierComponentsStatus)
        self.__ui.cbxPropertySaveType.activated.connect(self.__guiVerifier.updateVerifierSaveCbx)
        self.__ui.btnMonitorConfFileSelect.clicked.connect(self.__guiMonitor.selectConfFile)
        self.__ui.btnMonitorROSFolderSelect.clicked.connect(self.__guiMonitor.selectROSWs)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()