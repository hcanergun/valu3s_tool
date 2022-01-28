import Node


class SystemNode(Node):
    def __init__(self, name: str = None, type: str = None, path: str = None, launchName: str = None,
                 packageName: str = None, topics: list = None):
        super(SystemNode, self).__init__(name, type, path, launchName, packageName, topics)
