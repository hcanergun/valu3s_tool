class Node:
    def __init__(self, name: str = None, type: str = None, path: str = None, launchName: str = None,
                 packageName: str = None, topics: list = None):
        self.__name = name
        self.__type = type
        self.__path = path
        self.__launchName = launchName
        self.__packageName = packageName
        self.__topics = topics

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getType(self) -> str:
        return self.__type

    def setType(self, type: str):
        self.__type = type

    def getLaunchName(self) -> str:
        return self.__launchName

    def setLaunchName(self, launchName: str):
        self.__launchName = launchName

    def getPackageName(self) -> str:
        return self.__packageName

    def setPackageName(self, packageName: str):
        self.__packageName = packageName

    def getTopics(self) -> list:
        return self.__topics

    def setTopics(self, topics: list):
        self.__topics = topics
