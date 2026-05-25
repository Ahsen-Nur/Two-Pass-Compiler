class ASTNode:

    def __init__(self, node_type, value=None):

        self.node_type = node_type
        self.value = value

        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print_tree(self, level=0):

        indent = "  " * level

        print(f"{indent}{self.node_type}: {self.value}")

        for child in self.children:
            child.print_tree(level + 1)