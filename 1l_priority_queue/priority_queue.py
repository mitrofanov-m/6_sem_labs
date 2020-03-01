
class Heap:

    def __init__(self, order, heap=[]):
        if order not in (min, max):
            raise NameError("Incorrect order. Use 'min' or 'max'.")

        self.heap = heap
        self.order = order

        if self.heap:
            self.heapify()

    def __str__(self):
        return str(self.heap)

    def __len__(self):
        return len(self.heap)

    def in_order(self, parent, child):
        return self.order(parent, child) == parent

    def peek(self):
        return self.heap[0]

    def parent_of(self, i):
        return (i - 1) // 2

    def left_child_of(self, i):
        return 2 * i + 1

    def right_child_of(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def empty(self):
        return len(self.heap) == 0

    def hpush(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def hpop(self):
        if self.heap:
            first = self.heap[0]
            self.swap(0, -1)
            del self.heap[-1]
            self.sift_down(0)
            return first
        else:
            raise Exception("Heap is empty")

    def heapify(self):
        parent_of_last = self.parent_of(len(self.heap) - 1)
        parents = range(parent_of_last, -1, -1)

        for parent in parents:
            self.sift_down(parent)

    def sift_up(self, current):
        in_order = self.in_order
        heap = self.heap
        parent = self.parent_of(current)
        while current > 0 and not in_order(heap[parent], heap[current]):
            self.swap(current, parent)
            current = parent
            parent = self.parent_of(current)

    def sift_down(self, current):
        size = len(self.heap)
        in_order = self.in_order
        heap = self.heap

        while self.left_child_of(current) < size:
            left_child = self.left_child_of(current)
            right_child = self.right_child_of(current)
            swapped = current

            if not in_order(heap[swapped], heap[left_child]):
                swapped = left_child

            if right_child < size and \
                    not in_order(heap[swapped], heap[right_child]):
                swapped = right_child

            if swapped == current:
                return
            else:
                self.swap(current, swapped)
                current = swapped


class PriorityQueue:
    def __init__(self):
        pass


if __name__ == '__main__':
    heap1 = Heap(list, [4, 5, 1, 2, 8, 0, 9])
    print(heap1)
    heap1.hpush(10)
    print(heap1)
