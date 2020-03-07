
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, Node=Node):
        self.root = None
        self.count = 0
        self.Node = Node

    # Public Methods Section #
    def insert(self, value):
        self._insert_in(self, self.root, value)

    def contains(self, value):
        return self._contains_in(self.root, value)

    def remove_all(self):
        self._post_order_removing()
        self.count = 0

    # Private Methods Section #
    def _insert_in(self, current_node, value):
        if not current_node:
            self.count += 1
            return self.Node(value)
        elif value < current_node.value:
            current_node.left = self._insert_in(current_node.left, value)
        else:
            current_node.right = self._insert_in(current_node.right, value)

        return current_node

    def _contains_in(self, current_node, value):
        if not current_node:
            return False
        elif value < current_node.value:
            return self._contains_in(current_node.left, value)
        elif value > current_node.value:
            return self._contains_in(current_node.right, value)
        else:
            return True

    def _post_order_removing(self, current_node):
        if current_node:
            current_node.left = self._post_order_removing(current_node.left)
            current_node.right = self._post_order_removing(current_node.right)
        return None
