from rv.Verifier import Verifier


class RMLOracle(Verifier):
    def __init__(self, port: int, url: str, action: str):
        super(RMLOracle, self).__init__(port, url, action)