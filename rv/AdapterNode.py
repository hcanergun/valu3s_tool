import Node


class AdapterNode(Node):
    def __init__(self, name: str = None, type: str = None, path: str = None, launchName: str = None,
                 packageName: str = None, topics: list = None):
        Node.__init__(self, name, type, path, launchName, packageName, topics)
