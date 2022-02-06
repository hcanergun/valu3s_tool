from PyQt5.QtWidgets import *
from rv.RMLOracle import RMLOracle
from rv.TLOracle import TLOracle
from rv.GuiLog import GuiLog
from rv.Property import Property
from tool_gui import Ui_MainWindow
from rv.Verifier import Verifier
import json


class GuiVerifier:
    def __init__(self, ui: Ui_MainWindow = None, logger: GuiLog = None, rmlOracle: RMLOracle = None,
                 tlOracle: TLOracle = None):
        self.__rmlOracle = rmlOracle
        self.__ui = ui
        self.__tlOracle = tlOracle
        self.__logger = logger

        self.initComponents()

    def initComponents(self):
        self.__ui.btnPropertyDefineDelete.setEnabled(False)
        self.__ui.btnPropertyDefineUpdate.setEnabled(False)
        self.__ui.btnPropertyDefineCreate.setEnabled(True)

        ## silinecekk !!
        self.__ui.lwPropertyDefineNodes.addItem("deneme1")
        self.__ui.lwPropertyDefineNodes.addItem("deneme2")
        self.__ui.lwPropertyDefineNodes.addItem("deneme3")

    def getProperties(self) -> [Property]:
        temp = []
        temp.extend(self.__rmlOracle.getProperties())
        temp.extend(self.__tlOracle.getProperties())
        return temp

    def addProperty(self):
        if self.__ui.txtPropertyDefineName.text() == "" or \
                self.__ui.txtPropertyDefineDescription.toPlainText() == "" \
                or self.__ui.txtPropertyDefineFormula.text() == "" \
                or not self.__ui.lwPropertyDefineNodes.selectedItems():
            self.__logger.printLog(message="Please fill in all fields !!", color="red")
            return

        if self.__ui.cbxPropertyDefineType.currentText() == "TL Oracle":
            if self.__tlOracle.isExist(self.__ui.txtPropertyDefineName.text())[0] or \
                    self.__rmlOracle.isExist(self.__ui.txtPropertyDefineName.text())[0]:
                self.__logger.printLog(message="The name of the property is not unique. Change the name !!",
                                       color="red")
                return
            else:
                self.__tlOracle.setProperties(Property(name=self.__ui.txtPropertyDefineName.text(),
                                                       description=self.__ui.txtPropertyDefineDescription.toPlainText(),
                                                       formula=self.__ui.txtPropertyDefineFormula.text(),
                                                       nodeNames=[item.text() for item in
                                                                  self.__ui.lwPropertyDefineNodes.selectedItems()]))
                self.__logger.printLog(message="The property is added successfully", color="green")
        else:
            if self.__rmlOracle.isExist(self.__ui.txtPropertyDefineName.text())[0] or \
                    self.__tlOracle.isExist(self.__ui.txtPropertyDefineName.text())[0]:
                self.__logger.printLog(message="The name of the property is not unique. Change the name !!",
                                       color="red")
                return
            else:
                self.__rmlOracle.setProperties(Property(name=self.__ui.txtPropertyDefineName.text(),
                                                        description=self.__ui.txtPropertyDefineDescription.toPlainText(),
                                                        formula=self.__ui.txtPropertyDefineFormula.text(),
                                                        nodeNames=[item.text() for item in
                                                                   self.__ui.lwPropertyDefineNodes.selectedItems()]))
                self.__logger.printLog(message="The property is added successfully", color="green")
        self.__ui.txtPropertyDefineName.clear()
        self.__ui.txtPropertyDefineDescription.clear()
        self.__ui.txtPropertyDefineFormula.clear()
        self.__ui.lwPropertyDefineNodes.clearSelection()
        self.updateVerifierDefineCbx()
        self.updateVerifierSaveCbx()

    def editProperty(self):
        property = self.__tlOracle.getPropertyByName(self.__ui.cbxPropertyDefineVerifier.currentText())
        if property:
            self.__tlOracle.deletePropertyByName(property.getName())
        else:
            property = self.__rmlOracle.getPropertyByName(self.__ui.cbxPropertyDefineVerifier.currentText())
            if property:
                self.__rmlOracle.deletePropertyByName(property.getName())
        self.addProperty()

    def deleteProperty(self):
        propertyName = self.__ui.cbxPropertyDefineVerifier.currentText()
        if self.__tlOracle.isExist(propertyName)[0]:
            self.__tlOracle.getProperties().pop(self.__tlOracle.isExist(propertyName)[1])
        else:
            self.__rmlOracle.getProperties().pop(self.__rmlOracle.isExist(propertyName)[1])

        self.__ui.txtPropertyDefineName.clear()
        self.__ui.txtPropertyDefineDescription.clear()
        self.__ui.txtPropertyDefineFormula.clear()
        self.__ui.lwPropertyDefineNodes.clearSelection()
        self.updateVerifierDefineCbx()
        self.updateVerifierSaveCbx()

    def importProperty(self):
        filePath = self.openFileDialogWindow()
        if not filePath:
            return
        properties = self.getJSONFileContent(filePath=filePath)
        for property in properties["properties"]:
            if self.__ui.cbxPropertyImportType.currentText() == "TL Oracle":
                self.__tlOracle.setProperties(Property(name=property["name"],
                                                       description=property["description"],
                                                       formula=property["formula"],
                                                       nodeNames=property["nodeNames"]))
                self.__logger.printLog(message="TL properties imported successfully", color="green")
            else:
                self.__rmlOracle.setProperties(Property(name=property["name"],
                                                        description=property["description"],
                                                        formula=property["formula"],
                                                        nodeNames=property["nodeNames"]))
                self.__logger.printLog(message="RML properties imported successfully", color="green")
        self.updateVerifierDefineCbx()
        self.updateVerifierSaveCbx()

    def openFileDialogWindow(self) -> str:
        try:
            filePath, check = QFileDialog.getOpenFileName(None, "Open File", "rosmonitoring/oracle", "Text Files (*.json)")
            if filePath:
                self.__logger.printLog(message="File selection completed successfully", color="green")
                return filePath
            else:
                raise IOError(f"An error occurred while opening the file")
        except IOError:
            self.__logger.printLog(message=f"An error occurred while opening the file", color="red")
        except:
            self.__logger.printLog(message="ERROR in openFileDialogWindow()", color="red")

    def getJSONFileContent(self, filePath: str):
        try:
            with open(filePath) as file:
                if not file:
                    raise IOError(f"An error occurred while reading the file")
                self.__logger.printLog(message="File content read successfully", color="green")
                return json.load(file)
        except IOError:
            self.__logger.printLog(message=f"An error occurred while reading the file", color="red")
        except:
            self.__logger.printLog(message="ERROR in getJSONFileContent()", color="red")

    def saveProperty2File(self):
        fileName = self.__ui.txtPropertySaveFileName.text()
        if fileName:
            items = self.__ui.lwPropertySaveSelect.selectedItems()
            if items:
                try:
                    if self.__ui.cbxPropertySaveType.currentText() == "TL Oracle":
                        with open(f'rosmonitoring/oracle/TLOracle/properties/{fileName}.json', 'w') as f:
                            f.write(self.preparePropertiesJSON(self.__tlOracle.getPropertiesByName(names=[item.text() for item in items])))
                    else:
                        with open(f'rosmonitoring/oracle/RMLOracle/rml/properties/{fileName}.json', 'w') as f:
                            f.write(self.preparePropertiesJSON(self.__rmlOracle.getPropertiesByName(names=[item.text() for item in items])))

                    self.__ui.txtPropertySaveFileName.clear()
                    self.__logger.printLog(message="File content saved successfully", color="green")
                except IOError:
                    self.__logger.printLog(message=f"An error occurred while writing to the file", color="red")
                except:
                    self.__logger.printLog(message="ERROR in saveProperty2File()", color="red")

            else:
                self.__logger.printLog(message="Please select the properties", color="red")
        else:
            del fileName
            self.__logger.printLog(message="Please fill the file name", color="red")

    @staticmethod
    def preparePropertiesJSON(properties: [Verifier]) -> str:
        content = {"properties": []}
        for property in properties:
            content["properties"].append(
                {"name": property.getName(), "description": property.getDescription(), "formula": property.getFormula(),
                 "nodeNames": property.getNodeNames()})

        return json.dumps(content, indent=4)

    def setVerifierComponentsStatus(self):
        if self.__ui.cbxPropertyDefineVerifier.currentText() == "New Property":
            self.__ui.btnPropertyDefineDelete.setEnabled(False)
            self.__ui.btnPropertyDefineUpdate.setEnabled(False)
            self.__ui.btnPropertyDefineCreate.setEnabled(True)
        else:
            verifier = self.__tlOracle.getPropertyByName(self.__ui.cbxPropertyDefineVerifier.currentText())
            if verifier:
                self.__ui.cbxPropertyDefineType.setCurrentIndex(0)
            else:
                self.__ui.cbxPropertyDefineType.setCurrentIndex(1)
                verifier = self.__rmlOracle.getPropertyByName(self.__ui.cbxPropertyDefineVerifier.currentText())

            self.__ui.txtPropertyDefineName.setText(verifier.getName())
            self.__ui.txtPropertyDefineDescription.setPlainText(verifier.getDescription())
            self.__ui.txtPropertyDefineFormula.setText(verifier.getFormula())
            self.__ui.lwPropertyDefineNodes.clear()

            for name in verifier.getNodeNames():
                self.__ui.lwPropertyDefineNodes.addItem(name)

            self.__ui.btnPropertyDefineDelete.setEnabled(True)
            self.__ui.btnPropertyDefineUpdate.setEnabled(True)
            self.__ui.btnPropertyDefineCreate.setEnabled(False)

    def updateVerifierDefineCbx(self):
        self.__ui.cbxPropertyDefineVerifier.clear()
        self.__ui.cbxPropertyDefineVerifier.addItem("New Property")
        for tlVerifier in self.__tlOracle.getProperties():
            self.__ui.cbxPropertyDefineVerifier.addItem(tlVerifier.getName())
        for rmlVerifier in self.__rmlOracle.getProperties():
            self.__ui.cbxPropertyDefineVerifier.addItem(rmlVerifier.getName())

        self.__ui.cbxPropertyDefineVerifier.setCurrentIndex(0)
        self.__ui.btnPropertyDefineDelete.setEnabled(False)
        self.__ui.btnPropertyDefineUpdate.setEnabled(False)
        self.__ui.btnPropertyDefineCreate.setEnabled(True)

    def updateVerifierSaveCbx(self):
        self.__ui.lwPropertySaveSelect.clear()
        if self.__ui.cbxPropertySaveType.currentText() == "TL Oracle":
            for tlVerifier in self.__tlOracle.getProperties():
                self.__ui.lwPropertySaveSelect.addItem(tlVerifier.getName())
        else:
            for rmlVerifier in self.__rmlOracle.getProperties():
                self.__ui.lwPropertySaveSelect.addItem(rmlVerifier.getName())
        self.__ui.cbxPropertyDefineVerifier.setCurrentIndex(0)