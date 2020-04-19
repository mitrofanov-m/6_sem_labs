from functools import total_ordering
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
    def __init__(self, load_factor=2.0, hfunc=hash, length=0):
        self._hash = hfunc
        self._length = length
        self._buckets = [list() for i in range(2 * self._length + 5)]
        self._load_factor = load_factor

        self.__KEYTYPE = None
        self.__VALTYPE = None

    # Properties Section #
    @property
    def load(self):
        return round(self._length / len(self._buckets), 3)

    @property
    def load_factor(self):
        return self._load_factor

    @load_factor.setter
    def load_factor(self, load_factor):
        self._load_factor = load_factor if load_factor > 0.5 else 0.5

        if self.load >= self._load_factor:
             self._rehashing_to(2 * len(self._buckets) + 1)


    # Magic Methods Section #
    def __repr__(self):
        return str(self._buckets)

    def __len__(self):
        return self._length

    def __iter__(self):
        for bucket in self._buckets:
            for item in bucket:
                yield item

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

            if self.load >= self._load_factor:
                self._rehashing_to(2 * len(self._buckets) + 1)

    def __delitem__(self, key):
        if isinstance(key, self.__KEYTYPE):
            bucket = self._bucket_of(key)
            for i, item in enumerate(bucket):
                if item == key:
                    del bucket[i]
                    self._length -= 1
                    return
        raise KeyError("Incorrect key")

    # Public Methods Section #
    def remove_all(self):
        for bucket in self._buckets:
            bucket.clear()
        self._length = 0

    def compress(self):
        optimal_load = self.load_factor - 0.2
        optimal_num = round(self._length / optimal_load)
        self._rehashing_to(optimal_num)

    # Private Methods Section #
    def _rehashing_to(self, num):
        new_buckets = [list() for i in range(num)]
        for item in self:
            bucket = self._bucket_of(item.key, buckets=new_buckets)
            bucket.append(item)

        self._buckets = new_buckets

    def _bucket_of(self, key, buckets=None):
        _buckets = buckets or self._buckets
        index = self._hash(key) % len(_buckets)
        return _buckets[index]

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
