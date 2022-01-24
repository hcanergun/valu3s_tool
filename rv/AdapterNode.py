import Node


class AdapterNode(Node):
    def __init__(self, name: str, type: str, path: str, launchName: str, packageName: str, topics: list):
        Node.__init__(self, name, type, path, launchName, packageName, topics)
