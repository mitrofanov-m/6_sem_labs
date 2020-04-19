from functools import total_ordering
# TODO: init from last_map
# TODO: _rehashing

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


class HashMap:
    def __init__(self, last_map=None, load_factor=2.0, hfunc=hash):
        # TODO: init from last_map
        self.hash = hfunc
        self._length = 0
        self.buckets = [list() for i in range(2 * self.length + 5)]
        self.load_factor = load_factor

        self.__KEYTYPE = None
        self.__VALTYPE = None

        #if type(last_map) is HashMap:
        #    self.__KEYTYPE = last_map._Map__KEYTYPE
        #    self.__VALTYPE = last_map._Map__VALTYPE

            # for item in last_map:
            #     self.insert(item)

    # Properties Section
    @property
    def load(self):
        return self._length / len(self.buckets)

    @property
    def load_factor(self):
        return self.load_factor

    @load_factor.setter
    def load_factor(self, load_factor):
        self.load_factor = load_factor if load_factor > 0.2 else 0.2


    # Magic Methods Section
    def __len__(self):
        return self._length

    def __getitem__(self, key):
        bucket = self._bucket_of(key)
        for item in bucket:
            if item == key:
                return item.value
        else:
            raise KeyError("Incorrect key")

    def __setitem__(self, key, value):
        new_item = MapItem(key, value)
        if self.__KEYTYPE is None and self._comprable(new_item):
            self.__KEYTYPE = type(new_item.key)
            self.__VALTYPE = type(new_item.value)
        else:
            self._check_types_of(new_item)
            bucket = self._bucket_of(key)
            for item in bucket:
                if item == key:
                    item.value = value
                    break
            else:
                bucket.append(new_item)
                self._length += 1

                if self.load >= self.load_factor:
                    # TODO: _rehashing
                    # self._rehashing(2 * self.number_of_lists + 1)

    def __delitem__(self, key):
        if isinstance(key, self.__KEYTYPE):
            bucket = self._bucket_of(key)
            for i, item in enumerate(bucket):
                if item == key:
                    del bucket[i]
                    self._length -= 1
                    return
        raise KeyError("Incorrect key")

    # Private Methods Section #
    def _bucket_of(self, key):
        index = self.hash(key) % len(self.buckets)
        return self.buckets[index]

    def _check_types_of(self, item):
        if not isinstance(item.value, self.__VALTYPE) or \
           not isinstance(item.key, self.__KEYTYPE):
            raise \
                TypeError("The map cannot contains different types")
        return self._comprable(item)

    def _comprable(self, item):
        methods = ("__lt__", "__le__", "__eq__",
                   "__ne__", "__gt__", "__ge__")
        for attr in methods:
            if not hasattr(item.key, attr):
                raise TypeError("Type is not comparable")
        return True
