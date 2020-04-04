
class BNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

    def __len__(self):
        return len(self.keys)

    def is_empty(self):
        return len(keys) == 0

class Btree:
    def __init__(self, t):
        if t < 2:
            raise AttributeError("Use t > 1")

        self._t = t
        self._count = 0
        self._root = BNode(leaf=True)

    def is_empty(self):
        return len(_root) == 0

    def _correct(self, node):
        t = self._t
        result = True
        if len(node) < t - 1:
            result = False if self._root != node else True
        if len(node) >= t * 2 - 1:
            result = False

        return result

    def _split_child_of(self, parent, child_index):
        new_child = BNode()
        child = parent.children[child_index]
        new_child.leaf = child.leaf
        middle_index = self._t - 1

        middle_key = child.keys[middle_index]
        new_child.keys = child.keys[middle_index + 1:]
        child.keys = child.keys[:middle_index]

        if not child.leaf:
            new_child.children = child.children[middle_index + 1:]
            child.children = child.children[:middle_index + 1]

        parent.keys.insert(child_index, middle_key)
        parent.children.insert(child_index + 1, new_child)

    def _insert_into_nonfull(self, node, key):
        i = len(node) - 1

        if node.leaf:
            node.keys.append(key)
            while i >= 0 and key < node.keys[i]:
                node.keys[i+1], node.keys[i] = node.keys[i], node.keys[i+1]
                i -= 1
            
        else:
            while i > 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if self._correct(node.children[i]) is False:
                self._split_child(node, i)
                if key > node.keys[i]:  
                    i += 1

            self._insert_into_nonfull(node.children[i], key)

    def insert(self, key):
        self._count += 1
        if self._correct(self._root) is False:
            new_root = BNode()
            new_root.leaf = False
            new_root.children.append(self._root)
            self._root = new_root
            self._split_child_of(new_root, 0)
            self._insert_into_nonfull(self._root, key)
        else:
            self._insert_into_nonfull(self._root, key)


