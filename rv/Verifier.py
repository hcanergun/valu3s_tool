class Verifier:
    def __init__(self, port: int = None, url: str = None, action: str = None, properties: list = None):
        self.__port = port
        self.__url = url
        self.__action = action
        self.__properties = properties

    def setPort(self, port: int):
        self.__port = port

    def getPort(self) -> int:
        return self.__port

    def setUrl(self, url: str):
        self.__url = url

    def getUrl(self) -> str:
        return self.__url

    def setAction(self, action: str):
        self.__action = action

    def getAction(self) -> str:
        return self.__action

    def setProperties(self, properties: list):
        if self.__properties:
            self.__properties.extend(properties)
        else:
            self.__properties = properties

    def getProperties(self) -> list:
        return self.__properties
