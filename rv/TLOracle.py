import Verifier


class TLOracle(Verifier):
    def __init__(self, port: int, url: str, action: str):
        super(TLOracle, self).__init__(port, url, action)
