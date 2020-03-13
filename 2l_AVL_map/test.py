from AVLTree import *
from Map import Map
from math import log2


print("\n------- 1 Test Tree --------\n")

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

print("""------- 2 Test Tree --------

Test the worst case for the binary tree,
appending in order 0,1...n\n""")

avltree.remove_all()
bintree.remove_all()

load = 800
for value in range(load):
    avltree.insert(value)
    bintree.insert(value)

print(f"Height of binary tree : {len(bintree)}")
print(f"Height of AVL tree    : {avltree.get_height()}")
print(f"log2({load}) : {log2(load)}")

# print("AVL tree:", avltree, sep='\n')
# print("Binary tree:", bintree, sep='\n')


print("\n\n------- Test Map --------\n")

mmap = Map()
mmap[1] = "my"
mmap[2] = "friend"
mmap[0] = "hello"

del mmap[0]
print(f"mmap = {mmap}")
print(f"mmap[2] = {mmap[2]}")
