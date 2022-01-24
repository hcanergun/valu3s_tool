import Node


class SystemNode(Node):
    def __init__(self, name: str, type: str, path: str, launchName: str, packageName: str, topics: list):
        super(SystemNode, self).__init__(name, type, path, launchName, packageName, topics)
