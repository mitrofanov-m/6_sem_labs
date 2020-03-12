from functools import total_ordering
from AVLTree import *
from copy import deepcopy

@total_ordering
class MapItem:
    def __init__(self, key, value):
            self.key = key
            self.value = value

    def __eq__(self, other):
        if type(other) is not MapItem:
            return self.key == other
        return self.key == other.key

    def __lt__(self, other):
        if type(other) is not MapItem:
            return self.key < other

        return self.key < other.key

    def __repr__(self):
        return '{' + str(self.key) + ' : ' + str(self.value) + '}'


class Map(AVLTree):

    def __init__(self, last_map=None):
        super().__init__()

        self.__KEYTYPE = None
        self.__VALTYPE = None

        if type(last_map) is Map:
            self.__KEYTYPE = last_map._Map__KEYTYPE
            self.__VALTYPE = last_map._Map__VALTYPE
            
            for item in last_map:
                self.insert(item)

    def __str__(self):
        inorder = []
        for i in self:
            inorder.append(i)
        return str(inorder)

    def __getitem__(self, key):
        node = self._get_node_by_item(self._BinaryTree__root, key)
        if node is None:
            raise KeyError("Incorrect key") 

        if node.item == key:
            return node.item.value

    def __setitem__(self, key, value):
        item = MapItem(key, value)
        if self.__KEYTYPE is None and self._comprable(item):
            self.__KEYTYPE = type(item.key)
            self.__VALTYPE = type(item.value)
        else:
            self._check_type(item)

        if key in self:
            self.remove(key)

        self.insert(item)

    def __delitem__(self, key):
        removed = self.remove(key)
        if not removed:
            raise KeyError("Incorrect key")

    # Private Methods Section #
    def _check_type(self, item):
        if not isinstance(item.value, self.__VALTYPE) or \
           not isinstance(item.key, self.__KEYTYPE):
            raise \
                TypeError("The map cannot contains different types")
        self._comprable(item)

    def _comprable(self, item):
        methods = ("__lt__", "__le__", "__eq__",
                   "__ne__", "__gt__", "__ge__")
        for attr in methods:
            if not hasattr(item.key, attr):
                raise TypeError("Type is not comparable")
        return True
