class Topic:
    def __init__(self, name: str, type: str, action: str, publishers: [str]):
        self.__name = name
        self.__type = type
        self.__action = action
        self.__publishers = publishers

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getType(self) -> str:
        return self.__type

    def setType(self, type: str):
        self.__type = type

    def getAction(self) -> str:
        return self.__action

    def setAction(self, action: str):
        self.__action = action

    def getPublishers(self) -> list:
        return self.__publishers

    def setPublishers(self, publishers: list):
        self.__publishers = publishers
