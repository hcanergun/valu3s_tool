from rv.Node import Node
from rv.Verifier import Verifier


class Monitor:

    def __init__(self, name: str = None, logFileName: str = None, silent: bool = False, oracle: Verifier = None,
                 nodes: [Node] = None, topics: list = None):
        self.__name = name
        self.__logFileName = logFileName
        self.__silent = silent
        self.__oracle = oracle
        self.__nodes = nodes
        self.__topics = topics

    def generate(self) -> bool:
        pass

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getLogFileName(self) -> str:
        return self.__logFileName

    def setLogFileName(self, logFileName: str):
        self.__logFileName = logFileName

    def getSilent(self) -> bool:
        return self.__silent

    def setSilent(self, silent: bool):
        self.__silent = silent

    def getNodes(self) -> list:
        return self.__nodes

    def setNodes(self, nodes: list):
        self.__nodes = nodes

    def getTopics(self) -> list:
        return self.__topics

    def setTopics(self, topics: list):
        self.__topics = topics
