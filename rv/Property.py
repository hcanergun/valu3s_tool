class Property:
    def __init__(self, name: str, description: str, formula: str):
        self.__name = name
        self.__description = description
        self.__formula = formula

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