from rv.Verifier import Verifier


class TLOracle(Verifier):
    def __init__(self, port: int = None, url: str = None, action: str = None, properties: list = None):
        super(TLOracle, self).__init__(port, url, action, properties)
