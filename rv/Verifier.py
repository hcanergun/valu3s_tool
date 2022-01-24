class Verifier:
    def __init__(self, port: int, url: str, action: str):
        self.__port = port
        self.__url = url
        self.__action = action

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
