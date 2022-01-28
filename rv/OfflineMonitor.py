import Monitor
import Verifier


class OfflineMonitor(Monitor):
    def __init__(self, name: str = None, logFileName: str = None, silent: bool = None, oracle: Verifier = None,
                 nodes: list = None, topics: list = None):
        super(OfflineMonitor, self).__init__(name, logFileName, silent, oracle, nodes, topics)

    def generate(self) -> bool:
        pass
