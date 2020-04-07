# TODO
# + _binary_search
# + get_key
# 


class BNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

    def __len__(self):
        return len(self.keys)

    def __str__(self):
        return str(self.keys)

    def is_empty(self):
        return len(keys) == 0

class Btree:
    def __init__(self, t):
        if t < 2:
            raise AttributeError("Use t > 1")

        self._t = t
        self._count = 0
        self._height = 0
        self._root = BNode(leaf=True)

    def __len__(self):
        return self._count

    def __str__(self):
        inorder = []
        for i in self:
            inorder.append(i)
        return str(inorder)

    def __iter__(self):
        for i in self._in_order(self._root):
            yield i

    def __contains__(self, key):
        _, result = self._get_bkey(key)
        return result


    # Public Methods Section #
    def is_empty(self):
        return self._count == 0

    def insert(self, key):
        self._count += 1
        if self._incorrect(self._root):
            self._height +=1
            new_root = BNode()
            new_root.leaf = False
            new_root.children.append(self._root)
            self._root = new_root
            self._split_child_of(new_root, 0)
        
        self._insert_into_nonfull(self._root, key)

    def remove_all(self):
        self._count = 0
        self._height = 0
        self._root = BNode(leaf=True)


    # Private Methods Section #
    def _incorrect(self, node):
        t = self._t
        result = False
        if len(node) < t - 1:
            result = True if self._root != node else False
        if len(node) >= t * 2 - 1:
            result = True

        return result

    def _get_bkey(self, key):
        node = self._root
        while True:
            i, contains = self._search(node.keys, key)
            
            if contains:
                return node.keys[i-1], True
            elif node.leaf:
                return None, False
            else:
                node = node.children[i]

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
        i, _ = self._search(node.keys, key)
        if node.leaf:
            node.keys.insert(i, key)    
        else:
            if self._incorrect(node.children[i]):
                self._split_child_of(node, i)
                if key > node.keys[i]:
                    i += 1

            self._insert_into_nonfull(node.children[i], key)

    def _binary_search(self, keys, key):
        left, right = 0, len(keys) - 1
        middle = 0
        while left <= right:
            middle = (left + right) // 2
            if keys[middle] == key:
                return middle, True
            if keys[middle] < key:
                left = middle + 1
            elif keys[middle] > key:
                right = middle - 1
        return middle, False

    def _search(self, keys, key):
        i, contains = self._binary_search(keys, key)
        while i < len(keys) and key >= keys[i]:
            i += 1

        return i, contains

    def _in_order(self, node):
        if node.leaf:
            for i in node.keys:
                yield i
        else:
            for i, key in enumerate(node.keys):
                for j in self._in_order(node.children[i]):
                    yield j

                yield key

            for j in self._in_order(node.children[-1]):
                yield j
