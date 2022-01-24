import Monitor
import Verifier

class OnlineMonitor(Monitor):
    def __init__(self, name: str, logFileName: str, silent: bool, oracle: Verifier, nodes: list, topics: list):
        super(OnlineMonitor, self).__init__(name, logFileName, silent, oracle, nodes, topics)

    def generate(self) -> bool:
        pass
