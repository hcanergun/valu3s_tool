from rv.Verifier import Verifier
from rv.Property import Property


class TLOracle(Verifier):
    def __init__(self, port: int = None, url: str = None, action: str = None,
                 properties: [Property] = []):
        super(TLOracle, self).__init__(port, url, action, properties)
