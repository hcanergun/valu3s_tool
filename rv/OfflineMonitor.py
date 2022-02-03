import Monitor
import Verifier
from rv.Topic import Topic
from rv.Node import Node


class OfflineMonitor(Monitor):
    def __init__(self, name: str = None, logFileName: str = None, silent: bool = None, oracle: Verifier = None,
                 nodes: [Node] = [], topics: [Topic] = []):
        super(OfflineMonitor, self).__init__(name, logFileName, silent, oracle, nodes, topics)

    def generate(self) -> bool:
        pass
