import Monitor
import Verifier

class OfflineMonitor(Monitor):
    def __init__(self, name: str, logFileName: str, silent: bool, oracle: Verifier, nodes: list, topics: list):
        super(OfflineMonitor, self).__init__(name, logFileName, silent, oracle, nodes, topics)

    def generate(self) -> bool:
        pass
