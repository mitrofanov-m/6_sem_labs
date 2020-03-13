from AVLTree import *
from Map import Map
from math import log2
from time import time
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.setrecursionlimit(1500) 


str0 = \
"""
------------ 1 Test Tree ------------

"""
print(str0)

avltree = AVLTree()
bintree = BinaryTree()
values = [0, 5, 6, 7, 8, 9, -1]

for value in values:
    avltree.insert(value)
    bintree.insert(value)

print("AVL tree:", avltree, sep='\n')
print("Binary tree:", bintree, sep='\n')
avltree.remove(7)
bintree.remove(7)
print("Remove value = 7:")
print("AVL tree:", avltree, sep='\n')
print("Binary tree:", bintree, sep='\n')

print(f"\nLen of AVL tree is: {len(avltree)}")
print(f"Binary tree contains value = 0 : {0 in bintree}")
print(avltree.get_height())


str1 = \
"""
------------ 2 Test Tree --------------

Test the worst case for the binary tree:
    - appending in order
    - searching in order
"""
print(str1)

def insert_timetest(tree, load, step):
    test = []
    len_of_tree = []
    for value in range(0,load+1):
        start = time()
        tree.insert(value)
        stop = time()
        if value % step == 0:
            test.append(stop - start)
            len_of_tree.append(value)

    return test, len_of_tree

def contains_timetest(tree, load, step):
    test = []
    len_of_tree = []
    for value in range(0,load+1):
        tree.insert(value)

    for value in range(0,load+1):
        start = time()
        result = value in tree
        stop = time()
        if value % step == 0:
            test.append(stop - start)
            len_of_tree.append(value)

    return test, len_of_tree

def mean_of(func, TreeClass, load, step):
    tests = []
    for i in range(10):
        tree = TreeClass()
        tmp, len_of_tree = func(tree, load, step)
        tests.append(tmp)

    return np.mean(tests, axis=0), len_of_tree


def plotting(title, func, load, step):
    avltime, len_of_tree = mean_of(func, AVLTree, load, step)
    bintime, len_of_tree = mean_of(func, BinaryTree, load, step)
    
    plt.plot(len_of_tree, avltime, label='AVL tree')
    plt.plot(len_of_tree, bintime, label='Binary tree')
    plt.title(title)
    plt.xlabel('len of tree')
    plt.ylabel('time')
    plt.legend()
    plt.show()

    return avltime, bintime, len_of_tree

avltime, bintime, len_of_tree = \
    plotting('Speed test of appending in worst case', insert_timetest, load=300, step=25)

for i in range(len(avltime)-1):
    if avltime[i] > bintime[i] and avltime[i+1] <= bintime[i+1]:
        print(f"AVL benefits starting between steps {len_of_tree[i]} - {len_of_tree[i+1]}")
        break 
else:
    print("AVL tree slower than simple Binary tree")

plotting('Speed test of searching in worst case', contains_timetest, load=1000, step=100)


print("\n\n------- Test Map --------\n")

mmap = Map()
mmap[1] = "my"
mmap[2] = "friend"
mmap[0] = "hello"
mmap[1] = "ooops"

del mmap[0]
print(f"mmap = {mmap}")
print(f"mmap[2] = {mmap[2]}")
