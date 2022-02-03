from PyQt5.QtWidgets import *
from tool_gui import Ui_MainWindow
import sys
from rv.GuiConfig import GuiConfig
from rv.GuiVerifier import GuiVerifier
from rv.GuiLog import GuiLog
from rv.Monitor import Monitor
from rv.RMLOracle import RMLOracle
from rv.TLOracle import TLOracle


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.__monitors = []
        self.__rmlOracle = RMLOracle()
        self.__tlOracle = TLOracle()

        self.__guiLog = GuiLog(self.__ui)
        self.__guiConfig = GuiConfig(self.__ui, self.__guiLog, self.__monitors)
        self.__guiVerifier = GuiVerifier(self.__ui, self.__guiLog, self.__rmlOracle, self.__tlOracle)

        # bu fonk cagırılarak baslangıctakı tanımlamalar yapılmıs olacak; signal vs.
        self.initGui()

    def initGui(self):
        self.__ui.btnConfigImportConf.clicked.connect(self.__guiConfig.importConfig)
        self.__ui.btnConfigNodeCreate.clicked.connect(self.__guiConfig.createNode)
        self.__ui.btnConfigTopicCreate.clicked.connect(self.__guiConfig.createTopic)
        self.__ui.btnConfigOracleCreate.clicked.connect(self.__guiConfig.createOracle)
        self.__ui.btnConfigMonitorCreate.clicked.connect(self.__guiConfig.createMonitor)
        self.__ui.btnConfigNodeUpdate.clicked.connect(self.__guiConfig.updateNode)
        self.__ui.btnConfigTopicUpdate.clicked.connect(self.__guiConfig.updateTopic)
        self.__ui.btnConfigOracleUpdate.clicked.connect(self.__guiConfig.updateOracle)
        self.__ui.btnConfigMonitorUpdate.clicked.connect(self.__guiConfig.updateMonitor)
        self.__ui.btnConfigNodeDelete.clicked.connect(self.__guiConfig.deleteNode)
        self.__ui.btnConfigTopicDelete.clicked.connect(self.__guiConfig.deleteTopic)
        self.__ui.btnConfigOracleDelete.clicked.connect(self.__guiConfig.deleteOracle)
        self.__ui.btnConfigMonitorDelete.clicked.connect(self.__guiConfig.deleteMonitor)
        self.__ui.cbxConfigNode.activated.connect(self.__guiConfig.setNodeComponentStatus)
        self.__ui.cbxConfigTopicTopic.activated.connect(self.__guiConfig.setTopicComponentStatus)

        self.__ui.cbxMonitorMonitor.activated.connect(self.__guiConfig.setMonitorComponentStatus)
        self.__ui.btnConfigSaveSave.clicked.connect(self.__guiConfig.saveConfig2file)
        self.__ui.cbxConfigTopicNode.activated.connect(self.__guiConfig.setTopicNodeComponentStatus)

        self.__ui.btnPropertyImport.clicked.connect(self.__guiVerifier.importProperty)
        self.__ui.btnPropertySave.clicked.connect(self.__guiVerifier.saveProperty2File)
        self.__ui.btnPropertyDefineCreate.clicked.connect(self.__guiVerifier.addProperty)
        self.__ui.btnPropertyDefineUpdate.clicked.connect(self.__guiVerifier.editProperty)
        self.__ui.btnPropertyDefineDelete.clicked.connect(self.__guiVerifier.deleteProperty)
        self.__ui.cbxPropertyDefineVerifier.activated.connect(self.__guiVerifier.setVerifierComponentsStatus)
        self.__ui.cbxPropertySaveType.activated.connect(self.__guiVerifier.updateVerifierSaveCbx)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
