
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # thanks to groupmate for this feature
    def __str__(self):
        return self.diagram(self, "", "", "")

    def diagram(self, node, top, root, bottom):
        if node is None:
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

    def __len__(self):
        return self.__count

    def __contains__(self, value):
        return self._contains_in(self.__root, value)

    def __iter__(self):
        if self.__root is not None:
            for value in self._in_order(self.__root):
                yield value

    # Public Methods Section #
    def insert(self, value):
        self.__root = self._insert_in(self.__root, value)

    def remove(self, value):
        if value in self:
            self.__count -= 1
            self.__root = self._remove(value, self.__root)
            return True
        return False

    def remove_all(self):
        self._post_order_removing()
        self.__count = 0

    # Private Methods Section #
    def _insert_in(self, node, value):
        if node is None:
            self.__count += 1
            return self.__Node(value)
        elif value < node.value:
            node.left = self._insert_in(node.left, value)
        else:
            node.right = self._insert_in(node.right, value)

        return node

    def _contains_in(self, node, value):
        if node is None:
            return False
        elif value < node.value:
            return self._contains_in(node.left, value)
        elif value > node.value:
            return self._contains_in(node.right, value)
        else:
            return True

    def _remove(self, value, node):
        if node is None:
            return None

        if value == node.value:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            child = node.left
            while child.right:
                child = child.right

            node.value = child.value
            node.left = self._remove(node.value, node.left)

        elif value < node.value:
            node.left = self._remove(value, node.left)
        else:
            node.right = self._remove(value, node.right)

        return node

    def _in_order(self, node):
        if node.left:
            for value in self.inorder(node.left):
                yield value

        yield node.value

        if node.right:
            for value in self.inorder(node.right):
                yield value

    def _post_order_removing(self, node):
        if node is not None:
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

    def _remove(self, node, value):
        node = super()._remove(node, value)
        # append balancing of node that is returned
        if node is not None:
            return self._balanced(node)


    def _get_height(self, node):
        if node is None:
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
        if node is None:
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
