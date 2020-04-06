# TODO
# - binary_search
# - get_key
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
        result = ''
        result += str(self._root) + '\n'
        for i, child in enumerate(self._root.children):
            result += f'child[{i}] = {str(child)}\n'

        return result

    #def __str__(self):
    #    inorder = []
    #    for i in self:
    #        inorder.append(i)
    #    return str(inorder)

    def __iter__(self):
        for i in self._in_order(self._root):
            yield i

    def __contains__(self, key):
        return self._get_bkey(self._root, key) is not False

    # Public Methods Section #
    def is_empty(self):
        return len(_root) == 0

    def insert(self, key):
        self._count += 1
        if self._correct(self._root) is False:
            self._height +=1
            new_root = BNode()
            new_root.leaf = False
            new_root.children.append(self._root)
            self._root = new_root
            self._split_child_of(new_root, 0)
        
        self._insert_into_nonfull(self._root, key)

    # Private Methods Section #
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
        # TODO binary search
        if node.leaf:
            #if len(node) > 0:
            i, _ = self._search(node.keys, key)
                #if key > node.keys[-1]:
                #    i = len(node)
            node.keys.insert(i, key)
            #node.keys.append(key)
            #while i >= 0 and key < node.keys[i]:
            #    node.keys[i+1], node.keys[i] = node.keys[i], node.keys[i+1]
            #    i -= 1
            
        else:
            i, _ = self._search(node.keys, key)
            #if key < node.keys[0]:
            #    i = -1
            #while i >= 0 and key < node.keys[i]:
            #    i -= 1
            #i += 1
            if self._correct(node.children[i]) is False:
                self._split_child_of(node, i)
                if key > node.keys[i]:
                    i += 1

            self._insert_into_nonfull(node.children[i], key)

    def binary_search(self, keys, key):
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
        i, contains = self.binary_search(keys, key)
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
