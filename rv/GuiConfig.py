from PyQt5.QtWidgets import *
from rv.Monitor import Monitor
from rv.Node import Node
from rv.Topic import Topic
from rv.GuiLog import GuiLog
from rv.Verifier import Verifier
from tool_gui import Ui_MainWindow


class GuiConfig:
    def __init__(self, ui: Ui_MainWindow = None, logger: GuiLog = None, monitors: [Monitor] = []):
        self.__monitors = monitors
        self.__ui = ui
        self.__logger = logger

        self.initComponents()

    def initComponents(self):
        self.__ui.btnConfigNodeCreate.setEnabled(True)
        self.__ui.btnConfigNodeUpdate.setDisabled(True)
        self.__ui.btnConfigNodeDelete.setDisabled(True)
        self.__ui.btnConfigTopicCreate.setEnabled(True)
        self.__ui.btnConfigTopicUpdate.setDisabled(True)
        self.__ui.btnConfigTopicDelete.setDisabled(True)
        self.__ui.btnConfigOracleCreate.setEnabled(True)
        self.__ui.btnConfigOracleUpdate.setDisabled(True)
        self.__ui.btnConfigOracleDelete.setDisabled(True)
        self.__ui.btnConfigMonitorCreate.setEnabled(True)
        self.__ui.btnConfigMonitorUpdate.setDisabled(True)
        self.__ui.btnConfigMonitorDelete.setDisabled(True)
        self.__ui.txtConfigOracleName.setEnabled(False)

    def createNode(self):
        if not len(self.__monitors):
            self.__logger.printLog("Please create Monitor before creating Node ", "red")
            return

        if self.__ui.cbxMonitorMonitor.currentText() == 'New Monitor':
            self.__logger.printLog("Please select Monitor before creating Node ", "red")
            return

        if self.__ui.txtConfigNodeName.text() == "" or \
                self.__ui.txtConfigNodePath.text() == "" or \
                self.__ui.txtConfigNodePackage.text() == "":
            self.__logger.printLog("Please fill in all Node properties", "red")
            return

        for nodes in self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].getNodes():
            if nodes.getName() == self.__ui.txtConfigNodeName.text():
                self.__logger.printLog("Node name must be unique", "red")
                return

        self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].appendNode(
            Node(name=self.__ui.txtConfigNodeName.text(), type=None,
                 path=self.__ui.txtConfigNodePath.text(), launchName=None,
                 packageName=self.__ui.txtConfigNodePackage.text(),
                 topics=[]))

        self.__ui.cbxConfigNode.addItem(self.__ui.txtConfigNodeName.text())
        self.__ui.cbxConfigTopicNode.addItem(self.__ui.txtConfigNodeName.text())
        self.__ui.txtConfigNodeName.clear()
        self.__ui.txtConfigNodePath.clear()
        self.__ui.txtConfigNodePackage.clear()

        # self.__ui.cbxConfigNode.setCurrentIndex(self.__ui.cbxConfigNode.count() - 1)
        # self.setNodeComponentStatus()

        self.__logger.printLog("Node successfully created.", 'green')
        self.previewListWidget()

    def createTopic(self):
        if len(self.__monitors) == 0:
            self.__logger.printLog("Please create Monitor before creating Node and Topic ", "red")
            return

        if len(self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].getNodes()) == 0:
            self.__logger.printLog("Please create Node before creating Topic ", "red")
            return

        if self.__ui.txtConfigMonitorName.text() == "New Monitor":
            self.__logger.printLog("Please select Monitor before creating Topic ", "red")
            return

        if self.__ui.cbxConfigTopicNode.currentText() == "":
            self.__logger.printLog("Please select Node before creating Topic ", "red")
            return

        if self.__ui.txtConfigTopicName.text() == "" or \
                self.__ui.txtConfigTopicType.text() == "":
            self.__logger.printLog("Please fill in all Topic properties", "red")
            return

        for topics in self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].getNodes()[
            self.__ui.cbxConfigTopicNode.currentIndex()].getTopics():
            if topics.getName() == self.__ui.txtConfigTopicName.text():
                self.__logger.printLog("Topic name must be unique", "red")
                return

        self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].getNodes()[
            self.__ui.cbxConfigTopicNode.currentIndex()].appendTopic(
            Topic(name=self.__ui.txtConfigTopicName.text(),
                  type=self.__ui.txtConfigTopicType.text(),
                  action=self.__ui.cbxConfigTopicAction.currentText(),
                  publishers=[self.__ui.cbxConfigTopicNode.currentText()]))

        self.__ui.cbxConfigTopicTopic.addItem(self.__ui.txtConfigTopicName.text())
        self.__ui.txtConfigTopicName.clear()
        self.__ui.txtConfigTopicType.clear()
        self.__ui.cbxConfigTopicAction.setCurrentIndex(0)

        # self.__ui.cbxConfigTopicTopic.setCurrentIndex(self.__ui.cbxConfigTopicTopic.count() - 1)
        # self.setTopicComponentStatus()

        self.__logger.printLog("Topic successfully created.", 'green')
        self.previewListWidget()

    def createOracle(self):
        if len(self.__monitors) == 0:
            self.__logger.printLog("Please create Monitor before creating Oracle ", "red")
            return

        if self.__ui.cbxMonitorMonitor.currentText() == 'New Monitor':
            self.__logger.printLog("Please select Monitor before creating Oracle ", "red")
            return

        if self.__ui.txtConfigMonitorName.text() == "New Monitor":
            self.__logger.printLog("Please select Monitor before creating Oracle ", "red")
            return

        if self.__ui.txtConfigOraclePort.text() == "" or self.__ui.txtConfigOracleUrl.text() == "":
            self.__logger.printLog("Please fill in all Oracle properties", "red")
            return

        if not self.__ui.txtConfigOraclePort.text().isnumeric():
            self.__logger.printLog("Port value must be integer", "red")
            return

        self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].setOracle(
            Verifier(port=int(self.__ui.txtConfigOraclePort.text()),
                     url=self.__ui.txtConfigOracleUrl.text(),
                     action=self.__ui.cbxConfigOracleAction.currentText()))

        self.__ui.txtConfigOracleName.setText(self.__ui.txtConfigOraclePort.text() + ':' +
                                              self.__ui.txtConfigOracleUrl.text() + '  -> ' +
                                              self.__ui.cbxConfigOracleAction.currentText())

        self.__ui.btnConfigOracleCreate.setDisabled(True)
        self.__ui.btnConfigOracleUpdate.setDisabled(False)
        self.__ui.btnConfigOracleDelete.setDisabled(False)

        self.__logger.printLog("Oracle successfully created.", 'green')
        self.previewListWidget()

    def createMonitor(self):
        if self.__ui.txtConfigMonitorName.text() == "" or self.__ui.txtConfigMonitorLog.text() == "":
            self.__logger.printLog("Please fill in all Monitor properties", "red")
            return

        for monitor in self.__monitors:
            if monitor.getName() == self.__ui.txtConfigMonitorName.text():
                self.__logger.printLog("Monitor name must be unique", "red")
                return

        self.__monitors.append(Monitor(name=self.__ui.txtConfigMonitorName.text(),
                                       logFileName=self.__ui.txtConfigMonitorLog.text(),
                                       silent=bool(self.__ui.cbxMonitorSilent.currentIndex()),
                                       nodes=[]))

        self.__ui.cbxMonitorMonitor.addItem(self.__ui.txtConfigMonitorName.text())
        self.__ui.txtConfigMonitorName.clear()
        self.__ui.txtConfigMonitorLog.clear()
        self.__ui.cbxMonitorSilent.setCurrentIndex(0)

        # self.__ui.cbxMonitorMonitor.setCurrentIndex(self.__ui.cbxMonitorMonitor.count() - 1)
        # self.setMonitorComponentStatus()

        self.__logger.printLog(f"Monitor successfully created.", 'green')
        self.previewListWidget()

    def updateNode(self):
        nodes = self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].getNodes()
        index = self.__ui.cbxConfigNode.currentIndex() - 1

        if self.__ui.txtConfigNodeName.text() == "" or \
                self.__ui.txtConfigNodePath.text() == "" or \
                self.__ui.txtConfigNodePackage.text() == "":
            self.__logger.printLog("Please fill in all Node properties", "red")
            return

        if nodes[index].getName() != self.__ui.txtConfigNodeName.text():
            for nodes in self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].getNodes():
                if nodes.getName() == self.__ui.txtConfigNodeName.text():
                    self.__logger.printLog("Node name must be unique", "red")
                    return

        nodes[index].setName(self.__ui.txtConfigNodeName.text())
        nodes[index].setPath(self.__ui.txtConfigNodePath.text())
        nodes[index].setPackageName(self.__ui.txtConfigNodePackage.text())

        self.__ui.cbxConfigNode.setItemText(self.__ui.cbxConfigNode.currentIndex(), self.__ui.txtConfigNodeName.text())
        self.__ui.cbxConfigTopicNode.setItemText(self.__ui.cbxConfigNode.currentIndex(),
                                                 self.__ui.txtConfigNodeName.text())

        self.__ui.txtConfigNodeName.clear()
        self.__ui.txtConfigNodePath.clear()
        self.__ui.txtConfigNodePackage.clear()

        self.__logger.printLog("Node successfully updated.", 'green')
        self.previewListWidget()

    def updateTopic(self):
        topic = self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].getNodes()[
            self.__ui.cbxConfigTopicNode.currentIndex()].getTopics()[self.__ui.cbxConfigTopicTopic.currentIndex() - 1]

        if self.__ui.txtConfigTopicName.text() == "" or \
                self.__ui.txtConfigTopicType.text() == "":
            self.__logger.printLog("Please fill in all Topic properties", "red")
            return

        if topic.getName() != self.__ui.txtConfigTopicName.text():
            for topics in self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].getNodes()[
                self.__ui.cbxConfigTopicNode.currentIndex()].getTopics():
                if topics.getName() == self.__ui.txtConfigTopicName.text():
                    self.__logger.printLog("Topic name must be unique", "red")
                    return

        topic.setName(self.__ui.txtConfigTopicName.text())
        topic.setType(self.__ui.txtConfigTopicType.text())
        topic.setAction(self.__ui.cbxConfigTopicAction.currentText())

        self.__ui.cbxConfigTopicTopic.setCurrentText(self.__ui.txtConfigTopicName.text())
        self.__ui.txtConfigTopicName.clear()
        self.__ui.txtConfigTopicType.clear()
        self.__ui.cbxConfigTopicAction.setCurrentIndex(0)

        self.__logger.printLog("Topic successfully updated.", 'green')
        self.previewListWidget()

    def updateOracle(self):
        if self.__ui.txtConfigOraclePort.text() == "" or self.__ui.txtConfigOracleUrl.text() == "":
            self.__logger.printLog("Please fill in all Oracle properties", "red")
            return

        if not self.__ui.txtConfigOraclePort.text().isnumeric():
            self.__logger.printLog("Port value must be integer", "red")
            return

        oracle = self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].getOracle()
        oracle.setPort(int(self.__ui.txtConfigOraclePort.text()))
        oracle.setUrl(self.__ui.txtConfigOracleUrl.text())
        oracle.setAction(self.__ui.cbxConfigOracleAction.currentText())
        self.__ui.txtConfigOracleName.setText(self.__ui.txtConfigOraclePort.text() + ':' +
                                              self.__ui.txtConfigOracleUrl.text() + '  -> ' +
                                              self.__ui.cbxConfigOracleAction.currentText())

        self.__logger.printLog("Oracle successfully updated.", 'green')
        self.previewListWidget()

    def updateMonitor(self):
        if self.__ui.txtConfigMonitorName.text() == "" or self.__ui.txtConfigMonitorLog.text() == "":
            self.__logger.printLog("Please fill in all Monitor properties", "red")
            return
        index = self.__ui.cbxMonitorMonitor.currentIndex() - 1

        if self.__monitors[index].getName() != self.__ui.txtConfigMonitorName.text():
            for monitor in self.__monitors:
                if monitor.getName() == self.__ui.txtConfigMonitorName.text():
                    self.__logger.printLog("Monitor name must be unique", "red")
                    return

        self.__monitors[index].setName(self.__ui.txtConfigMonitorName.text())
        self.__monitors[index].setLogFileName(self.__ui.txtConfigMonitorLog.text())
        self.__monitors[index].setSilent(bool(self.__ui.cbxMonitorSilent.currentIndex()))
        self.__ui.cbxMonitorMonitor.setItemText(self.__ui.cbxMonitorMonitor.currentIndex(),
                                                self.__ui.txtConfigMonitorName.text())
        self.__ui.txtConfigMonitorName.clear()
        self.__ui.txtConfigMonitorLog.clear()
        self.__ui.cbxMonitorSilent.setCurrentIndex(0)

        self.__logger.printLog("Monitor successfully updated.", 'green')
        self.previewListWidget()

    def deleteNode(self):
        self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].removeNode(
            self.__ui.cbxConfigNode.currentIndex() - 1)

        self.__ui.cbxConfigTopicNode.removeItem(self.__ui.cbxConfigNode.currentIndex() - 1)
        self.__ui.cbxConfigNode.removeItem(self.__ui.cbxConfigNode.currentIndex())

        self.clearNodeComponents()

        self.__logger.printLog("Node successfully deleted.", 'green')
        self.previewListWidget()

    def deleteTopic(self):
        self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].getNodes()[
            self.__ui.cbxConfigTopicNode.currentIndex()].removeTopic(self.__ui.cbxConfigTopicTopic.currentIndex() - 1)
        self.__ui.cbxConfigTopicTopic.removeItem(self.__ui.cbxConfigTopicTopic.currentIndex())

        self.clearTopicComponents()

        self.__logger.printLog("Topic successfully deleted.", 'green')
        self.previewListWidget()

    def deleteOracle(self):
        self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].setOracle(None)

        self.clearOracleComponents()

        self.__logger.printLog("Oracle successfully deleted.", 'green')
        self.previewListWidget()

    def deleteMonitor(self):
        self.__monitors.pop(self.__ui.cbxMonitorMonitor.currentIndex() - 1)

        self.__ui.txtConfigMonitorName.clear()
        self.__ui.txtConfigMonitorLog.clear()
        self.__ui.cbxMonitorSilent.setCurrentIndex(0)
        self.__ui.cbxMonitorMonitor.removeItem(self.__ui.cbxMonitorMonitor.currentIndex())

        self.__logger.printLog("Monitor successfully deleted.", 'green')
        self.previewListWidget()

    def setNodeComponentStatus(self):
        if self.__ui.cbxConfigNode.currentText() != 'New Node':
            node = self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].getNodes()[
                self.__ui.cbxConfigNode.currentIndex() - 1]
            self.__ui.txtConfigNodeName.setText(node.getName())
            self.__ui.txtConfigNodePackage.setText(node.getPackageName())
            self.__ui.txtConfigNodePath.setText(node.getPath())
            self.__ui.btnConfigNodeUpdate.setEnabled(True)
            self.__ui.btnConfigNodeDelete.setEnabled(True)
            self.__ui.btnConfigNodeCreate.setDisabled(True)
        else:
            self.__ui.txtConfigNodeName.clear()
            self.__ui.txtConfigNodePath.clear()
            self.__ui.txtConfigNodePackage.clear()
            self.__ui.btnConfigNodeCreate.setEnabled(True)
            self.__ui.btnConfigNodeUpdate.setDisabled(True)
            self.__ui.btnConfigNodeDelete.setDisabled(True)

    def clearNodeComponents(self):
        self.__ui.txtConfigNodeName.clear()
        self.__ui.txtConfigNodePath.clear()
        self.__ui.txtConfigNodePackage.clear()
        self.__ui.btnConfigNodeCreate.setEnabled(True)
        self.__ui.btnConfigNodeUpdate.setDisabled(True)
        self.__ui.btnConfigNodeDelete.setDisabled(True)

    def setTopicNodeComponentStatus(self):
        self.__ui.cbxConfigTopicTopic.clear()
        self.__ui.cbxConfigTopicTopic.addItem('New Topic')
        for topic in self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].getNodes()[
            self.__ui.cbxConfigTopicNode.currentIndex()].getTopics():
            self.__ui.cbxConfigTopicTopic.addItem(topic.getName())

    def setTopicComponentStatus(self):
        if self.__ui.cbxConfigTopicTopic.currentText() != 'New Topic':
            topic = self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1].getNodes()[
                self.__ui.cbxConfigTopicNode.currentIndex()].getTopics()[
                self.__ui.cbxConfigTopicTopic.currentIndex() - 1]

            self.__ui.txtConfigTopicName.setText(topic.getName())
            self.__ui.txtConfigTopicType.setText(topic.getType())
            action = topic.getAction()
            if action == 'filter':
                self.__ui.cbxConfigTopicAction.setCurrentIndex(0)
            elif action == 'log':
                self.__ui.cbxConfigTopicAction.setCurrentIndex(1)
            elif action == 'nothing':
                self.__ui.cbxConfigTopicAction.setCurrentIndex(2)

            self.__ui.btnConfigTopicUpdate.setEnabled(True)
            self.__ui.btnConfigTopicDelete.setEnabled(True)
            self.__ui.btnConfigTopicCreate.setDisabled(True)
        else:
            self.__ui.txtConfigTopicName.clear()
            self.__ui.txtConfigTopicType.clear()
            self.__ui.cbxConfigTopicAction.setCurrentIndex(0)
            self.__ui.btnConfigTopicCreate.setEnabled(True)
            self.__ui.btnConfigTopicUpdate.setDisabled(True)
            self.__ui.btnConfigTopicDelete.setDisabled(True)

    def clearTopicComponents(self):
        self.__ui.txtConfigTopicName.clear()
        self.__ui.txtConfigTopicType.clear()
        self.__ui.cbxConfigTopicAction.setCurrentIndex(0)
        self.__ui.btnConfigTopicCreate.setEnabled(True)
        self.__ui.btnConfigTopicUpdate.setDisabled(True)
        self.__ui.btnConfigTopicDelete.setDisabled(True)

    def setMonitorComponentStatus(self):
        if self.__ui.cbxMonitorMonitor.currentText() != 'New Monitor':
            monitor = self.__monitors[self.__ui.cbxMonitorMonitor.currentIndex() - 1]
            self.__ui.txtConfigMonitorName.setText(monitor.getName())
            self.__ui.txtConfigMonitorLog.setText(monitor.getLogFileName())
            if monitor.getSilent():
                self.__ui.cbxMonitorSilent.setCurrentIndex(1)
            else:
                self.__ui.cbxMonitorSilent.setCurrentIndex(0)

            self.fillOracle()
            self.fillNodeLists()
            self.__ui.btnConfigMonitorUpdate.setEnabled(True)
            self.__ui.btnConfigMonitorDelete.setEnabled(True)
            self.__ui.btnConfigMonitorCreate.setDisabled(True)
        else:
            self.__ui.cbxConfigNode.clear()
            self.__ui.cbxConfigTopicNode.clear()
            self.__ui.cbxConfigNode.addItem('New Node')
            self.__ui.cbxConfigTopicTopic.clear()
            self.__ui.cbxConfigTopicTopic.addItem('New Topic')

            self.clearNodeComponents()
            self.clearTopicComponents()
            self.clearOracleComponents()

            self.__ui.txtConfigMonitorName.clear()
            self.__ui.txtConfigMonitorLog.clear()
            self.__ui.cbxMonitorSilent.setCurrentIndex(0)
            self.__ui.btnConfigMonitorCreate.setEnabled(True)
            self.__ui.btnConfigMonitorUpdate.setDisabled(True)
            self.__ui.btnConfigMonitorDelete.setDisabled(True)

    def fillOracle(self):
        index = self.__ui.cbxMonitorMonitor.currentIndex() - 1
        oracle = self.__monitors[index].getOracle()
        if oracle:
            self.__ui.txtConfigOraclePort.setText(str(oracle.getPort()))
            self.__ui.txtConfigOracleUrl.setText(oracle.getUrl())
            if oracle.getAction() == 'filter':
                self.__ui.cbxConfigOracleAction.setCurrentIndex(2)
            elif oracle.getAction() == 'log':
                self.__ui.cbxConfigOracleAction.setCurrentIndex(1)
            elif oracle.getAction() == 'nothing':
                self.__ui.cbxConfigOracleAction.setCurrentIndex(0)
            self.__ui.txtConfigOracleName.setText(
                str(oracle.getPort()) + ':' + oracle.getUrl() + '  -> ' + oracle.getAction())
            self.__ui.btnConfigOracleCreate.setDisabled(True)
            self.__ui.btnConfigOracleUpdate.setDisabled(False)
            self.__ui.btnConfigOracleDelete.setDisabled(False)
        else:
            self.__ui.txtConfigOraclePort.clear()
            self.__ui.txtConfigOracleUrl.clear()
            self.__ui.txtConfigOracleName.clear()
            self.__ui.cbxConfigOracleAction.setCurrentIndex(0)
            self.__ui.btnConfigOracleCreate.setDisabled(False)
            self.__ui.btnConfigOracleUpdate.setDisabled(True)
            self.__ui.btnConfigOracleDelete.setDisabled(True)

    def clearOracleComponents(self):
        self.__ui.txtConfigOraclePort.clear()
        self.__ui.txtConfigOracleUrl.clear()
        self.__ui.txtConfigOracleName.clear()
        self.__ui.cbxConfigOracleAction.setCurrentIndex(0)
        self.__ui.btnConfigOracleCreate.setDisabled(False)
        self.__ui.btnConfigOracleUpdate.setDisabled(True)
        self.__ui.btnConfigOracleDelete.setDisabled(True)

    def fillNodeLists(self):
        index = self.__ui.cbxMonitorMonitor.currentIndex() - 1
        nodes = self.__monitors[index].getNodes()
        self.__ui.cbxConfigNode.clear()
        self.__ui.cbxConfigTopicNode.clear()
        self.__ui.cbxConfigNode.addItem('New Node')
        for node in nodes:
            self.__ui.cbxConfigNode.addItem(node.getName())
            self.__ui.cbxConfigTopicNode.addItem(node.getName())

    def previewListWidget(self):
        self.__ui.listWidget.clear()
        for line in self.cast2configFile().split('\n'):
            self.__ui.listWidget.addItem(line)

    def saveConfig2file(self):
        if not self.__ui.txtConfigSaveYaml.text():
            self.__logger.printLog("Please fill the file name field.", color="red")
            return
        if not self.__monitors.__len__():
            self.__logger.printLog("Can not cast to file, no monitor exists.", color="red")
            return
        try:
            with open(self.__ui.txtConfigSaveYaml.text() + ".yaml", 'w') as file:
                if not file:
                    raise IOError("An error occurred while reading the file", color="red")
                file.write(self.cast2configFile())
                self.__logger.printLog("Config file successfully created.", "green")
        except IOError:
            self.__logger.printLog("An error occurred while reading the file", color="red")
        except:
            self.__logger.printLog("ERROR in saveConfig2file()", color="red")

    def importConfig(self):
        fname = 'file/to/open'
        try:
            fname, filter = QFileDialog.getOpenFileName(None, 'Select config file', '', 'Graph (*.yaml);;All files (*)')
            if not fname:
                raise ImportError(f"<CONFIG IMPORT> An error occurred while {fname} importing")
            self.insertConfigFile(fname)

        except ImportError:
            self.__logger.printLog(f"An error occurred while {fname} importing")
        except:
            self.__logger.printLog(f"An error occurred while {fname} importing")
        finally:
            pass

    def cast2configFile(self):
        fileNodes = "#CREATED FILE\n\n"
        fileTopics = ""
        nodeList = []
        if len(self.__monitors) > 0:
            fileTopics += 'monitors:\n'
            for monitor in self.__monitors:
                fileTopics += '  - monitor:\n'
                fileTopics += '      id: ' + monitor.getName() + '\n'
                fileTopics += '      log: ' + monitor.getLogFileName() + '\n'
                fileTopics += '      silent: ' + str(monitor.getSilent()) + '\n'
                oracle = monitor.getOracle()
                if oracle:
                    fileTopics += '      oracle:\n'
                    fileTopics += '        port: ' + str(oracle.getPort()) + '\n'
                    fileTopics += '        url: ' + oracle.getUrl() + '\n'
                    fileTopics += '        action: ' + oracle.getAction() + '\n'
                topicList = monitor.getTopics()
                if len(topicList) > 0:
                    fileTopics += '      topics:\n'
                    for topic in topicList:
                        fileTopics += '        - name: ' + topic.getName() + '\n'
                        fileTopics += '          type: ' + topic.getType() + '\n'
                        fileTopics += '          action: ' + topic.getAction() + '\n'
                        publisherList = topic.getPublishers()
                        if len(publisherList) > 0:
                            fileTopics += '          publishers:\n'
                            for publisher in publisherList:
                                fileTopics += '            - ' + publisher + '\n'
                for node in monitor.getNodes():
                    if node not in nodeList and node:
                        nodeList.append(node)

            if len(nodeList) > 0:
                fileNodes += 'nodes:\n'
                for node in nodeList:
                    fileNodes += '  - node:\n'
                    fileNodes += '      name: ' + node.getName() + '\n'
                    fileNodes += '      package: ' + node.getPackageName() + '\n'
                    fileNodes += '      path: ' + node.getPath() + '\n'
                fileNodes += '\n\n'

        return fileNodes + fileTopics

    def insertConfigFile(self, filename):
        f = open(filename, 'r')
        nodeList = []
        line = f.readline()
        while line:
            line = line.strip()
            if line[:7] == "- node:":
                node = Node(name=(f.readline().replace(' ', '').replace("name:", "")).split("#")[0].rstrip("\n"),
                            type=None,
                            packageName=(f.readline().replace(' ', '').replace("package:", "")).split("#")[0].rstrip(
                                "\n"),
                            path=(f.readline().replace(' ', '').replace("path:", "")).split("#")[0].rstrip("\n"),
                            launchName=None,
                            topics=[])
                nodeList.append(node)
            if line[:9] == "monitors:":
                break
            line = f.readline()
        while line:
            if line[:9] == "monitors:":
                (f.readline())
                monitor = Monitor(name=(f.readline().replace(' ', '').replace("id:", "")).split("#")[0].rstrip("\n"),
                                  logFileName=(f.readline().replace(' ', '').replace("log:", "")).split("#")[0].rstrip(
                                      "\n"),
                                  silent=bool(
                                      (f.readline().replace(' ', '').replace("silent:", "")).split("#")[0].rstrip(
                                          "\n")),
                                  oracle=None, nodes=[])
                (f.readline())
                oracle = Verifier(
                    port=int((f.readline().replace(' ', '').replace("port:", "")).split("#")[0].rstrip("\n")),
                    url=(f.readline().replace(' ', '').replace("url:", "")).split("#")[0].rstrip("\n"),
                    action=(f.readline().replace(' ', '').replace("action:", "")).split("#")[0].rstrip("\n"))
                monitor.setOracle(oracle)
                while line:
                    line = line.strip()
                    if line[:7] == "- name:":  # topic
                        topic = Topic(name=(line.replace(' ', '').replace("-name:", "")).split("#")[0].rstrip("\n"),
                                      type=(f.readline().replace(' ', '').replace("type:", "")).split("#")[0].rstrip(
                                          "\n"),
                                      action=(f.readline().replace(' ', '').replace("action:", "")).split("#")[
                                          0].rstrip("\n"),
                                      publishers=[])
                        f.readline()
                        subLine = f.readline()
                        while subLine:
                            if subLine[:14] != "            - ":
                                break
                            subLine = (subLine.replace(' ', '').replace("-", "")).split("#")[0].rstrip("\n")
                            if not topic.getPublishers():
                                topic.addPublisher(subLine)
                                indexofnode = self.findIndexOfNode(nodeList, subLine)
                                nodeList[indexofnode].appendTopic(topic)
                                monitor.appendNode(nodeList[indexofnode])
                            subLine = f.readline()
                    line = f.readline()
                self.__monitors.append(monitor)
                self.__ui.cbxMonitorMonitor.addItem(monitor.getName())
            line = f.readline()
        self.previewListWidget()

    @staticmethod
    def findIndexOfNode(nodes: [Node], name: str):
        for i in range(nodes.__len__()):
            if nodes[i].getName() == name:
                return i
