
class Heap:

    def __init__(self, order, heap=[]):
        if order not in (min, max):
            raise NameError("Incorrect order. Use 'min' or 'max'.")

        self.__heap = heap
        self.order = order

        if self.__heap:
            self._heapify()

    # Public Methods Section #
    def __str__(self):
        return str(self.__heap)

    def __len__(self):
        return len(self.__heap)

    def peek(self):
        return self.__heap[0]

    def empty(self):
        return len(self.__heap) == 0

    def hpush(self, value):
        self.__heap.append(value)
        self._sift_up(len(self.__heap) - 1)

    def hpop(self):
        heap = self.__heap
        if heap:
            first = heap[0]
            self._swap(0, -1)
            del heap[-1]
            self._sift_down(0)
            return first
        else:
            raise Exception("Heap is empty")

    # Private Methods Section #
    def _in_order(self, parent, child):
        return self.order(parent, child) == parent

    def _parent_of(self, i):
        return (i - 1) // 2

    def _left_child_of(self, i):
        return 2 * i + 1

    def _right_child_of(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

    def _heapify(self):
        _parent_of_last = self._parent_of(len(self.__heap) - 1)
        parents = range(_parent_of_last, -1, -1)

        for parent in parents:
            self._sift_down(parent)

    def _sift_up(self, current):
        in_order = self._in_order
        heap = self.__heap
        parent = self._parent_of(current)
        while current > 0 and not in_order(heap[parent], heap[current]):
            self._swap(current, parent)
            current = parent
            parent = self._parent_of(current)

    def _sift_down(self, current):
        in_order = self._in_order
        heap = self.__heap
        size = len(heap)

        while self._left_child_of(current) < size:
            left_child = self._left_child_of(current)
            right_child = self._right_child_of(current)
            _swapped = current

            if not in_order(heap[_swapped], heap[left_child]):
                _swapped = left_child

            if right_child < size and \
                    not in_order(heap[_swapped], heap[right_child]):
                _swapped = right_child

            if _swapped == current:
                return
            else:
                self._swap(current, _swapped)
                current = _swapped


class PriorityQueue:
    def __init__(self, collection=[], order=min):
        self.__TYPE = None
        collection = list(collection)

        if collection:
            self.__TYPE = type(collection[0])
        for value in collection:
            self._check_type(value)

        self.__queue = Heap(order, collection)

    # Public Methods Section #
    def __str__(self):
        return str(self.__queue)

    def __len__(self):
        return len(self.__queue)

    def peek(self):
        return self.__queue.peek()

    def get_type(self):
        return self.__TYPE

    def empty(self):
        return len(self.__queue) == 0

    def qpop(self):
        return self.__queue.hpop()

    def qpush(self, value):
        if self.__TYPE is None and self._comprable(value):
            self.__TYPE = type(value)
        else:
            self._check_type(value)
        self.__queue.hpush(value)

    # Private Methods Section #
    def _check_type(self, value):
        if not isinstance(value, self.__TYPE):
            raise \
                TypeError("The collection cannot contains different types")
        self._comprable(value)

    def _comprable(self, value):
        methods = ("__lt__", "__le__", "__eq__",
                   "__ne__", "__gt__", "__ge__")
        for attr in methods:
            if not hasattr(value, attr):
                raise TypeError("Type is not comparable")
        return True


if __name__ == '__main__':
    q = PriorityQueue((5, 100, -10, 33, 12))
    print("\nCreate an interger priority queue:")
    print(f"> {q}")
    try:
        to_push = 1
        print(f"Pushing integer {to_push}:")
        q.qpush(1)
        print(f"> {q}")
        to_push = "Oops!"
        print(f"Pushing another type value '{to_push}':")
        q.qpush(to_push)
    except TypeError as err:
        print(err.args[0])

    any_q = PriorityQueue()
    print("\nCreate an optional type priority queue:")
    print(f"> {any_q}")
    print(f"Type of queue is: {any_q.get_type()}")
    print(f"Appending float value:")
    any_q.qpush(3.45)
    print(f"> {any_q}")
    print(f"Type of queue is: {any_q.get_type()}")
