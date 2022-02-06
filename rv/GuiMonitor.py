from PyQt5.QtWidgets import *
from rv.RMLOracle import RMLOracle
from rv.TLOracle import TLOracle
from rv.GuiLog import GuiLog
from rv.Property import Property
from tool_gui import Ui_MainWindow
from rv.Verifier import Verifier
from rv.Exceptions import *
import json
import os
import subprocess


class GuiMonitor:
    def __init__(self, ui: Ui_MainWindow = None, logger: GuiLog = None):
        self.__ui = ui
        self.__logger = logger
        self.__rosws = None

        os.system("roslaunch rosmonitoring/monitor/src/")

    def selectConfFile(self):
        if not self.__rosws:
            self.__logger.printLog("First select the ROS workspace", "red")
            return
        try:
            filePath = self.openFileDialogWindow()
            self.convertYAML2MonitorPy(filePath=filePath)
            self.__logger.printLog("Selecting conf .yaml file is complete successfully", "green")
        except:
            self.__logger.printLog("An error is occurred while conf .yaml file selecting", "red")

    def selectROSWs(self):
        self.__rosws = self.openFolderDialogWindow()
        try:
            if os.system(f"rm -rf {self.__rosws}/src/monitor") == 0:
                self.__logger.printLog("The monitor link is deleted from Ros workspace successfully", "green")
            else:
                raise LinkMonitor2ROSWs

            print(f"ln -s {os.getcwd()}/rosmonitoring/monitor {self.__rosws}/src")
            if os.system(f"ln -s {os.getcwd()}/rosmonitoring/monitor {self.__rosws}/src") == 0:
                self.__logger.printLog("Monitor link is created into Ros workspace successfully", "green")
            else:
                raise LinkMonitor2ROSWs
        except LinkMonitor2ROSWs:
            self.__logger.printLog("An error is occurred while the monitor folder linking into Ros workspace", "red")

    def convertYAML2MonitorPy(self, filePath: str):
        try:
            if os.system("chmod +x rosmonitoring/generator/generator") == 0:
                self.__logger.printLog("Generator got executable permission successfully.", "green")
            else:
                raise GetExecutableAuth
            os.chdir("rosmonitoring/generator/")
            # result = subprocess.check_output(f"./generator --config_file {filePath}", shell=True)
            if os.system(f"./generator --config_file {filePath}") != 0:
                raise ConvertYAML2MonitorPy
            os.chdir("../../")
            print(os.getcwd())

            monitorName = "beginner_tutorials.py"
            if os.system(f"chmod +x rosmonitoring/monitor/src/{monitorName}") == 0:
                self.__logger.printLog("Generator got executable permission successfully.", "green")
            else:
                raise GetExecutableAuth

        except GetExecutableAuth:
            self.__logger.printLog("An error is occurred while setting executable authentication to the generator",
                                   "red")
        except ConvertYAML2MonitorPy:
            self.__logger.printLog("An error occurred while generating monitor file from .yaml configuration", "red")
        except:
            self.__logger.printLog("An error is occurred in convertYAML2MonitorPy()", "red")

    def openFolderDialogWindow(self):
        try:
            rosWsFolder = QFileDialog.getExistingDirectory(None, "Select your catkin_ws folder")
            if rosWsFolder:
                self.__logger.printLog(message="ROS workspace folder selection completed successfully", color="green")
                return rosWsFolder
            else:
                raise IOError(f"An error occurred while opening the folder")
        except IOError:
            self.__logger.printLog(message=f"An error occurred while opening the folder", color="red")
        except:
            self.__logger.printLog(message="An error is occurred in openFolderDialogWindow()", color="red")

    def openFileDialogWindow(self) -> str:
        try:
            filePath, check = QFileDialog.getOpenFileName(None, "Open File", "rosmonitoring/generator/online_configs/",
                                                          "Text Files (*.yaml)")
            if filePath:
                self.__logger.printLog(message="File selection completed successfully", color="green")
                return filePath
            else:
                raise IOError(f"An error occurred while opening the file")
        except IOError:
            self.__logger.printLog(message=f"An error occurred while opening the file", color="red")
        except:
            self.__logger.printLog(message="An error is occurred in openFileDialogWindow()", color="red")
