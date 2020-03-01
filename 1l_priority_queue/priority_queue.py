
class Heap:

    def __init__(self, heap=[]):
        self.heap = heap
        if len(self.heap) != 0:
            self.heapify(len(self.heap) - 1)

    def push(self):
        pass

    def pop(self):
        pass

    def heapify(self, last_index):
        start_index = self.parent_of(last_index)

        for i in range(start_index, -1, -1):
            self.sift_down(i, last_index)

    def sift_down(self, start, last_index):
        current = start
        print(self.heap)
        while self.left_child_of(current) <= last_index:
            left_child = self.left_child_of(current)
            right_child = self.right_child_of(current)
            swapped = current

            if self.heap[left_child] > self.heap[swapped]:
                swapped = left_child

            if right_child <= last_index and self.heap[right_child] > self.heap[swapped]:
                swapped = right_child

            if swapped == current:
                return
            else:
                self.swap(current, swapped)
                current = swapped

    def parent_of(self, i):
        return (i - 1) // 2

    def left_child_of(self, i):
        return 2 * i + 1

    def right_child_of(self, i):
        return 2 * i + 2

    def swap(self, i, j):

        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp


class PriorityQueue:
    def __init__(self):
        pass


if __name__ == '__main__':
    heap = Heap([4, 5, 1, 2, 8, 0, 9])
    print(heap.heap)
