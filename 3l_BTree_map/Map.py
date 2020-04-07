from functools import total_ordering
from Btree import Btree

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


class Map(Btree):

    def __init__(self, t=2, last_map=None):
        super().__init__(t)

        self.__KEYTYPE = None
        self.__VALTYPE = None

        if type(last_map) is Map:
            self.__KEYTYPE = last_map._Map__KEYTYPE
            self.__VALTYPE = last_map._Map__VALTYPE
            
            for item in last_map:
                self.insert(item)

    def __getitem__(self, key):
        bkey, contains = self._get_bkey(key)
        if not contains:
            raise KeyError("Incorrect key") 
        if bkey == key:
            return bkey.value

    def __setitem__(self, key, value):
        item = MapItem(key, value)
        if self.__KEYTYPE is None and self._comprable(item):
            self.__KEYTYPE = type(item.key)
            self.__VALTYPE = type(item.value)
        else:
            self._check_type(item)

        bkey, contains = self._get_bkey(key)
        if not contains:
            self.insert(item)
        if bkey == key:
            bkey.value = value


    #def __delitem__(self, key):
    #    removed = self.remove(key)
    #    if not removed:
    #        raise KeyError("Incorrect key")

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