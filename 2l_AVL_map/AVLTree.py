
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # thanks to classmate for this feature
    def __str__(self):
        return self.diagram(self, "", "", "")

    def diagram(self, node, top, root, bottom):
        if not node:
            return root + "nil\n"
        if node.left is None and node.right is None:
            return root + " " + str(node.value) + "\n"
        return self.diagram(node.right, top + " ", top + "┌──", top + "│ ") + \
               root + str(node.value) + "\n" + \
               self.diagram(node.left, bottom + "│ ", bottom + "└──", bottom + " ")


class BinaryTree:
    def __init__(self, Node=Node):
        self.__root = None
        self.__count = 0
        self.__Node = Node

    def __str__(self):
        return str(self.__root)

    # Public Methods Section #
    def insert(self, value):
        self.__root = self._insert_in(self.__root, value)

    def contains(self, value):
        return self._contains_in(self.__root, value)

    def remove_all(self):
        self._post_order_removing()
        self.__count = 0

    def in_order(self):
        traverse_list = []
        self._in_order(self.__root, traverse_list)
        return traverse_list

    # Private Methods Section #
    def _insert_in(self, node, value):
        if not node:
            self.__count += 1
            return self.__Node(value)
        elif value < node.value:
            node.left = self._insert_in(node.left, value)
        else:
            node.right = self._insert_in(node.right, value)

        return node

    def _contains_in(self, node, value):
        if not node:
            return False
        elif value < node.value:
            return self._contains_in(node.left, value)
        elif value > node.value:
            return self._contains_in(node.right, value)
        else:
            return True

    def _in_order(self, node, traverse_list):
        if node:
            self._in_order(node.left, traverse_list)
            traverse_list.append(node.value)
            self._in_order(node.right, traverse_list)

    def _post_order_removing(self, node):
        if node:
            node.left = self._post_order_removing(node.left)
            node.right = self._post_order_removing(node.right)
            node.value = None
        return None


class AVLNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.height = 1


class AVLTree(BinaryTree):
    def __init__(self):
        super().__init__(AVLNode)

    # Private Methods Section #
    def _insert_in(self, node, value):
        node = super()._insert_in(node, value)
        # append balancing of node that is returned
        return self._balanced(node)

    def _get_height(self, node):
        if not node:
            return -1

        return node.height

    def _refresh_height(self, node):
        return 1 + max(self._get_height(node.left),
                       self._get_height(node.right))

    def _right_rotate(self, node):
        pivot = node.left
        node.left = pivot.right
        pivot.right = node

        node.height = self._refresh_height(node)
        pivot.height = self._refresh_height(pivot)

        return pivot

    def _left_rotate(self, node):
        pivot = node.right
        node.right = pivot.left
        pivot.left = node

        node.height = self._refresh_height(node)
        pivot.height = self._refresh_height(pivot)

        return pivot

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.right) - self._get_height(node.left)

    def _balanced(self, node):
        if self._get_balance(node) == 2:
            if self._get_balance(node.right) == -1:
                node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        elif self._get_balance(node) == -2:
            if self._get_balance(node.left) == 1:
                node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        else:
            node.height = self._refresh_height(node)
            return node
