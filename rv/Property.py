class Property:
    def __init__(self, name: str = None, description: str = None, formula: str = None, nodeNames: list = None):
        self.__name = name
        self.__description = description
        self.__formula = formula
        self.__nodeNames = nodeNames

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getDescription(self) -> str:
        return self.__description

    def setDescription(self, description: str):
        self.__description = description

    def getFormula(self) -> str:
        return self.__formula

    def setFormula(self, formula: str):
        self.__formula = formula
