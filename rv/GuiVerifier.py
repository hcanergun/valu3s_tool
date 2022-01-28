from PyQt5.QtWidgets import *
from rv.RMLOracle import RMLOracle
from rv.TLOracle import TLOracle
from rv.GuiLog import GuiLog


class GuiVerifier:
    def __init__(self, ui: QMainWindow = None, logger: GuiLog = None, rmlOracle: RMLOracle = None,
                 tlOracle: TLOracle = None):
        self.__rmlOracle = rmlOracle
        self.__ui = ui
        self.__tlOracle = tlOracle
        self.__logger = logger

    def importProperty(self):
        lines = self.getTxtFileContent(filePath=self.openFileDialogWindow())
        lines = [line.strip('\n') for line in lines]

        if self.__ui.cbxPropertyImportType.currentText() == "TL Oracle":
            self.importTLProperty(lines=lines)
        else:
            self.importRMLProperty(lines=lines)

    def importRMLProperty(self, lines: list):
        if self.__rmlOracle:
            self.__rmlOracle.setProperties(lines)
        else:
            self.__rmlOracle = TLOracle()
            self.__rmlOracle.setProperties(lines)
        self.__logger.printLog("RML properties imported successfully", color="green")

    def importTLProperty(self, lines: list):
        if self.__tlOracle:
            self.__tlOracle.setProperties(lines)
        else:
            self.__tlOracle = TLOracle()
            self.__tlOracle.setProperties(lines)
        self.__logger.printLog("TL properties imported successfully", color="green")

    def openFileDialogWindow(self) -> str:
        # file , check = QFileDialog.getOpenFileName(None,
        # "Open File","C:/Users/zeker/OneDrive/Masaüstü/YerYazProje/docs", "Text Files (*.txt)")
        try:
            filePath, check = QFileDialog.getOpenFileName(None, "Open File", "","Text Files (*.txt)")
            #filePath = 'C:/Users/zeker/OneDrive/Masaüstü/New Text Document.txt'
            if filePath:
                self.__logger.printLog("File selection completed successfully", color="green")
                return filePath
            else:
                raise IOError(f"An error occurred while opening the file")
        except IOError:
            self.__logger.printLog(f"An error occurred while opening the file", color="red")
        except:
            self.__logger.printLog("ERROR in openFileDialogWindow()", color="red")

    def getTxtFileContent(self, filePath: str) -> list:
        try:
            with open(filePath) as file:
                if not file:
                    raise IOError(f"An error occurred while reading the file")
                self.__logger.printLog("File content read successfully", color="green")
                return file.readlines()
        except IOError:
            self.__logger.printLog(f"An error occurred while reading the file", color="red")
        except:
            self.__logger.printLog("ERROR in getTxtFileContent()", color="red")

    def saveProperty2File(self):
        fileName = self.__ui.txtPropertySaveFileName.text()
        if fileName:
            items = self.__ui.lwPropertySaveSelect.selectedItems()
            if items:
                try:
                    with open(f'{fileName}.txt', 'w') as f:
                        f.writelines([item.text() + "\n" for item in items])
                        self.__logger.printLog("File content saved successfully", color="green")
                except IOError:
                    self.__logger.printLog(f"An error occurred while writing to the file", color="red")
                except:
                    self.__logger.printLog("ERROR in saveProperty2File()", color="red")

            else:
                self.__logger.printLog("Please select the properties", color="red")
        else:
            del fileName
            self.__logger.printLog("Please fill the file name", color="red")
